# ### for one lottery micro blog
#     1. find the blog and indetntify
#     2. like
#     3. follow
#     4. comment
#     5. exit
#     function we need:
#       1. re to indentify useful information
#           topic to comment , user to follow, topic to follow
#       2. follow function (parameters:name, flag)
#            open another tab
#            follow user or follow topic
#            exit
#       3. comment function(topic)
# #            add topic
# #            comment
# #            exit
import re
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
from pprint import pprint

import time

weibo = webdriver.Chrome()
weibo.maximize_window()


# Login
def login(user, pasw, num, data,message):
    weibo.get('https://www.weibo.com/')
    time.sleep(6)
    # 把用户名填入
    weibo.find_element_by_xpath('//*[@id="loginname"]').send_keys(user)
    # 把密码填入
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pasw)
    # 点击登录按钮
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    weibo.implicitly_wait(10)
    try:
      weibo.get('http://s.weibo.com/')
      weibo.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[2]/div/input').send_keys(message)
      weibo.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[1]/a').click()
    except:
        print('wair for 15 secs')
        weibo.implicitly_wait(15)
        weibo.get('http://s.weibo.com/')
        weibo.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[2]/div/input').send_keys(message)
        weibo.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[1]/a').click()
    iweibo()

def iweibo():
        time.sleep(3)
        blogs = weibo.find_elements_by_css_selector(".WB_cardwrap.S_bg2.clearfix")
        blogs2 = weibo.find_elements_by_xpath("//*[@class='WB_cardwrap S_bg2 clearfix']")
        time.sleep(3)
        for i in blogs:
            # all_children_by_xpath = i.find_element_by_xpath('.//*[@class="feed_content wbcon"]')
            try:
               info = i.find_element_by_css_selector(".feed_content.wbcon")
            except common.exceptions.NoSuchElementException:
                continue
            follow_oner = info.find_element_by_xpath("./a[1]")
            content = info.find_element_by_xpath("./p[@class='comment_txt']")
            links = content.find_elements_by_tag_name('a')
        #         <a href="//huati.weibo.com/k/%E5%BE%90%E7%A7%89%E9%BE%99" suda-data="key=tblog_search_weibo&amp;value=weibo_nologin_topic" target="_blank"><i class="W_ficon ficon_supertopic"></i> 徐秉龙</a>
        # <a class="W_texta W_fb" nick-name="赵梦玥UU" href="//weibo.com/youcharenee?refer_flag=1001030103_" target="_blank" title="赵梦玥UU" suda-data="key=tblog_search_weibo&amp;value=weibo_h_1_name">
		# 赵梦玥UU	    </a>
            # div2 = i.find_element_by_xpath()
            # print(div2)
            # for j in all_children_by_xpath :
            #     attrs = weibo.execute_script('var items = {}; for (index = 0; index < arguments[0].attributes.length; ++index) { items[arguments[0].attributes[index].name] = arguments[0].attributes[index].value }; return items;', j)
            #     pprint (attrs)
            #     print ('nothing')

        print('all done')
        time.sleep(3)

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
        user = '13253312354'
        pasw = 'zsq1212'
        data = '我爱莹莹小仙女！！！！！！！！！！！！！！！！！'
        num = int(100)
        print('开始登陆微博')
        login(user, pasw,num, data,message='微博抽奖平台')



if __name__ == '__main__':
    main()
