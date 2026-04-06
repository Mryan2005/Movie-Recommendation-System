import scrapy


class DoubanmovieSpider(scrapy.Spider):
    name = "doubanMovie"
    # 允许主站和安全验证站（防止跳转报错）
    allowed_domains = ["movie.douban.com", "sec.douban.com"]
    start_urls = ["https://movie.douban.com", "https://movie.douban.com/subject/36172038/"]

    custom_settings = {
        'ROBOTSTXT_OBEY': False,
        'DOWNLOAD_DELAY': 10,  # 豆瓣抓取建议保持延迟
        'COOKIES_ENABLED': True,
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.9',
        }
    }

    def parse(self, response):
        # 1. 遇到验证码页面直接跳过
        if "sec.douban.com" in response.url:
            self.logger.warning(f"验证码拦截: {response.url}")
            return

        # 2. 提取当前页面所有链接
        all_links = response.css('a::attr(href)').getall()

        for link in all_links:
            # 只关注电影详情页 URL
            if 'subject/' in link:
                # 清洗 URL，去掉查询参数（?from=... 等），只保留 ID 部分
                full_url = response.urljoin(link).split('?')[0]

                # 确保 URL 是以 / 结尾的规范格式
                if not full_url.endswith('/'):
                    full_url += '/'

                # 3. 输出 URL
                yield {
                    'subject_url': full_url
                }

                # 4. 递归：顺着这个详情页点进去，寻找更多链接
                # Scrapy 会自动根据 URL 进行去重，不会重复抓取同一个页面
                yield scrapy.Request(full_url, callback=self.parse)