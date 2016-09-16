import scrapy
from scrapy.item import Field


class SunPetroItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    time = Field()
    title = Field()
    html = Field()
    url = Field()
    summary = Field()
    replay_times = Field()
    browse_times = Field()
    author = Field()
    channel = Field()
