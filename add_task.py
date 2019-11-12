#! /usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ : pighui
# __time__ : 2019-11-5 下午7:36

import redis

from dytt.settings import REDIS_PORT, REDIS_HOST


def add_url(url):
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    # url = input("请输入要爬取的网址：\n")
    r.lpush('movies', url)
    # print('写入完成')
    r.close()


if __name__ == '__main__':
    urls = [
        'https://www.dy2018.com/html/gndy/dyzz/index.html',
        'https://www.dy2018.com/html/bikan/',
        'https://www.dy2018.com/html/gndy/jddyy/',
        'https://www.dy2018.com/html/tv/hytv/',
        'https://www.dy2018.com/html/tv/oumeitv/',
        'https://www.dy2018.com/html/zongyi2013/',
    ]
    for url in urls:
        add_url(url)
    print('写入完成')
