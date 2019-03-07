# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import time

bili = webdriver.Chrome()
bili.maximize_window()

def next2():
    s = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[8]')
    s.click()
    time.sleep(1)

bili.get('https://live.bilibili.com/6')
time.sleep(8)
z = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[3]')
z.click()
for i in range(1, 29):
    next2()

