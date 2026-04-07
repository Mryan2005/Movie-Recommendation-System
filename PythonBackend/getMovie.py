import json
import time
import re
from collections import deque
from urllib.parse import urljoin, urlparse, parse_qs, urlencode

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException


SUBJECT_MAIN_RE = re.compile(r"^https?://movie\.douban\.com/subject/(\d+)/?")

# 这些是 subject 的子页面，访问它们通常更慢、更容易触发风控；我们统一不访问
SUBJECT_SUBPATH_BLOCKLIST = (
    "/questions/",
    "/review/",
    "/reviews",
    "/discussion/",
    "/comments",
    "/photos",
    "/celebrities",
    "/trailer",
)


def normalize_url(base_url: str, href: str) -> str | None:
    """把相对链接变成绝对链接，并去掉 #fragment。"""
    if not href:
        return None
    abs_url = urljoin(base_url, href)
    parsed = urlparse(abs_url)
    if parsed.scheme not in ("http", "https"):
        return None
    return parsed._replace(fragment="").geturl()


def canonicalize_remove_from(url: str) -> str:
    """
    canonical 用于去重：
    - 去掉 fragment
    - 去掉 query 里的 from
    - 其他 query 保留
    """
    p = urlparse(url)
    qs = parse_qs(p.query, keep_blank_values=True)
    qs.pop("from", None)
    new_query = urlencode(qs, doseq=True)
    return p._replace(query=new_query, fragment="").geturl()


def has_from_query(url: str) -> bool:
    """判断 URL 是否带 ?from=..."""
    p = urlparse(url)
    qs = parse_qs(p.query, keep_blank_values=True)
    return "from" in qs


def subject_main_url(url: str) -> str | None:
    """把任何 subject 相关链接提纯成主页面：https://movie.douban.com/subject/<id>/"""
    m = SUBJECT_MAIN_RE.match(url)
    if not m:
        return None
    sid = m.group(1)
    return f"https://movie.douban.com/subject/{sid}/"


def is_subject_main_url(url: str) -> bool:
    """严格判断是否为 subject 主页面（而不是 /questions/ /review/ 等子页面）。"""
    main = subject_main_url(url)
    return main is not None and url.rstrip("/") + "/" == main


def save_json_incrementally(path: str, data: list[dict]) -> None:
    """边爬边存：每新增一条就覆盖写一次（简单可靠）。"""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def parse_style_background_image(style_value: str) -> str:
    """从 style="background-image: url(...)" 提取图片 URL。"""
    if not style_value:
        return ""
    m = re.search(r"background-image\s*:\s*url\((['\"]?)(.*?)\1\)", style_value, flags=re.I)
    return m.group(2).strip() if m else ""


def extract_poster_image_url(soup: BeautifulSoup) -> str:
    """提取主海报图：#mainpic img[src]"""
    img = soup.select_one("#mainpic img")
    if img and img.get("src"):
        return img["src"].strip()
    return ""


def extract_info_attributes(soup: BeautifulSoup) -> dict:
    """
    解析 <div id="info">，将每个字段拆成独立属性：
    - 用 <span class="pl"> 作为 key
    - 收集其后兄弟节点直到 <br>
    """
    info_dict: dict = {}
    info_div = soup.find(id="info")
    if not info_div:
        return info_dict

    for pl_tag in info_div.find_all("span", class_="pl"):
        key = pl_tag.get_text(strip=True).replace("：", "").replace(":", "").strip()

        chunks: list[str] = []
        for sib in pl_tag.next_siblings:
            if getattr(sib, "name", None) == "br":
                break
            text = sib.get_text(" ", strip=True) if hasattr(sib, "get_text") else str(sib).strip()
            if text:
                chunks.append(text)

        value_str = " ".join(chunks).strip()
        value_str = value_str.replace("更多...", "").strip()
        value_str = value_str.lstrip(":：").strip()

        if " / " in value_str:
            value = [v.strip() for v in value_str.split(" / ") if v.strip()]
        else:
            value = value_str

        if key and value:
            info_dict[key] = value

    # 类型通常更适合取成列表
    genres = [g.get_text(strip=True) for g in info_div.find_all("span", property="v:genre")]
    if genres:
        info_dict["类型"] = genres

    # 多值字段兜底拆分
    for multi_key in ("上映日期", "片长"):
        if multi_key in info_dict and isinstance(info_dict[multi_key], str) and " / " in info_dict[multi_key]:
            info_dict[multi_key] = [v.strip() for v in info_dict[multi_key].split(" / ") if v.strip()]

    return info_dict


