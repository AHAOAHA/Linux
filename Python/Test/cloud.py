#!/usr/bin/python
#coding:utf-8
import urllib2
from bs4 import BeautifulSoup
import sys


#取出页面内容
def OpenPage(url):
    head = {}	
    request = urllib2.Request(url,headers=head)
    f = urllib2.urlopen(request)
    data = f.read()
#   data = data.decode("GBK").encode("utf-8")
    return data

if __name__ == "__main__":
    print "请输入要爬取的网页url"
    url = raw_input()
    i = 10
    while i>0:
        OpenPage(url)
        i = i - 1
    print "over"
