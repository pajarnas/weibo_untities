# -*- coding: utf-8 -*-
from selenium import webdriver
import time

weibo = webdriver.Chrome()
weibo.maximize_window()


def login(user, pasw, numb):
    weibo.get('https://www.weibo.com/')
    time.sleep(3)
    # 把用户名填入
    weibo.find_element_by_xpath('//*[@id="loginname"]').send_keys(user)
    # 把密码填入
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pasw)
    # 点击登录按钮
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    time.sleep(6)

    print ('登陆成功')
    delweibo(numb)


def delweibo(numb):
    weibo.find_element_by_xpath('//div[@id="v6_pl_rightmod_myinfo"]/div/div/div[2]/ul/li[3]/a/strong').click()


    for i in range(0, numb):
       try:
           print ('Deleting term %d blog',273-i)
           time.sleep(3)
           # 下拉菜单
           weibo.find_element_by_xpath('//div[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/a/i').click()
          # 点击删除按键
           weibo.find_element_by_xpath(
            '//div[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/a').click()
          # 点击确认删除
           weibo.find_element_by_xpath("//div[@id]/div/p[2]/a[1]/span").click()
       except:
           print('Deleting term %d blog', 273 - i)
           time.sleep(3)
           # 下拉菜单
           weibo.find_element_by_xpath(
               '//div[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/a/i').click()
           # 点击删除按键
           weibo.find_element_by_xpath(
               '//div[@id="Pl_Official_MyProfileFeed__20"]/div/div[2]/div[1]/div[1]/div/div/ul/li[1]/a').click()
           # 点击确认删除
           weibo.find_element_by_xpath("//div[@id]/div/p[2]/a[1]/span").click()
    weibo.close()
    print ('微博已经清空')


user = '17326833696'
pasw = 'zsq1212'
numb = 273
print ('开始登陆微博')
login(user, pasw, numb)