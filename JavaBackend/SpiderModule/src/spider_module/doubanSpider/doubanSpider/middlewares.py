# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

import random
import string
from scrapy.http import HtmlResponse

class DoubanspiderSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class DoubanspiderDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class DoubanAdvancedMiddleware:
    """
    针对豆瓣 2025 反爬设计的进阶中间件
    功能：动态 bid 生成、现代浏览器指纹模拟、Referer 自动补全
    """

    def process_request(self, request, spider):
        # 1. 动态生成 bid (豆瓣用来追踪设备的关键 Cookie)
        # 如果你没在 settings 里写死 Cookie，这里会随机生成一个，模拟新访客
        if b'Cookie' not in request.headers:
            random_bid = "".join(random.sample(string.ascii_letters + string.digits, 11))
            request.headers['Cookie'] = f'bid={random_bid}'

        # 2. 模拟现代浏览器的 Client Hints (这是知乎文章提到的关键，防止 403)
        request.headers['sec-ch-ua'] = '"Microsoft Edge";v="147", "Not.A/Brand";v="8", "Chromium";v="147"'
        request.headers['sec-ch-ua-mobile'] = '?0'
        request.headers['sec-ch-ua-platform'] = '"Windows"'
        request.headers['sec-fetch-dest'] = 'document'
        request.headers['sec-fetch-mode'] = 'navigate'
        request.headers['sec-fetch-site'] = 'same-origin'
        request.headers['sec-gpc'] = '1'

        # 3. 动态 Referer 策略
        # 如果当前抓取的是电影详情页，把来源设置为豆瓣电影首页
        if 'subject/' in request.url:
            request.headers['Referer'] = 'https://movie.douban.com/'

        return None

    def process_response(self, request, response, spider):
        # 4. 检测是否触发了验证码重定向 (sec.douban.com)
        if response.status in [302, 301] and "sec.douban.com" in response.headers.get('Location', b'').decode():
            spider.logger.error(f"🛑 触发硬核验证！IP可能被暂时封禁。URL: {request.url}")
            # 这里可以选择直接关闭爬虫，或者在此处集成代理切换逻辑

        # 5. 如果遇到 403，说明 Header 模拟还是没过关或者频率太快
        if response.status == 403:
            spider.logger.warning(f"⚠️ 收到 403 响应，建议增加 DOWNLOAD_DELAY 或更换 Cookie/IP")

        return response