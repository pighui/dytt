# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    name = scrapy.Field()
    year = scrapy.Field()
    type = scrapy.Field()
    country = scrapy.Field()
    language = scrapy.Field()
    detail_url = scrapy.Field()
    magnet = scrapy.Field()