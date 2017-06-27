#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import requests

proxies = {
	"https": "http://41.118.132.69:4433"
}
r = requests.post('http://httpbin.org/post', proxies = proxies)
print r.text
