#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests
from bs4 import BeautifulSoup
import os

class mzitu():
	def all_url(self, url):
		html = self.request(url)
		all_a = BeautifulSoup(html.text, 'lxml').find('div', class_='postlist').find_all('a')
		cnt = 0	#cnt用来计数，越大程序执行时间越长，爬取内容越多
		for a in all_a:
			title = a.get_text()
			if len(title) > 5:
				print u'saving'+title
				path = str(title.encode('utf-8'))

				self.mkdir(path)
				href = a['href']
				self.html(href)
				cnt += 1
				if cnt > 4:
					break

	#在主页中找到每个图片页面的url
	def html(self, href):
		html = self.request(href)
		max_span = BeautifulSoup(html.text, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
		for page in range(1, int(max_span)+1):
			page_url = href+'/'+str(page)
			self.img(page_url)

	#在页面中找到图片的url
	def img(self, page_url):
		img_html = self.request(page_url)
		img_url = BeautifulSoup(img_html.text, 'lxml').find('div', class_='main-image').find('img')['src']
		self.save(img_url)

	#通过图片的url保存图片
	def save(self, img_url):
		name = img_url[-9:-4]
		img = self.request(img_url)
		f = open(name+'.jpg', 'ab')
		f.write(img.content)
		f.close()

	#建立存储图片的文件夹
	def mkdir(self, path):
		path = path.strip()
		isExist = os.path.exists(os.path.join(os.getcwd(), path))
		if not isExist:
			print 'make a directory:'+path
			os.makedirs(os.path.join(os.getcwd(), path))
			os.chdir(os.path.join(os.getcwd(), path))
			return True
		else:
			print 'is Existed'
			return False
			
	#对url发送请求，获取内容
	def request(self, url):
		headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
		res = requests.session()
		content = res.get(url, headers=headers, timeout=10)
		return content


MZ = mzitu()
MZ.all_url('http://www.mzitu.com')