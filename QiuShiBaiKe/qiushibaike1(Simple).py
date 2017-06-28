#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import urllib
import urllib2
import re

url = 'http://www.qiushibaike.com/text/'#链接
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'#代理
headers = {'User-Agent': user_agent}

request = urllib2.Request(url, headers = headers)#发送请求
response = urllib2.urlopen(request)#得到响应
content = response.read()#获取内容
pattern = re.compile('<span>(.*?)</span>.*?<span.*?><i.*?>(.*?)</i>(.*?)</span>', re.S)#模式(使用正则表达式)
items = re.findall(pattern, content)#匹配模式并查找获取有用的内容
f = open('/Users/zhangbeibei/Desktop/PSpider.txt', 'w')#保存在目标文件中('***'为文件路径)
cnt = 0
for i in items:
    haveImg = re.search('img', i[0])
    if not haveImg:#略过有图片的内容
        cnt = cnt + 1
        f.write(str(cnt)+'. '+i[0])
        f.write('\n')
        f.write('\t'+i[1]+i[2])
        f.write('\n\n')

f.close()
print 'Succeed' #爬取成功，内容保存在文件中
