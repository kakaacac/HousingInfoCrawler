# -*- coding: utf-8 -*-

import scrapy


class DoubanSpider(scrapy.Spider):
    name = "douban"
    start_urls = [
        "https://www.douban.com/group/106955/discussion?start=0",
        "https://www.douban.com/group/106955/discussion?start=25",
        "https://www.douban.com/group/106955/discussion?start=50"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=)

    def parse(self, response):
        pass