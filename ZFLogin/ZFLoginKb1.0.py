#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

#账号密码:
usr_name = '201605070523'
pass_word = 'xx19980903'

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
print name[0]

now_url = driver.current_url
print now_url
#print source

kburl = 'http://115.236.84.162/xskbcx.aspx?xh=201605070523&xm=%D5%C2%D3%C0%CA%A4&gnmkdm=N121603'
headers = {
	'Referer':'http://115.236.84.162/xs_main.aspx?xh=201605070523',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}
driver.get(kburl)
driver.find_element_by_link_text('here').click()
print driver.page_source
driver.close()





