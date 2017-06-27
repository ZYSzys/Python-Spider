#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2

#代理
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":'http://some-proxy.com:8080'})
#系统默认环境变量
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
	opener = urllib2.build_opener(proxy_handler)
else:
	opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#Set Timeout
response = urllib2.urlopen('http://www.baidu.com', timeout = 10)