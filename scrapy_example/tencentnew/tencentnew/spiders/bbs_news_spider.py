from __future__ import absolute_import

# !/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'wtq'

from scrapy.spiders import Spider, Rule
from ..sunpetroitem import SunPetroItem
from scrapy.linkextractors import LinkExtractor
from ..db_operate import conn_mongo

client = conn_mongo.client_mongo()
db = client.spider


class BbsSpider(Spider):

    name = "sunpetrobbs"
    allowed_domains = ["sunpetro.cn"]
    start_urls = ["http://www.sunpetro.cn/search.php?mod=forum&searchid=1520&orderby=lastpost&ascdesc=desc&searchsubmit=yes&kw=%CA%AF%BB%AF"]

    def parse(self, response):
        i = 0
        for sel in response.xpath("//ul/li[@class='pbw']"):
        # for sel in response.xpath("//div[@class='tl']/div[@id='threadlist']/ul"):
            item = SunPetroItem()

            item['time'] = sel.xpath('//p/span/text()').extract()

            item['title'] = sel.xpath('//h3/a/text()').extract()

            item['author'] = sel.xpath('//p/span/a[@href]/text()').extract()
            # item['replay_time'] = sel.xpath('p[@class="xgl"]/text()').extract().split('-')[0]
            # item['browse_time'] = sel.xpath('p[@class="xgl"]/text()').extract().split('-')[1]
            item['url'] = sel.xpath('//h3/a/@href').extract()
            item['summary'] = sel.xpath('//p/text()').extract()
            item['channel'] = sel.xpath('//p/a[@class="xil"]/text()').extract()
            yield item
            i += 1
        print 'count.....', i

    def parse_item(self, response):

        item = SunPetroItem()
        # print db.tencent_url.find({"url":response.url}).count()
        if db.tencent_url.find({"tencent_url" : response.url}).count() == 0:
            print 'it is a new news!'
            item['url'] = response.url
            # item["title"] = response.xpath("//title/text()").extract()
            # item["content"] = response.xpath('//div[@id="Cnt-Main-Article-QQ"]/p/text()').extract()
            return item

