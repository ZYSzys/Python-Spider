#!/usr/bin/env Python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests
from bs4 import BeautifulSoup
import re
import os

url = raw_input("输入网址: ") 
res = requests.get(url)
cont = res.content.decode('gb2312')

soup = BeautifulSoup(cont)
title = soup.title.string

pattern = re.compile('<tbody>(.*?)</tbody>', re.S)
items = re.findall(pattern, cont)
f = open(os.getcwd()+'/'+title+'.txt', 'w')
for i in items:
	soup = BeautifulSoup(i)
	ftp = soup.find_all("a")
	res = ftp[0].get('href')
	f.write(res.encode('utf-8')+'\n')
f.close()

print "Completed!"