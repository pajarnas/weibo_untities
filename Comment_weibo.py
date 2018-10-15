# TODO
# 转发抽奖微博
# 识别 抽奖的微博 打开新界面跳转 点赞关注转发评论 识别需要关注的其他人 打开新界面关注 退出 退出
# 新界面跳转关注关闭函数
# 新界面微博 关闭函数
# 主函数等待 所有关闭继续下一条
# 抽奖10个后 刷新 等待20分钟
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import time

weibo = webdriver.Chrome()
weibo.maximize_window()

# Login
def login(user, pasw, num, data):
    weibo.get('https://www.weibo.com/')
    time.sleep(6)
    # 把用户名填入
    weibo.find_element_by_xpath('//*[@id="loginname"]').send_keys(user)
    # 把密码填入
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pasw)
    # 点击登录按钮
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    time.sleep(12)

    print ('登陆成功')
    weibo.find_element_by_xpath('//*[@id="v6_pl_leftnav_group"]/div[2]/div[1]/div[5]/div[1]/a/span[2]').click()
    cweibo(num,data)

def cweibo(num,data):
    # goto hot
    j = 0


    for i in range(1, num):
        try:
            time.sleep(3)
            print (i)
            i = str(i)
            weibo.find_element_by_xpath('//*[ @ id = "Pl_Core_NewMixFeed__3"] / div / div[2] / div['+i+'] / div[2] / div / ul / li[3] / a / span / span / span / em[2]').click()
            time.sleep(2)
            weibo.find_element_by_xpath('//*[@id="Pl_Core_NewMixFeed__3"]/div/div[2]/div['+i+']/div[3]/div/div/div[2]/div[2]/div[1]/textarea').send_keys(data)
            time.sleep(2)
            weibo.find_element_by_xpath(' // *[ @ id = "Pl_Core_NewMixFeed__3"] / div / div[2] /div['+i+']/ div[3] / div / div / div[2] / div[2] / div[2] / div[1] / a').click()
            if int(i)%5 == 0:
                time.sleep(10)
                print ('scroll down')
                html = weibo.find_element_by_tag_name('html')
                html.send_keys(Keys.END)
        except common.exceptions.NoSuchElementException:
            print('Deleting term %d blog')
            j=j+1
            if j >9:
                weibo.refresh()
                cweibo(num - int(i), data)
        except common.exceptions.WebDriverException:
            print ('network error')
            weibo.refresh()
            cweibo(num - int(i),data)

    print('微博已经评论')


# find comment
# input data
# summit
def main():
    """
    主函数
    """

    while True:
        user = 'your id'
        pasw = 'your pass'
        data = 'Three fake Koreans,韩杂 @低调莫忧 @下雪了你知道吗 @onemorelookandbang  kneel to your grandpapa of LPL '
        num = int(100)
        print('开始登陆微博')
        login(user, pasw,num, data)



if __name__ == '__main__':

    main()

