#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2

url = 'http://www.server.com/login'
#设置用户代理，模拟浏览器
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username':'zys', 'password':'xxxx'}
#referer：对付‘反盗链’
headers = {'User-Agent': user_agent, 'Referer':'http://www.zhihu.com/articles'}
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()