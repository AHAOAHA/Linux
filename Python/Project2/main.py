#!/usr/bin/python
#coding:utf-8


import urllib2
from bs4 import BeautifulSoup

import sys
def OpenPage(url):
    MyHeaders = {}
    request = urllib2.Request(url,headers = MyHeaders)
    f = urllib2.urlopen(request)
    data = f.read()
    data = data.decode("GBK").encode("utf-8")
    return data
    











if __name__ == "__main__":
    print OpenPage("http://59.74.168.16:8989/")
