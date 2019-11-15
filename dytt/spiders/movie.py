# -*- coding: utf-8 -*-
import re

from scrapy import Request
from scrapy_redis.spiders import RedisSpider


class MovieSpider(RedisSpider):
    name = 'movie'
    redis_key = 'movies'

    def parse(self, response):
        detail_url_list = response.xpath("//table[@class='tbspan']//a[@class='ulink']/@href").extract()
        for detail_url in detail_url_list:
            full_detail_url = 'https://www.dy2018.com' + detail_url
            yield Request(url=full_detail_url, callback=self.parse_item)
        try:
            next_href = response.xpath("//div[@class='x']/a[1]/@href").extract()[0]
            full_link = 'https://www.dy2018.com/' + next_href
            print(full_link)
        except:
            print('已经是最后一页了')
        else:
            yield Request(full_link, callback=self.parse)

    def parse_item(self, response):
        text = ''
        try:
            info_list = response.xpath("//div[@id='Zoom']/p/text()").extract()
        except:
            info_list = response.xpath("//div[@id='Zoom']/text()").extract()
        for info in info_list:
            text += info.replace('\xa0', '').replace('\3000', '').replace(" ", "")
        pure_text = text.replace("　　", "").replace("　", '')
        pattern = re.compile('片名(.*?)◎'
                             '年代(.*?)◎'
                             '类别(.*?)◎'
                             '语言(.*?)◎')
        items = re.findall(pattern, pure_text)
        if items:
            name, year, type, language = items[0]
            detail_url = response.url
            item = {
                'name': name,
                'type': type,
                'language': language,
                'year': year,
                'detail': detail_url
            }
            yield item
