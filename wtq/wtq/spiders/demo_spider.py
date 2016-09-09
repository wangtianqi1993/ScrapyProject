# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wtq'


import scrapy
from scrapy.selector import Selector
from ..items import WtqItem


class DemoSpider(scrapy.Spider):
    name = "demotest"
    allowed_domains = ["dmoz.org"]
    start_urls = {
        "http://www/dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    }

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = WtqItem()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)
        return items
