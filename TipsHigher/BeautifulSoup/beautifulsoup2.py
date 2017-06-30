#!/usr/bin/env python
#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup

r = requests.get('https://www.patest.cn/contests/pat-a-practise/1004')
html = r.content
#创建beautifulsoup对象
soup = BeautifulSoup(html)

#搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
print soup.find_all(id='problemContent')
print soup.find_all('p')

