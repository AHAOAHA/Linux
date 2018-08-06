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
#	data = data.decode("GBK").encode("utf-8")
	return data

if __name__ == "__main__":
	url = "https://music.163.com/#/song?id=190016"
	print OpenPage(url)
