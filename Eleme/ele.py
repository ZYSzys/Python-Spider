#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import os
import sys
import time
from bs4 import BeautifulSoup
from selenium import webdriver

reload(sys)
sys.setdefaultencoding('utf-8')

url = 'https://www.ele.me/home/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(20)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml').prettify()
rs = BeautifulSoup(soup, 'lxml').find_all('a', class_="rstblock")
f = open(os.getcwd()+'/1.csv', 'w+')
f.write('title\tmonthsales\tcost\ttime\n')
for each in rs:
	title = each.find('div', class_="rstblock-title").string.strip()
	monthsales = each.find('span', class_="rstblock-monthsales").string.strip()
	cost = each.find('div' ,class_="rstblock-cost").string.strip()
	time = each.find('span').string.strip()
	f.write(title+'\t'+str(int(monthsales[2:-1]))+'\t'+cost+'\t'+time+'\n')

print 'OK!!'
f.close()
