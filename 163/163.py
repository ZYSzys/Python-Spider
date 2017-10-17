#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = 'ZYSzys'

import random
from selenium import webdriver
import time
import selenium.webdriver.support.ui as ui
import traceback

def CatchPlaylist(url):
	driver = webdriver.PhantomJS()
	driver.get(url)
	driver.switch_to_frame('g_iframe')
	try:
		wait = ui.WebDriverWait(driver, 10)
		wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="m-cvrlst f-cb"]'))
		urls = driver.find_elements_by_xpath('//*[@class="m-cvrlst f-cb"]/li/div/a')
		favorite_url = urls[0].get_attribute("href")
	except Exception:
		print traceback.print_exc()
	finally:
		driver.quit()
	return favorite_url

def CatchSongs(url_id, url):
	user = url_id.split('=')[-1].strip()
	print user+': '

	driver = webdriver.PhantomJS()
	driver.get(url)
	driver.switch_to_frame('g_iframe')
	#print driver.page_source
	try:
		wait = ui.WebDriverWait(driver, 10)
		wait.until(lambda driver: driver.find_element_by_xpath('//*[@class="j-flag"]'))
		song_key = 1
		try:
			while song_key <= 50:
				songs = driver.find_elements_by_xpath('//*[@class="j-flag"]/table/tbody/tr[%s]'%song_key)
				for i in songs[0].text.strip().split('\n'):
					print i.encode('utf-8'),
				song_key += 1
				print '\n'

		except Exception:
			print 'No more music'
			traceback.print_exc()
	except Exception:
		traceback.print_exc()
	finally:
		driver.quit()

if __name__ == '__main__':
	for url in ['http://music.163.com/#/user/home?id=339449788']:
		time.sleep(random.randint(2, 4))
		url_playlist = CatchPlaylist(url)
		
		time.sleep(random.randint(1, 2))
		CatchSongs(url, url_playlist)

