#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import os
import re
from lxml import etree
import requests
import sys
import bs4
from PIL import Image

#设置编码
reload(sys)
sys.setdefaultencoding('utf-8')


uesr = '201605070523'
passw = 'xx19980903'

s = requests.session()
url = 'http://115.236.84.162/default5.aspx'
response = s.get(url)

#BeautifulSoup抓取__VIEWSTATE
soup = bs4.BeautifulSoup(response.text, 'lxml')
__VIEWSTATE = soup.find('input', attrs={'name':'__VIEWSTATE'})['value']

#获取验证码，手动输入----失败！！！！！
imgUrl = 'http://115.236.84.162/CheckCode.aspx'
pic = requests.get(imgUrl).content
with open('ver_pic.png', 'wb') as f:
	f.write(pic)
image = Image.open('{}/ver_pic.png'.format(os.getcwd()))
image.show()
code = raw_input('SecretCode:')


data = {
	'__VIEWSTATE':__VIEWSTATE,
	'TextBox1':uesr,
	'TextBox2':passw,
	'TextBox3':code,
	'TadioButtonList1':'学生',
	'Button1':'',
	'hidPdrs':'',
    'hidsc': '',
}

headers = {
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}

response = s.post(url, data = data, headers = headers)
content = response.text
print content

