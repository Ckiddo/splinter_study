#-*- coding: utf-8 -*-  
import time
from splinter.browser import Browser

executable_path = {'executable_path':"/Users/ckiddo/Downloads/chromedriver"}

with Browser('chrome',**executable_path) as browser:
	url = "http://www.zhihu.com/#signin"
	browser.visit(url)
	#button = browser.find_by_value("使用密码登录")
	#button.click()
	time.sleep(600)
	browser.fill("account","13661141240")
	browser.fill("password","heimeiGUI123")
	button = browser.find_by_value(u"登录")[1]
	
	button.click()

	print "clicked"
	while True:
		pass
	
	


