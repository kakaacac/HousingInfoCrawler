# -*- coding: utf-8 -*-

import Scrapy

class DoubanSpider(Scrapy.Spider):
    name = "douban"
    start_urls = [
        "https://www.douban.com/group/106955/discussion?start=0",
        "https://www.douban.com/group/106955/discussion?start=25",
        "https://www.douban.com/group/106955/discussion?start=50"
    ]

    def parse(self, response):
        pass