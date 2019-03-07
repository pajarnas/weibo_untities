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

tieba = webdriver.Edge()
tieba.maximize_window()

# Login
def login( data):
    tieba.get('http://dq.tieba.com/f?kw=%E6%8A%97%E5%8E%8B&ie=utf-8')
    tieba.find_element_by_xpath('//*[@id="com_userbar"]/ul/li[4]/div/a').click()
    time.sleep(1500)
    # # 把用户名填入
    # bili.find_element_by_xpath('//*[@id="login-username"]').send_keys(user)
    # # 把密码填入
    # bili.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(pasw)
    # # 点击登录按钮
    # bili.find_element_by_xpath('//*[@id="login-app"]/div/div[2]/div[3]/div[3]/div/div/ul/li[5]/a[1]').click()
    # time.sleep(15)
    # print('登陆成功')
    # bili.get('https://www.bilibili.com/blackboard/activity-s8cheer-pc.html?spm_id_from=888.2805.support-mount-point.2')
    # time.sleep(10)
    # z = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[3]')
    # z.click()
    # for i in range(1, 29):
    #     next2()

    ctieba(data)


def ctieba(data):
    pass

def next():
    pass

def main():
    """
    主函数
    """

    while True:
        data = '你说是就是吧'
        print('开始登陆bilibili')
        login( data)



if __name__ == '__main__':

    main()

