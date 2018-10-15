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

bili = webdriver.Chrome()
bili.maximize_window()

# Login
def login(user, pasw, data):
    bili.get('https://passport.bilibili.com/login')

    # 把用户名填入
    bili.find_element_by_xpath('//*[@id="login-username"]').send_keys(user)
    # 把密码填入
    bili.find_element_by_xpath('//*[@id="login-passwd"]').send_keys(pasw)
    # 点击登录按钮
    bili.find_element_by_xpath('//*[@id="login-app"]/div/div[2]/div[3]/div[3]/div/div/ul/li[5]/a[1]').click()
    time.sleep(15)
    print('登陆成功')
    bili.get('https://www.bilibili.com/blackboard/activity-s8cheer-pc.html?spm_id_from=888.2805.support-mount-point.2')
    time.sleep(10)
    z = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[3]')
    z.click()
    for i in range(1, 29):
        next2()

    cbilibili(data)


def cbilibili(data):
    # goto hot
    j = 0
    for k in range(1, 50):
        comms = bili.find_elements_by_css_selector(".list-item.reply-wrap")
        time.sleep(3)
        for i in range(1,18,2):
            bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[4]/div['+str(i)+']/div[2]/div[2]/span[3]').click()
            bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[4]/div[' + str(i) + ']/div[2]/div[2]/span[5]').click()
            time.sleep(2)
            bili.find_element_by_xpath(
                '//*[@id="bili-comment-mount-point"]/div/div[4]/div[' + str(i) + ']/ div[2] / div[5] / div[2] / textarea').send_keys(data)
            bili.find_element_by_xpath(
                '//*[@id="bili-comment-mount-point"]/div/div[4]/div[' + str(i) + ']/ div[2] / div[5] / div[2] / button').click()
            print('已经评论')
            time.sleep(5)
            j += 1
            if j == 4:
                time.sleep(300)
                j = 0
        next2()

def next2():
    s = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[8]')
    s.click()
    time.sleep(1)

def next():
    # bili-comment-mount-point > div > div.comment-header.clearfix > div.header-page.paging-box > a.next

    try:
        s = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[5]')
        if s.text != '下一页':
            raise Exception
    except:
        s = bili.find_element_by_xpath('//*[@id="bili-comment-mount-point"]/div/div[2]/div[2]/a[8]')
    s.click()

def main():
    """
    主函数
    """

    while True:
        user = '13253312354'
        pasw = 'zsq1212,,,'
        data = '能给我写的给LPL助威的文章点个喜欢吗，cv1320484， 谢谢！！'
        print('开始登陆bilibili')
        login(user, pasw, data)



if __name__ == '__main__':

    main()

