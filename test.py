#-*- coding: utf-8 -*-  

from splinter import Browser
# from selenium import webdriver

# driver = webdriver.Chrome("/Users/ckiddo/Downloads/chromedriver")
# driver.get('http://www.google.com')

executable_path = {'executable_path':"/Users/ckiddo/Downloads/chromedriver"}

with Browser('chrome',**executable_path) as browser:
    # Visit URL
    url = "http://www.google.com"
    browser.visit(url)
    browser.fill('q', 'splinter - python acceptance testing for web applications')
    # Find and click the 'search' button

    button = browser.find_by_name('Google搜索')
    # Interact with elements
    button.click()
    if browser.is_text_present('splinter.readthedocs.io'):
        print("Yes, the official website was found!")
    else:
        print("No, it wasn't found... We need to improve our SEO techniques")