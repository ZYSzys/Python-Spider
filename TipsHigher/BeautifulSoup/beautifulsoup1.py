#!/usr/bin/env python
#-*- coding: utf-8 -*_

__author__ = 'ZYSzys'

import urllib2
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.patest.cn/contests/pat-a-practise/1004')
html = r.content
soup = BeautifulSoup(html)

#格式化输出内容
#print soup.prettify()

#获取标签内容，只能获取到所有内容中第一个符合要求的标签

print soup.head
print soup.title
print soup.a
print soup.p
print type(soup.p)

#Tag的name属性
print soup.name
print soup.head.name
#Tag的attrs属性
print soup.div.attrs

#搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
print soup.find_all(id='problemContent')
print soup.find_all('p')