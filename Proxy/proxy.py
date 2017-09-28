#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests
import os
from bs4 import BeautifulSoup

class Proxy():
	"""docstring for Proxy"""
	def __init__(self, cnt):
		self.cnt = cnt
		self.url = 'http://www.xicidaili.com'
		self.test = 'http://ip.chinaz.com/getip.aspx'
		self.raw_ip1 = []
		self.raw_ip2 = []
		self.headers = {
		'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
		'Referer': self.url,
		}
		self.req = requests.session()

	def GetIPs(self):
		cont = self.req.get(self.url, headers=self.headers).content
		trs = BeautifulSoup(cont, 'lxml').find('table', id="ip_list").find_all('tr')
		for tr in trs:
			try:
				ip1 = tr.find_all('td')[1].text
				ip2 = tr.find_all('td')[2].text
				self.raw_ip1.append(ip1)
				self.raw_ip2.append(ip2)
			except:
				pass

	def Filter(self):
		n = cnt = 0
		self.GetIPs()
		for ip1 in self.raw_ip1:
			proxy = {
			'http': 'http://'+str(ip1),
			'https': 'https://'+str(ip1),
			}
			print ip1
			try:
				cont = self.req.get(self.test, timeout=3, proxies=proxy, headers=self.headers).content
				#print cont
				cnt += 1
				print str(cnt)+'\tis completed\t', ip1
				f = open(os.getcwd()+'/p.txt', 'a+')
				f.write(str(cnt)+'\t'+ip1+':'+self.raw_ip2[n]+'\n')
				f.close()
				if cnt > int(self.cnt):
					return
			except Exception:
				print Exception
			n += 1
			if n > 50:
				return
		print 'Done'

if __name__ == '__main__':
	cnt = raw_input("The ip counts you need is: ")
	proxy = Proxy(cnt)
	proxy.Filter()
		


