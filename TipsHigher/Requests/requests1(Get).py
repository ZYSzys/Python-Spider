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
r = requests.get('http://httpbin.org/get', params = payload, stream = True, headers = headers, timeout = 10)#timeout:超时配置
print r.url
print r.raw#通过stream=True获取原始套接字
print r.raw.read()
print r.cookies
print r.text


#SSL证书验证, 若verify=True则会出现SSLError
r = requests.get('https://kyfw.12306.cn/otn/', verify=False)
print r.text


#建立一个长久会话
s = requests.Session()
#设置cookies
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
#设置headers变量
s.headers.update({'x-test':'true'})
#获得cookies
r = s.get("http://httpbin.org/headers", headers = {'x-test':None})#若与先前设置的headers变量有冲突会覆盖，设为None则没有全局变量了
print(r.text)