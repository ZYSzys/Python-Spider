#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.patest.cn/contests/pat-a-practise/1004')
html = r.content
#创建beautifulsoup对象
soup = BeautifulSoup(html)

#搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
print soup.find_all('p')
print soup.find_all(id='problemContent')
for tag in  soup.find_all(True):
	print tag.name

def has_class_but_not_id(tag):
	return tag.has_attr('class') and not tag.has_attr('id')
print soup.find_all(has_class_but_not_id)