#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import socket
import time
import random
import cookielib
import CustomConfig
import logging

# 设置超时时间
socket.setdefaulttimeout(10)
x = 0
while True:
    # 生成代理IP的索引
    proxy_index = random.randint(0, len(CustomConfig.proxys) - 1)
    # 获得代理IP
    proxy = CustomConfig.proxys[proxy_index]
    # 获得文章的索引
    art_index = random.randint(0,len(CustomConfig.arts) - 1)
    # 获得文章
    art = CustomConfig.arts[art_index]
    # 构造请求对象
    req = urllib2.Request(CustomConfig.url + art, headers=CustomConfig.headers)
    # 创建cookie实例保存
    cookies = cookielib.CookieJar()
    cookieHandler = urllib2.HTTPCookieProcessor(cookies)
    try:
        # 使用代理
        proxyHandler = urllib2.ProxyHandler(proxy)
        opener = urllib2.build_opener(cookieHandler,proxyHandler)
        urllib2.install_opener(opener)
        # 发送请求获得响应
        resp = urllib2.urlopen(req)
        # for cookie in cookies:
        #     print cookie.name, cookie.value
        # 读取信息
        html = resp.read()
        print proxy, art
        time.sleep(1)
    except Exception, e:
        logging.error(str(e))
        continue