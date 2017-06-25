#!usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2

url = 'http://www.baidu.com'
request = urllib2.Request(url, data = data, timeout = 10)

#http请求方式，使用次数较少
request.get_method = lambda: 'PUT' # or 'DELETE'/'GET'/'HEAD'......
response = urllib2.urlopen(request)

#使用DebugLog，方便调试
httpHandler = urllib2.HTTPHandler(debuglevel = 1)
httpsHandler = urllib2.HTTPSHandler(debuglevel = 1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen(url)