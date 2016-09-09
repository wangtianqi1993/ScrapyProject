# !/usr/bin/env python
# -*- coding:utf-8 -*-

__author__ = 'wtq'
import os, sys
import scrapy
from scrapy.selector import Selector

parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)



class DemoSpider(scrapy.Spider):
    name = "demo"
    allowed_domains = ["dmoz.org"]
    start_urls = {
        "http://www/dmoz.org/Computer/Programming/Language/Python/Books/",
        "http://www.dmoz.org/Computer/Programming/Language/Python/Resource/"
    }

    def parse(self, response):
        # filename = response.url.split("/")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        sel = Selector()
