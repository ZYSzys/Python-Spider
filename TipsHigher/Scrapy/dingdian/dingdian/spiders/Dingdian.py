#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import scrapy
from scrapy.http import Request
from bs4 import BeautifulSoup
from dingdian.items import DingdianItem

class DingdianSpider(scrapy.Spider):
    name = "Dingdian"
    allowed_domains = ["x23us.com"]
    bash_url = 'http://www.x23us.com/class/'
    bashurl = '.html'
    cnt = 0

    def start_requests(self):
        for i in range(1, 11):
            url = self.bash_url + str(i) + '_1' + self.bashurl
            yield Request(url)

    def parse(self, response):
        max_page = BeautifulSoup(response.text, 'lxml').find('div', class_='pagelink').find_all('a')[-1].get_text()
        bashurl = str(response.url)[:-7]
        for i in range(1, (int)(max_page)+1):
            url = bashurl + '_' + str(i) + self.bashurl
            yield Request(url ,callback=self.get_name)

    def get_name(self, response):
        names = BeautifulSoup(response.text, 'lxml').find_all('tr', bgcolor='#FFFFFF')
        for tr in names:
            info = tr.find_all('a')
            name = info[1].get_text()
            url = info[0]['href']
            yield Request(url, callback=self.get_chapterurl, meta={'name': name, 'url': url})

    def get_chapterurl(self, response):
        item = DingdianItem()
        time.sleep(1)
        item['name'] = response.meta['name']
        item['novelurl'] = response.meta['url']
        category = BeautifulSoup(response.text, 'lxml').find('table').find('a').string
        author = BeautifulSoup(response.text, 'lxml').find('table').find_all('td')[1].string
        bash_url = BeautifulSoup(response.text, 'lxml').find('p', class_='btnlinks').find('a', class_='read')['href']
        name_id = str(bash_url)[-6:-1].replace('/', '')
        item['category'] = category
        item['author'] = author
        item['name_id'] = name_id
        return item
    






