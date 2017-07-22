#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests
import re
import os
import sys
import urllib
import urllib2
import cookielib
from lxml import etree
from PIL import Image
from bs4 import BeautifulSoup

class WHO:
	def __init__(self, user, pswd):
		self.user = user
		self.pswd = pswd

class Tool:
	rmtb = re.compile('<br />|</br>|<br>')
	rmtime1 = re.compile('<td align="Center" width="7%">.*?</td>')
	rmtime2 = re.compile('<td class="noprint" align="Center".*?>.*?</td>')
	def replace(self, x):
		x = re.sub(self.rmtb, '---', x)
		x = re.sub(self.rmtime1, '\n', x)
		x = re.sub(self.rmtime2, '', x)
		return x.strip()

class ZAFU:

	def __init__(self, student, baseurl):
		reload(sys)
		sys.setdefaultencoding('utf-8')
		self.student = student
		self.baseurl = baseurl
		self.session  = requests.session()
		self.session.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'

	def Login(self):
		url = self.baseurl+'/default2.aspx'
		res = self.session.get(url)
		cont = res.content
		selector = etree.HTML(cont)
		__VIEWSTATE = selector.xpath('//*[@id="form1"]/input/@value')[0]
		imgurl = self.baseurl + '/CheckCode.aspx'
		imgres = self.session.get(imgurl, stream=True)
		img = imgres.content
		with open('code.jpg', 'wb') as f:
			f.write(img)
		jpg = Image.open('{}/code.jpg'.format(os.getcwd()))
		jpg.show()
		jpg.close
		code = raw_input('Input the secret code: ')

		RadioButtonList1 = u"学生".encode('gb2312', 'replace')
		data = {
			"__VIEWSTATE": __VIEWSTATE,
			"txtUserName": self.student.user,
			"TextBox1": self.student.pswd,
			"TextBox2": self.student.pswd,
			"txtSecretCode": code,
   		    "RadioButtonList1": RadioButtonList1,
		    "Button1": "", 
 		    "lbLanguage": ""        
		}
		loginres = self.session.post(url, data=data)
		logcont = loginres.text
		pattern = re.compile('<form name="Form1".*?action=(.*?) id="Form1">', re.S)
		res = re.findall(pattern, logcont)
		if res[0][17:29] == self.student.user:
			print 'Login succeed!'
		pattern = re.compile('<span id="xhxm">(.*?)</span>')
		xhxm = re.findall(pattern, logcont)
		name = xhxm[0][:3]
		return name
		
	def GetClass(self):
		name = self.Login()
		urlname = urllib.quote_plus(str(name.encode('gb2312')))
		self.session.headers['Referer'] = self.baseurl + '/xs_main.aspx?xh=' + self.student.user
		kburl = self.baseurl + '/xskbcx.aspx?xh='+self.student.user+'&xm='+urlname+'&gnmkdm=N121603'
		kbresponse = self.session.get(kburl)
		kbcont = kbresponse.text
		f = open(os.getcwd()+'/ZFKB.txt', 'w')
		pattern = re.compile('<td.*?align="Center".*?>(.*?)</td>', re.S)
		contents = re.findall(pattern, kbcont)
		tool = Tool()
		cnt = 1
		for i in contents:
			if u'星期' in i:
				continue
			elif u'第' in i:
				con = tool.replace(i)
				f.write('\t'+str(cnt)+':'+con.encode('utf-8')+'\n')
 				cnt += 1
			else:
				continue
		#关闭文件和浏览器
		f.close()
		print 'Load class succeed!'
		return True

	#爬取失败，痛心！！
	def GetGrade(self):
		name = self.Login()
		urlname = urllib.quote_plus(str(name.encode('gb2312')))
		self.session.headers['Referer'] = self.baseurl + '/xs_main.aspx?xh=' + self.student.user
		gradeurl = self.baseurl + '/xscjcx.aspx?xh='+self.student.user+'&xm='+urlname+'&gnmkdm=N121605'
		
		graderesponse = self.session.get(gradeurl)
		
		gradecont = graderesponse.content.decode("gb2312")
		soup = BeautifulSoup(gradecont.decode("utf-8"))
		__VIEWSTATE = soup.findAll(name="input")[2]["value"]
		
		self.session.headers['Referer'] = gradeurl
		
		data = {
			"__EVENTTARGET":"",
			"__EVENTARGUMENT":"",
			"__VIEWSTATE":__VIEWSTATE,
			"hidLanguage":"",
			"ddlXN":"",
			"ddlXQ": "",
			"ddl_kcxz":"",
			"btn_zcj" : u'历年成绩'.encode('gb2312', 'replace')
		}
		grares = self.session.post(gradeurl, data=data)
		gracont = grares.text
		print gradecont

if __name__ == "__main__":
	url = 'http://..........'
	user = '2016........'
	pswd = '..........'
	who = WHO(user, pswd)
	zafu = ZAFU(who, url)
	#zafu.GetClass()
	zafu.GetGrade()