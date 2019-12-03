#!/usr/bin/env python
# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
webd = webdriver.Chrome()
webd.implicitly_wait(30)
webd.get("http://test.oa.xchw.online/")
webd.implicitly_wait(10)
webd.maximize_window()
webd.find_element_by_id('username').send_keys('admin')
webd.find_element_by_id('password').send_keys('1')
#webd.find_element_by_css_selector('.ant-form-item-children').send_keys(Keys.ENTER)
webd.find_element_by_css_selector('[type="submit"]').click()
#webd.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/div/div/div[3]/div/div[5]/div/div/span').click()
#webd.find_element_by_class_name('ant-form-item-children').click()
webd.implicitly_wait(30)
text = webd.find_element_by_xpath('//*[@id="root"]/div/div/section/aside/div/div/a/h1').text
if text=='办公系统':
    print('登录成功')
webd.find_element_by_xpath('//a[@href="#/user_book"]').click()
webd.find_element_by_xpath('//a[@href="#/file"]').click()

#webd.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/form/div/div/div[3]/div/div[5]/div/div/span').click()
#webd.implicitly_wait(5)
