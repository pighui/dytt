#! /usr/bin/env python
# -*-coding:UTF-8-*-
# __author__ : pighui
# __time__ : 2019-11-5 下午7:36

import redis

from dytt.settings import REDIS_PORT, REDIS_HOST


def add_url():
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    url_list = [
        'https://www.dy2018.com/html/gndy/dyzz/index.html',
        'https://www.dy2018.com/html/bikan/',
        'https://www.dy2018.com/html/gndy/index.html',
        'https://www.dy2018.com/html/gndy/jddyy/',
        'https://www.dy2018.com/html/tv/hytv/',
        'https://www.dy2018.com/html/tv/rihantv/',
        'https://www.dy2018.com/html/tv/oumeitv/',
        'https://www.dy2018.com/html/zongyi2013/',
    ]
    for url in url_list:
        r.lpush('movies', url)
    print("写入完成")
    r.close()


if __name__ == '__main__':
    add_url()
