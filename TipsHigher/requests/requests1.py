#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests

#例子
r = requests.get('http://www.baidu.com')
print type(r)#类型
print r.status_code#状态码
print r.encoding#编码方式
print r.cookies

#传入参数
payload = {'key1':'value1', 'key':'value2'}
#添加headers
headers = {'content-type':'application/json'}
#利用cookies变量向服务器发送cookies信息
cookies = dict(cookies_are = 'working')
r = requests.get('http://httpbin.org/get', params = payload, stream = True, headers = headers, timeout = 5)
print r.url
print r.raw#通过stream=True获取原始套接字
print r.raw.read()
print r.cookies
print r.text