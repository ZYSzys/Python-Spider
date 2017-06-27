#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2

request = urllib2.Request('http://www.xxxx.com')

#异常处理1:
'''
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	print e.reason
'''

#异常处理2:
'''
try:
	urllib2.urlopen(request)
except urllib2.HTTPError, e:
	print e.code + e.reason
'''

#异常处理3:HTTPError的父类是URLError，若子类捕获不到，则捕获父类异常
try:
	urllib2.urlopen(request)
except urllib2.HTTPError, e:
	print e.code
except urllib2.URLError, e:
	print e.reason
else:
	print 'OK'

#异常处理4:加入hasattr对属性进行判断
'''
try:
	urllib2.urlopen(request)
except urllib2.URLError, e:
	if hasattr(e, 'reason'):
		print e.reason
	else:
		print 'OK'
'''