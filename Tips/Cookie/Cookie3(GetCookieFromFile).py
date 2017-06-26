#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib2
import cookielib

#声明一个MozillaCookieJar对象实例来保存cookie件
cookie = cookielib.MozillaCookieJar()
#从文件中读取cookie内容到变量
cookie.load('cookie.txt', ignore_discard = True, ignore_expires = True)
#创建请求的request
request = urllib2.Request("http://www.baidu.com")
#利用urllib2的build_opener方法创建一个opener
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(request)
print response.read()
