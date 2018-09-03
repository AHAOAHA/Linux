#/usr/bin/python
#coding:utf-8
import sys
import urllib2
from bs4 import BeautifulSoup
myhead={}
def GetHtml(url,headers):
    req = urllib2.Request(url,headers=myhead)
    page = urllib2.urlopen(req)
    html = page.read()
    return html

if __name__ =="__main__":
    url = input()
    int i = 10
    while i>10:
        GetHtml(url,headers)
