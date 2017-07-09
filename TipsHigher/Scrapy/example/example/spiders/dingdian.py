import re
import scrapy
from bs4 import BeautifulSoup
import scrapy.http import Request
from example.items import DingdianItem

class Myspider(scrapy.Spider):

