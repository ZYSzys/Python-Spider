#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import re

class Tool:
	rmtb = re.compile('<br>')
	rmtime2 = re.compile('<td align="Center" width="7%">.*?</td>')
	rmtime3 = re.compile('<td class="noprint" align="Center".*?>.*?</td>')
	'''
	rmtime1 = re.compile('<td colspan="2".*?>.*?</td>')
	rmk = re.compile('<td align="Center"></td>')
	'''
	def replace(self, x):
		x = re.sub(self.rmtb, '--', x)
		x = re.sub(self.rmtime2, '\n', x)
		x = re.sub(self.rmtime3, '', x)
		'''
		x = re.sub(self.rmtime1, '', x)
		x = re.sub(self.rmk, '', x)
		'''
		return x.strip()


#账号密码:
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

#soup = BeautifulSoup(driver.page_source)
#print soup.title.string

html = driver.page_source
pattern = re.compile('<td align="Center" rowspan="2" width="7%">(.*?)</td>', re.S)
contents = re.findall(pattern, html)
tool = Tool()
for i in contents:
	print tool.replace(i)

#print tool.replace(content[0])
#print content[0]

driver.close()





