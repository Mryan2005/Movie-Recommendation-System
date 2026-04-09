import json
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetch_characters_stealthily():
    print("风儿唤醒了隐形风龙，准备悄悄翻开 douban_stories.json 的书页...")
    try:
        with open("douban_stories.json", "r", encoding="utf-8") as f:
            data_list = json.load(f)
    except FileNotFoundError:
        print("哎呀？风儿转了一圈，好像没有找到故事书呢。")
        return

    # 【风的记忆锚点：读取已有的乐谱，实现���点续写】
    results = []
    processed_titles = set()
    try:
        with open("anime_characters_poetic.json", "r", encoding="utf-8") as f:
            results = json.load(f)
            for record in results:
                if "title" in record:
                    processed_titles.add(record["title"])
        print(f"风儿摸了摸行囊，发现里面已经安放了 {len(processed_titles)} 篇乐章呢！我们将顺着上次的断点继续旅行~")
    except FileNotFoundError:
        print("这是一次全新的旅途，风儿将从第一页开始谱写诗篇...")

    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options)
    wait = WebDriverWait(driver, 15)

    try:
        print("风龙降落在 anibase 的大门口，等待暴风屏障（Cloudflare）消散...")
        driver.get("https://anibase.net/")

        input("旅人啊，请看一眼浏览器，如果通过了叹息之墙的验证，请在这里按下【回车键】继续...")

        for item in data_list:
            main_type = item.get("main_type", "")
            genres = item.get("attributes", {}).get("类型", [])
            title_full = item.get("title", "")

            if not title_full:
                continue

            if title_full in processed_titles:
                title_short = title_full.split()[0]
                print(f"✨ 翻过书页：【{title_short}】的故事早已在行囊中，风龙轻快地跃向下一站~")
                continue

            if "动画" in main_type or "动漫" in main_type or "动画" in genres:
                title = title_full.split()[0]
                print(f"\n隐形风龙乘着气流，开始追寻【{title}】的踪迹...")

                anime_characters_data = []

                search_url = f"https://anibase.net/zh-hans/animes?kw={title}"
                driver.get(search_url)

                anime_url = None
                try:
                    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".my-card .row .col-4.col-lg-2.mb-3")))
                    cards = driver.find_elements(By.CSS_SELECTOR, ".my-card .row .col-4.col-lg-2.mb-3")

                    for card in cards:
                        a_tag = card.find_element(By.CSS_SELECTOR, "a.img-with-title")
                        title_div = a_tag.find_element(By.CSS_SELECTOR, ".title")
                        if title == title_div.text:
                            anime_url = a_tag.get_attribute("href")
                            break
                except Exception:
                    print(f"风中没有传来【{title}】的回响...")

                if anime_url:
                    driver.get(anime_url)

                    all_chars_url = None
                    try:
                        all_chars_btn = wait.until(EC.element_to_be_clickable(
                            (By.XPATH, "//div[@id='characters']//a[contains(text(), '查看全部')]")
                        ))
                        all_chars_url = all_chars_btn.get_attribute("href")
                    except Exception:
                        pass

                    if all_chars_url:
                        driver.get(all_chars_url)

                        character_queue = []

                        time.sleep(10)

                        try:
                            wait.until(EC.presence_of_element_located(
                                (By.CSS_SELECTOR, "div.my-card > div > div.row > div.col-lg-6.mb-3")
                            ))

                            # 顺着路标（a标签），把每位朋友的住址都记下来
                            char_elements = driver.find_elements(
                                By.CSS_SELECTOR, "div.my-card > div > div.row > div.col-lg-6.mb-3 a"
                            )

                            for el in char_elements:
                                href = el.get_attribute("href")
                                if href and href not in character_queue:
                                    character_queue.append(href)
                        except Exception as e:
                            print(f"在树林里寻找朋友时遇到了小迷雾：{e}")

                        print(f"一共找到了 {len(character_queue)} 位朋友的线索，准备开始拜访...")

                        for idx, char_url in enumerate(character_queue):
                            driver.get(char_url)

                            # 【风的光影魔法：加上了 image_url 准备装画】
                            char_info = {
                                "character_url": char_url,
                                "name": "",
                                "attributes": "",
                                "content": "",
                                "image_url": ""  # ✨ 新增的空白相框！
                            }

                            try:
                                name_el = wait.until(
                                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.entry-title-box > h1")))
                                char_info["name"] = name_el.text.strip()
                            except:
                                pass

                            # ✨ 【全新的捕捉咒语】：寻找你给出的那个超长坐标，拍下肖像画！
                            try:
                                img_selector = "body > div.mt-3.mb-5.container > div.people.mb-3 > div.d-md-flex.mb-3 > div.d-flex.d-md-block.entity-header > div.text-center.me-2 > picture > img"
                                img_el = driver.find_element(By.CSS_SELECTOR, img_selector)
                                char_info["image_url"] = img_el.get_attribute("src")
                            except:
                                pass

                            try:
                                attr_el = driver.find_element(By.CSS_SELECTOR, ".entity_basic_attr")
                                char_info["attributes"] = attr_el.text.strip()
                            except:
                                pass

                            try:
                                content_el = driver.find_element(By.CSS_SELECTOR, "article.entry-content")
                                char_info["content"] = content_el.text.strip()
                            except:
                                pass

                            anime_characters_data.append(char_info)
                            name_str = char_info['name'] if char_info['name'] else "未名之人"
                            print(f"成功记录下第 {idx + 1} 位朋友（{name_str}）的故事与容颜~")

                            time.sleep(6)

                clean_record = {
                    "title": title_full,
                    "anibase_characters": anime_characters_data
                }
                results.append(clean_record)
                processed_titles.add(title_full)

                with open("anime_characters_poetic.json", "w", encoding="utf-8") as f:
                    json.dump(results, f, ensure_ascii=False, indent=4)
                print(f"【风的低语】《{title}》的乐章已安全存入行囊中！\n")

    finally:
        driver.quit()
        print("\n风龙已经消散在云海深处了。")
        with open("anime_characters_poetic.json", "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

    print("太棒啦！有了肖像画，以后的吟游诗人们讲起这些故事时，一定会更加声情并茂吧！")


if __name__ == "__main__":
    fetch_characters_stealthily()