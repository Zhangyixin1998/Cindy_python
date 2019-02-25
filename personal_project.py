# -*- coding:utf-8 -*-
import time
from bs4 import BeautifulSoup
import requests
from urllib import request
import urllib
import sys
import os
import importlib

"""
环境 python3
pip3 install BeautifulSoup4
pip3 install requests
pip3 install lxml
"""
importlib.reload(sys)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, compress',
    'Accept-Language': 'en-us;q=0.5,en;q=0.3',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'
}


def gettxtfromBaidu(word):
    try:
        os.remove('url.txt')
    except:
        pass
    start = time.time()
    file_id = 1
    url = 'https://www.baidu.com.cn/s?wd=' + urllib.parse.quote(word) + '&pn=' 
    for k in range(1, 10): #前十页的内容
        geturl(url, k)
    for url in open('url.txt'):
        print(url.strip())
        save_html(url.strip(), file_id)
        file_id += 1
    end = time.time()
    print(end - start)


def save_html(url, filename):
    page1 = requests.get(url)
    f = open(str(filename) + '.html', 'wb')
    f.write(page1.content)
    f.close()
    return page1


def geturl(url, k):#获取前十页各网页url
    path = url + str((k - 1) * 10)
    response = request.urlopen(path)
    page = response.read()
    soup = BeautifulSoup(page, 'lxml')
    jjj = soup.find_all('h3')
    for h3 in jjj:
        href = h3.find('a').get('href')
        baidu_url = requests.get(url=href, headers=headers, allow_redirects=False)
        raw_url = baidu_url.headers['Location']  # 得到网页原始地址
        if raw_url.startswith('http'):
            try:
                with open('url.txt', 'a') as f:
                    f.write(raw_url + '\n')
                    f.close()
            except Exception as e:
                print(e)

        # all.write(raw_url + '\n')


if __name__ == '__main__':
    gettxtfromBaidu('张以欣')
