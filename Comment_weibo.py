# -*- coding: utf-8 -*-
# TODO
# 转发抽奖微博
# 识别 抽奖的微博 打开新界面跳转 点赞关注转发评论 识别需要关注的其他人 打开新界面关注 退出 退出
# 新界面跳转关注关闭函数
# 新界面微博 关闭函数
# 主函数等待 所有关闭继续下一条
# 抽奖10个后 刷新 等待20分钟
# -*- coding: utf-8 -*-
import random
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import time

weibo = webdriver.Chrome()
weibo.maximize_window()

# Login
def login(user, pasw, num):
    weibo.get('https://www.weibo.com/')
    time.sleep(6)
    # 把用户名填入
    weibo.find_element_by_xpath('//*[@id="loginname"]').send_keys(user)
    # 把密码填入
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pasw)
    # 点击登录按钮
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    time.sleep(40)

    print ('登陆成功')
    weibo.get("https://www.weibo.com/p/1008081b39e3456bcfe62618b5703a0395c6ce/super_index")
    publish_weibo()

def cweibo():
    # goto hot
    l = [u"我男朋友新开的公司再收新人主播，客服24小时在线，有兴趣加上聊聊被，我空间置顶微博~~",
         u"我男朋友开了一个公司，让我帮忙宣传QAQ，有想当主播的小姐姐吗，戳我看置顶",
         u"男朋友让我帮他宣传下他的公司，有没有相当主播的小姐姐，点我头像置顶微博。。谢谢",
         u"男友的主播公司正在招聘主播，有人想要看看吗，在我主页里置顶",
         u"帮男票发一下，有人当主播吗？我男票新开的公司正在找主播，看我首页置顶。。",
         u"男友的新公司在招主播，有没有小姐姐小哥哥愿意看一眼？么么哒，谢谢",
         u"有没有有才艺的小哥哥小姐姐想业余做个主播，我男友刚开的公司再找主播，有没有愿意看一下的，我置顶微博",
         u"你才艺这么好，要不要看一下我的置顶微博，我男友新开的公司在招主播~~",
         u"小姐姐，小哥哥有没有想做主播的，我男友新开的公司在找主播，待遇很好的，要不要找客服问一下，我置顶微博有联系方式~",
         u"有没有想做业余主播的，我男盆友开了公司，需要主播，有没有要做主播的可以联系他公司客服，24小时在线，在我的置顶微博"]
    for k in range(1, 50):

        cards = weibo.find_elements_by_css_selector(".card-wrap")
        j=0
        for i in cards:
            j+=1
            try:
               blog_info = i.find_element_by_xpath("./div[1]/div[2]/ul/li[3]")
               a = blog_info.text
               if a[0:2] == '评论':
                   print(a[0:2])
                   blog_info.click()
                   time.sleep(4)
                   data1= l[random.randint(0,9)]
                   data = '#美妆[超话]#' + data1 + ' 24小时在线收主播'
                   i.find_element_by_xpath("./div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/textarea").send_keys(data)
                   i.find_element_by_xpath('./div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/span/label/input').click()
                   i.find_element_by_xpath('./div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/a').click()
                   time.sleep(15)
            except:

                    for i in range(8,17,1):
                        try:
                           weibo.find_element_by_xpath('/html/body/div['+str(i)+']/div[2]/div/div/a').click()
                        except:
                            pass

                    if j > 15:
                      try:
                        a=weibo.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[2]/div/a')
                        if a.text == '下一页':

                            a.click()
                        else:
                            a=weibo.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[2]/div/a[2]')
                            a.click()
                        print('翻页')
                        break
                      except:
                          weibo.refresh()

    print('微博已经评论')
    time.sleep(20)

def publish_weibo():
    # goto hot
    l = [u"我男朋友新开的公司再收新人主播，客服24小时在线，有兴趣加上聊聊被，我空间置顶微博~~",
         u"我男朋友开了一个公司，让我帮忙宣传QAQ，有想当主播的小姐姐吗，戳我看置顶",
         u"男朋友让我帮他宣传下他的公司，有没有相当主播的小姐姐，点我头像置顶微博。。谢谢",
         u"男友的主播公司正在招聘主播，有人想要看看吗，在我主页里置顶",
         u"帮男票发一下，有人当主播吗？我男票新开的公司正在找主播，看我首页置顶。。",
         u"男友的新公司在招主播，有没有小姐姐小哥哥愿意看一眼？么么哒，谢谢",
         u"有没有有才艺的小哥哥小姐姐想业余做个主播，我男友刚开的公司再找主播，有没有愿意看一下的，我置顶微博",
         u"你才艺这么好，要不要看一下我的置顶微博，我男友新开的公司在招主播~~",
         u"小姐姐，小哥哥有没有想做主播的，我男友新开的公司在找主播，待遇很好的，要不要找客服问一下，我置顶微博有联系方式~",
         u"有没有想做业余主播的，我男盆友开了公司，需要主播，有没有要做主播的可以联系他公司客服，24小时在线，在我的置顶微博"]
    for k in range(1, 600):

        try:
               time.sleep(4)
               data1= l[random.randint(0,9)]
               data = '#美妆[超话]#' + data1 + ' 24小时在线收主播'
               weibo.find_element_by_xpath('//*[@id="Pl_Core_PublishV6__287"]/div/div/div/div/div[2]/div[2]/div[1]/textarea').click()
               weibo.find_element_by_xpath('//*[@id="Pl_Core_PublishV6__287"]/div/div/div/div/div[2]/div[2]/div[1]/textarea').send_keys(data)
               weibo.find_element_by_xpath('//*[@id="Pl_Core_PublishV6__287"]/div/div/div/div/div[2]/div[2]/div[2]/div[1]/a').click()
               time.sleep(random.randint(85,105))
        except:
                weibo.refresh()

    print('微博已经评论')
    time.sleep(20)

# find comment
# input data
# summit
def main():
    """
    主函数
    """
    i = 0
    while True:

        user = 'saigezhang17@gmail.com'
        pasw = 'zsq1212'

        num = int(100)
        print('开始登陆微博')
        login(user, pasw,num)
        time.sleep(6)



if __name__ == '__main__':

    main()