def extract_synopsis(soup: BeautifulSoup) -> str:
    """提取剧情简介：优先 span[property=v:summary]，否则 #link-report-intra"""
    summary_tag = soup.find("span", property="v:summary")
    if summary_tag:
        return summary_tag.get_text(strip=True)

    report_div = soup.find(id="link-report-intra")
    if report_div:
        return report_div.get_text(" ", strip=True)

    return ""


def extract_celebrities(soup: BeautifulSoup) -> list[dict]:
    """
    提取演职员（含头像）：
    - name: span.name
    - role: span.role
    - person_url: span.name a[href]
    - avatar_url: div.avatar style 里的 background-image url(...)
    """
    result: list[dict] = []
    ul = soup.find("ul", class_="celebrities-list")
    if not ul:
        return result

    for li in ul.find_all("li", class_="celebrity"):
        name_span = li.find("span", class_="name")
        role_span = li.find("span", class_="role")
        if not name_span or not role_span:
            continue

        name = name_span.get_text(strip=True)
        role = role_span.get_text(strip=True)

        a = name_span.find("a", href=True)
        person_url = a["href"].strip() if a else ""

        avatar_div = li.select_one("div.avatar")
        avatar_url = parse_style_background_image(avatar_div.get("style", "")) if avatar_div else ""

        if name and role:
            result.append(
                {
                    "name": name,
                    "role": role,
                    "person_url": person_url,
                    "avatar_url": avatar_url,
                }
            )
    return result


def classify_main_type(attributes: dict) -> str:
    """
    分类规则（按你的需求）：
    1) 类型含“动画” => 动画
    2) 出现“片长” => 电影
    3) 类型里出现包含“剧”的项 => 电视剧
    否则 => 未知
    """
    genres = attributes.get("类型", [])
    if isinstance(genres, str):
        genres_list = [genres]
    else:
        genres_list = [g for g in genres if isinstance(g, str)]

    if any("动画" in g for g in genres_list):
        return "动画"

    if "片长" in attributes and attributes.get("片长"):
        return "电影"

    if any("剧" in g for g in genres_list):
        return "电视剧"

    return "未知"


def safe_get(driver, url: str, sleep_seconds: float) -> bool:
    """给 driver.get 增加超时兜底；超时就 stop 并返回 False。"""
    try:
        driver.get(url)
        time.sleep(sleep_seconds)
        return True
    except TimeoutException:
        try:
            driver.execute_script("window.stop();")
        except Exception:
            pass
        return False
    except WebDriverException:
        return False


def should_enqueue(candidate_url: str, visited: dict[str, bool]) -> str | None:
    """
    入队列条件（按你的三条 + 稳定性增强）：
    1) 要包含 subject
    2) 要有 ?from
    3) visited 里没有（原始 + 去 from + 主页面都算）
    返回：入队用的 URL（统一返回 subject 主页面），不满足则返回 None
    """
    if "subject" not in candidate_url:
        return None
    if not has_from_query(candidate_url):
        return None

    # 如果是明显的 subject 子页面链接，直接不入队
    for bad in SUBJECT_SUBPATH_BLOCKLIST:
        if bad in candidate_url:
            return None

    main = subject_main_url(candidate_url)
    if not main:
        return None

    canonical = canonicalize_remove_from(candidate_url)
    main_canonical = canonicalize_remove_from(main)

    if candidate_url in visited:
        return None
    if canonical in visited:
        return None
    if main in visited:
        return None
    if main_canonical in visited:
        return None

    return main


