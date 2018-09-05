#!/usr/bin/python
# coding: utf-8
__author__ = 'h___q'

import requests
from bs4 import BeautifulSoup
import multiprocessing
import time

success_num=0

CONSTANT=0
def getProxyIp():
    global CONSTANT
    proxy = []
    for i in range(1, 12):
        print i
        header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                'Ubuntu Chromium/44.0.2403.89 '
                                'Chrome/44.0.2403.89 '
                                'Safari/537.36'}
        r = requests.get('https://www.kuaidaili.com/free/inha/'.format(i), headers=header)

        html = r.text
        
        soup = BeautifulSoup(html)
        
        table = soup.find('table')
        
        tbody = table.find('tbody')
        
        tds = tbody.find_all('tr')
        print tds
        '''
        # 解析得到代理ip的地址，端口，和类型
        for item in tds:
            ips = item.find_all('td':'data-title')
            print ips
            
            print tds.get_text()
            
            temp_dict = {}
            kind = tds[5].get_text().lower()
            # exit()

            if 'http' in kind:
                temp_dict['http'] = "http://{0}:{1}".format(tds[1].get_text(), tds[2].get_text())
            if 'https' in kind:
                temp_dict['https'] = "https://{0}:{1}".format(tds[1].get_text(), tds[2].get_text())

            proxy.append(temp_dict)
    return proxy



'''
if __name__ == '__main__':
    getProxyIp()
