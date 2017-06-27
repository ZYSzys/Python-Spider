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

#post方式传送：不会在网址上显示所有参数，直接查看提交内容不方便
url = 'http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn'
requset = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()