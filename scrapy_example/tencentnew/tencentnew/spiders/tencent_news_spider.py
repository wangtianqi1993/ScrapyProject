from __future__ import absolute_import

# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentnewItem
from scrapy.linkextractors import LinkExtractor
from ..db_operate import conn_mongo

client = conn_mongo.client_mongo()
db = client.spider


class TencentSpider(CrawlSpider):

    name = "tencentnews"
    allowed_domains = ["news.qq.com"]
    start_urls = ["http://news.qq.com/world_index.shtml", "http://news.qq.com/society_index.shtml", "http://mil.qq.com/mil_index.htm",
                  "http://tech.qq.com/"]
    rules = (
        # Rule(LinkExtractor(allow=("http://news\.qq\.com/[b-zA-Z0-9^/]"), deny=("http://news\.qq\.com/[b-zA-Z0-9]/"))),
        # Rule(LinkExtractor(allow=("http://news\.qq\.com/"))),
        Rule(LinkExtractor(allow=("http://news\.qq\.com/a/\w+")), callback='parse_item'),
        Rule(LinkExtractor(allow=("http://tech\.qq\.com/a/\w+")), callback='parse_item'),
    )

    def parse_item(self, response):

        item = TencentnewItem()
        # print db.tencent_url.find({"url":response.url}).count()
        if db.tencent_url.find({"tencent_url" : response.url}).count() == 0:
            print 'it is a new news!'
            item['url'] = response.url
            item["title"] = response.xpath("//title/text()").extract()
            item["content"] = response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
            return item
