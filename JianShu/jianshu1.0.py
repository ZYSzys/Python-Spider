#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib2
import re

url = 'http://www.jianshu.com/p/6e6ab7353859'
request = urllib2.Request(url)
response = urllib2.urlopen(request)
content = response.read()

pattern = re.compile('<title>(.*?)</title>', re.S)
title = re.findall(pattern, content)
print title[0]

pattern = re.compile('<span class="name"><a.*?>(.*?)</a></span>', re.S)
name = re.findall(pattern, content)
print name[0]

pattern = re.compile('<p>(.*?)</div>', re.S)
showcon = re.findall(pattern, content)

pattern = re.compile('<p>')
showcon[0] = re.sub(pattern, '', showcon[0])

pattern = re.compile('</p>')
showcon[0] = re.sub(pattern, '\n', showcon[0])
print showcon[0]
