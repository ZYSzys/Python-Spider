#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2

#以CSDN网站登录为例
#定义一个名为values的字典 包含参数username和password
values = {}
values['username'] = '1220736035@qq.com'
values['password'] = 'xxxxxx'
#利用urllib的urlencode方法将字典编码，命名为data
data = urllib.urlencode(values)

#get方式传送: 以链接形式直接访问，若包含了密码则不安全，可以直观地看到自己提交了什么内容
url = 'http://passport.csdn.net/account/login'
geturl = url + "?" + data
requset = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()