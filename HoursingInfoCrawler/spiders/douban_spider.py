# -*- coding: utf-8 -*-

import scrapy
from HoursingInfoCrawler import config

class DoubanSpider(scrapy.Spider):
    name = "douban"
    total_page = 20
    start_urls = ["https://www.douban.com/group/futianzufang/discussion?start={}".format(i*25) for i in range(total_page)]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, cookies=config.DOUBAN_COOKIES, headers=config.DOUBAN_HEADERS)

    def parse(self, response):
        for item in response.xpath('//table[@class="olt"]/tr/td[@class="title"]/a'):
            title = item.xpath('./@title').extract_first()
            if "石厦" in title:
                link = item.xpath('./@href').extract_first()
                print("Title: {} ---- Link: {}".format(title, link))