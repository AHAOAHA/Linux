#!/usr/bin/python
#coding:utf-8
'''
从小说网站抓取一本小说
'''
#Python库，提供一系列针对url的操作方法
import urllib2
#Re正则表达式库，提供一系列针对正则表达式的方法
import re

from bs4 import BeautifulSoup

import sys
#获取页面内容
def OpenPage(url): 
    Myheaders = {}
    #urllib2.Request()填写两个参数，第一个参数是url，第二个参数是我们的请求头
    request = urllib2.Request(url,headers=Myheaders)
    #类文件对象
    #urlopen发送指令请求  
    f = urllib2.urlopen(request) 
    #f.read()读取响应对象的内容
    data = f.read()
    #编码解码方法 decode解码 encode编码
    return data.decode("GBK",errors="ignore").encode("utf-8")
    #return data

#测试访问页面内容：
def Test1():
    print OpenPage("http://www.shengxu6.com/book/2967.html")

#解析主页内容，获取url列表
def ParseMainPage(page):
    #调用BaeautifulSoup库解析页面
    soup = BeautifulSoup(page,"html.parser")
    #find_all方法查询所有的指定内容
    #包含read字符串的href链接  通过正则表达式
    list_charts = soup.find_all(href=re.compile("read"))
    #每一个item是一个tag标签类的实例化对象
    #通过item['herf']可以获取到herf的值
    url_list = ["http://www.shengxu6.com"+item['href'] for item in list_charts]
    return soup

def Test2():
    page = OpenPage("http://www.shengxu6.com/book/2967.html")
    print ParseMainPage(page)#解析详情页内容，获取到小说正文

def PraseDetailPage(page):
    soup = BeautifulSoup(page,"html.parser")
    title = soup.find_all(class_="panel-heading")[0].get_text()
    content = soup.find_all(class_="content-body")[0].get_text()
    return title,content

def Test3():
    page = OpenPage("http://www.shengxu6.com/read/2967_2008734.html")
    title = ParseDetailPage(page)
    print title
    print content[:-12]


#把获取到的内容写入文件中
def WriteDataToFile(file_path,data):
    f = open(file_path,"a+")
    f.write(data)
    f.close()
    #with open(file_path,"a+") as f:
    #    f.write(data)

def Test4():
    WriteDataToFile("tmp.txt","aisdnoasidno\n")
    WriteDataToFile("tmp.txt","aisdnoasidion\n")






if __name__ == "__main__":
    #构建完整的爬虫应用
    #小说的主页
    url = "http://www.shengxu6.com/book/2967.html"
    #获取主页内容
    main_page = OpenPage(url)
    #获取主页内的各个章节的url
    url_list = ParseMainPage(main_page)
    for url in url_list:
        print "Clone url=" +url
        detail_page = OpenPage(url)
        title,content = ParseDetailPage(detail_page)
        data = "\n\n\n"+title+"\n\n\n"+content
        data = data.encode("mpnth.txt",data)
        WriteDataToFile("mpnth.txt",data)
        WriteDataToFile("mpnth.txt",data)
        

    print "爬取完成"

