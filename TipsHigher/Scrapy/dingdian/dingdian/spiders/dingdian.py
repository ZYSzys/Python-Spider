import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from ..items import DingdianItem

class Myspider(scrapy.Spider):
	name = 'dingdian'
	allowed_domains = ['23wx.cc']
	bash_url = 'http://www.23wx.cc/class/'
	bashurl = '.html'

	def start_requests(self):
		for i in range(1, 11):
			url = self.bash_url + str(i) + '_1' + self.bashurl
			yield Request(url, self.parse)
		yield Request('http://www.23wx.cc/quanben/1', self.parse)

	def parse(self, response):
		print response.text