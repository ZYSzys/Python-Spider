#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie件,之后写入文件
cookie = cookielib.MozillaCookieJar()
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata = urllib.urlencode({
	'stuid':'201605070523',
	'pwd':'201605070523'
	})
#登录教务系统的url
LoginUrl = 'http://~~~~~~~~.login'
#模拟登录，并把cookie保存到变量
result = opener.open(LoginUrl, postdata)
#保存cookie到cookie.txt中
cookie.save(ignore_discard = True, ignore_expires = True)
#利用cookie请求访问另一个网址，此网址是成绩查询网址
GradeUrl = 'http://~~~~~~~~~~~~~'
#请求访问成绩查询网址
result = opener.open(GradeUrl)
print result.read()