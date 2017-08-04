#!/usr/bin/env python
#-*- coding: utf-8 -*-
import urllib2
import re
import urllib
from sgmllib import SGMLParser

class ListName(SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_span = ""
        self.name = []
    def start_span(self, attrs):
        self.is_span = 1
    def end_span(self):
        self.is_span = ""
    def handle_data(self, text):
        if self.is_span == 1:
            self.name.append(text)

url = 'http://www.qiushibaike.com/hot/page/1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url, headers = headers)
response = urllib2.urlopen(request)
content = response.read()
listname = ListName()
listname.feed(content)
for item in listname.name:
    haveImg = re.search('img', item)
    if not haveImg:
        print item

