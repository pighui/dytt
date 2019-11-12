# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy_redis.spiders import RedisSpider

from dytt.items import MovieItem


class MovieSpider(RedisSpider):
    name = 'movie'
    redis_key = 'movies'

    def parse(self, response):
        detail_url_list = response.xpath("//table[@class='tbspan']//a[@class='ulink']/@href").extract()
        for detail_url in detail_url_list:
            full_detail_url = 'https://www.dy2018.com' + detail_url
            yield Request(url=full_detail_url,callback=self.parse_item,dont_filter=True)
        try:
            next_href = response.xpath("//div[@class='x']/a[1]/@href").extract()[0]
            full_link = 'https://www.dy2018.com/' + next_href
            print(full_link)
        except:
            print('已经是最后一页了')
        else:
            yield Request(full_link, callback=self.parse, dont_filter=True)


    def parse_item(self,response):
        item = MovieItem()
        item['name'] = response.xpath("//div[@id='Zoom']/p[2]/text()").extract()[0].split("名")[1].strip(" ")
        item['year'] = response.xpath("//div[@id='Zoom']/p[3]/text()").extract()[0].split("代")[1].strip(" ")
        item['country'] = response.xpath("//div[@id='Zoom']/p[4]/text()").extract()[0].split("地")[1].strip(" ")
        item['type'] = response.xpath("//div[@id='Zoom']/p[5]/text()").extract()[0].split("别")[1].strip(" ")
        item['language'] = response.xpath("//div[@id='Zoom']/p[6]/text()").extract()[0].split("言")[1].strip(" ")
        item['detail_url'] = response.url
        item['magnet'] = response.xpath("//div[@id='Zoom']/table[1]/tbody/tr/td/a[1]/text()").extract()[0]
        yield item