def wandering_in_douban(
    seed_urls: list[str] | None = None,
    output_json: str = "douban_stories.json",
    sleep_seconds: float = 2.0,
    headless: bool = False,
    max_pages: int | None = None,
    page_load_timeout: int = 30,
):
    if seed_urls is None:
        seed_urls = [
            "https://movie.douban.com",
            "https://movie.douban.com/subject/36172038/",
            "https://movie.douban.com/subject/26596140/",
            "https://movie.douban.com/subject/1464448/",
            "https://movie.douban.com/subject/1300883/",
            "https://movie.douban.com/subject/1297747/",
            "https://movie.douban.com/subject/35914259/",
            "https://movie.douban.com/subject/37375594/",
            "https://movie.douban.com/subject/25728590/",
            "https://movie.douban.com/subject/1291543/",
            "https://movie.douban.com/subject/1299645/",
            "https://movie.douban.com/subject/1293351/",
        ]

    url_queue = deque(seed_urls)

    # visited 里同时存：原始、remove-from、main、main-remove-from（多重去重，减少重复访问）
    visited_urls: dict[str, bool] = {}
    collected: list[dict] = []

    options = Options()
    if headless:
        options.add_argument("--headless")

    print("正在唤醒 Firefox...")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(page_load_timeout)
    driver.set_script_timeout(page_load_timeout)

    pages_visited = 0
    fail_count = 0

    try:
        while url_queue:
            if max_pages is not None and pages_visited >= max_pages:
                print(f"已达到 max_pages={max_pages}，停止。")
                break

            current_url = url_queue.popleft()
            current_url = normalize_url("https://movie.douban.com", current_url)
            if not current_url:
                continue

            # 访问统一用 subject 主页面（稳定）
            main = subject_main_url(current_url) or current_url

            current_canonical = canonicalize_remove_from(current_url)
            main_canonical = canonicalize_remove_from(main)

            if (
                current_url in visited_urls
                or current_canonical in visited_urls
                or main in visited_urls
                or main_canonical in visited_urls
            ):
                continue

            # 标记访问：四种都记录
            visited_urls[current_url] = True
            visited_urls[current_canonical] = True
            visited_urls[main] = True
            visited_urls[main_canonical] = True

            pages_visited += 1
            print(f"[{pages_visited}] 访问: {main}")

            ok = safe_get(driver, main, sleep_seconds=sleep_seconds)
            if not ok:
                fail_count += 1
                print(f"  超时/驱动异常，跳过: {main} (fail_count={fail_count})")

                # 连续失败就重启浏览器
                if fail_count >= 3:
                    try:
                        driver.quit()
                    except Exception:
                        pass
                    driver = webdriver.Firefox(options=options)
                    driver.set_page_load_timeout(page_load_timeout)
                    driver.set_script_timeout(page_load_timeout)
                    fail_count = 0
                continue

            fail_count = 0

            soup = BeautifulSoup(driver.page_source, "html.parser")

            # 简单检测验证页（可按需扩展）
            html_lower = driver.page_source.lower()
            if "captcha" in html_lower or "验证" in driver.page_source:
                print("  疑似触发验证页，先跳过：", main)
                continue

            # 只解析 subject 主页面
            if is_subject_main_url(main):
                h1 = soup.find("h1")
                title = h1.get_text(" ", strip=True) if h1 else ""

                attributes = extract_info_attributes(soup)

                story = {
                    "url": main,
                    "title": title,
                    "poster_image_url": extract_poster_image_url(soup),
                    "attributes": attributes,
                    "main_type": classify_main_type(attributes),  # 新增：分类结果
                    "synopsis": extract_synopsis(soup),
                    "celebrities": extract_celebrities(soup),
                }

                collected.append(story)
                save_json_incrementally(output_json, collected)
                print(f"  已写入 JSON：{title or '(no title)'} | main_type={story['main_type']}")

            # 抽取链接：必须 subject + 必须 ?from + 多重去重；入队统一是主页面
            for a in soup.find_all("a", href=True):
                href = a["href"].strip()
                next_url = normalize_url(main, href)
                if not next_url:
                    continue

                # 限制域名，避免跑偏
                if urlparse(next_url).netloc != "movie.douban.com":
                    continue

                enqueue_url = should_enqueue(next_url, visited_urls)
                if enqueue_url:
                    url_queue.append(enqueue_url)

        print("-" * 60)
        print(f"结束：访问页面数={pages_visited}，visited key 数={len(visited_urls)}，收集 subject 数={len(collected)}")
        print(f"输出文件：{output_json}")

    finally:
        driver.quit()


if __name__ == "__main__":
    wandering_in_douban(
        output_json="douban_stories.json",
        sleep_seconds=6,
        headless=False,
        max_pages=2001,
        page_load_timeout=30,
    )