# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wtq'
import scrapy
from scrapy.selector import Selector
from testnew.testnew.items import TestnewItem


class DemoSpider(scrapy.Spider):
    name = "testnew"
    allowed_domains = ["dmoz.org"]
    start_urls = {
        "http://www/dmoz.org/Computer/Programming/Language/Python/Books/",
        "http://www.dmoz.org/Computer/Programming/Language/Python/Resource/"
    }

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="directory-url"]/li')
        items = []

        for site in sites:
            item = TestnewItem()
            item['name'] = site.xpath('a/text()').extract()
            item['url'] = site.xpath('a/@href').extract()
            item['description'] = site.xpath('text()').re('-\s[^\n]*\\r')
            items.append(item)

        return items
