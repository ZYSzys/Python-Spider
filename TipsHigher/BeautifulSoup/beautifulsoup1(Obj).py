#!/usr/bin/env python
#-*- coding: utf-8 -*_

__author__ = 'ZYSzys'

import urllib2
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.patest.cn/contests/pat-a-practise/1004')
html = r.content
#创建beautifulsoup对象
soup = BeautifulSoup(html)

#格式化输出内容
#print soup.prettify()

#获取标签内容，只能获取到所有内容中第一个符合要求的标签

print soup.head
print soup.title
print soup.a
print soup.p
print type(soup.p)

#四大对象种类


#Tag:
#Tag的name属性: 标签本身的名称
print soup.name
print soup.head.name
#Tag的attrs属性: 得到标签的所有属性
print soup.script.attrs
print soup.script['src']
print soup.script.get('type')
#更改 soup.script['src'] = 'pic'
#删除 del soup.script['type']

#NavigableString:
#.string获取标签内部的文字
print soup.title.string
print type(soup.title.string)

#BeautifulSoup: 是一个特殊的Tag

#Comment: 是一个特殊的NavigableString对象
