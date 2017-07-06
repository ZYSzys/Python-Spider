#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re
import urllib

#学号密码:
usr_name = '2016........'
pass_word = '........'

#浏览器驱动:
driver = webdriver.Chrome()
driver.get('http://115.236.84.162/default5.aspx')

#寻找'class = login'输入帐号
account = driver.find_element_by_name('TextBox1')
account.clear()
account.send_keys(usr_name)

#寻找'class = password'输入密码
password = driver.find_element_by_name('TextBox2')
password.clear()
password.send_keys(pass_word)

vercode = raw_input('vercode:')
code = driver.find_element_by_name('TextBox3')
code.clear()
code.send_keys(vercode)

account.send_keys(Keys.RETURN)
time.sleep(5)

source = driver.page_source
pattern = re.compile('<span id="xhxm">(.*?)</span>', re.S)
name = re.findall(pattern, source)
xm = name[0][:3]
print xm

now_url = driver.current_url
print now_url
#print source

urlxm = urllib.quote_plus(str(xm.encode('gb2312')))
kburl = 'http://115.236.84.162/xskbcx.aspx?xh='+usr_name+'&xm='+urlxm+'&gnmkdm=N121603'
headers = {
	'Referer':'http://115.236.84.162/xs_main.aspx?xh='+usr_name,
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}
driver.get(kburl)
driver.find_element_by_link_text('here').click()
print driver.page_source
driver.close()





