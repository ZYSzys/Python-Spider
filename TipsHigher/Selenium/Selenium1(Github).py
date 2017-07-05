#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#账号密码:
usr_name = '..........@...com'
pass_word = '..........'

#浏览器驱动:
driver = webdriver.Chrome()
driver.get('https://github.com/login')

#寻找'class = login'输入帐号
account = driver.find_element_by_name('login')
account.clear()
account.send_keys(usr_name)

#寻找'class = password'输入密码
password = driver.find_element_by_name('password')
password.clear()
password.send_keys(pass_word)

account.send_keys(Keys.RETURN)
time.sleep(5)

print driver.page_source
driver.close()







