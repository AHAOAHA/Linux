#!/usr/bin/python
#coding:utf-8


import urllib2

from bs4 import BeautifulSoup

import sys
import re

#取出页面的内容
def OpenPage(url):
    head = {}
    request = urllib2.Request(url,headers=head)

    f=urllib2.urlopen(request)
    data=f.read()
    data = data.decode("GBK").encode("utf-8")
    return data

#解析主页内容，获取url列表
def ParseMainPage(page):
    #调用BeautifulSoup库解析页面
    soup = BeautifulSoup(page,"html.parser")
    list_charts = soup.find_all(href=re.compile("read"))
    url_list = ["http://www.shengxu6.com" + item['href'] for item in list_charts]
    return url_list

#解析详情页内容，获取小说内容
def ParseDetailPage(page):
    soup = BeautifulSoup(page,"html.parser")
    title = soup.find_all(class_="panel-heading")[0].get_text()
    content = soup.find_all(class_="content-body")[0].get_text()
    return title,content

#把获取到的内容写到文件中
def WriteDataToFile(file_path,data):
    f = open("file_path","w")
    data = data.encode("utf-8")
    f.write(data)
    f.close()




#下面控制语句的执行	
if __name__ == "__main__":
   main_page = OpenPage("http://www.shengxu6.com/book/2967.html")
    #获取各个章节的url
    url_list = ParseMainPage(main_page)
    for url in url_list:
        #print "Clone url=" + url
        detail_page = OpenPage(url)
        title,content = ParseDetailPage(detail_page)
        print title
        data = "\n\n\n" + title + "\n\n\n" + content
        WriteDataToFile("mpnth.txt",data)
    	WriteDataToFile("mpnth.txt",data)
print "爬取完成"

'''
    main_page = OpenPage("http://www.shengxu6.com/book/2967.html")
    url_list = ParseMainPage(main_page)
    print url_list
'''
