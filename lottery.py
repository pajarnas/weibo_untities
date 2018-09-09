### for one lottery micro blog
    # 1. find the blog and indetntify
    # 2. like
    # 3. follow
    # 4. comment
    # 5. exit
    # function we need:
    #   1. re to indentify useful information
    #       topic to comment , user to follow, topic to follow
    #   2. follow function (parameters:name, flag)
    #        open another tab
    #        follow user or follow topic
    #        exit
    #   3. comment function(topic)
    #        add topic
    #        comment
    #        exit
import re
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
from pprint import pprint

import time

weibo = webdriver.Chrome()
weibo.maximize_window()
weibo.get('https://www.weibo.com/')
main_win = weibo.current_window_handle
data = '希望中奖！顺便告白我喜欢某位小仙女！'

# Login
def login(user, pasw):
    time.sleep(6)
    # 把用户名填入
    weibo.find_element_by_xpath('//*[@id="loginname"]').send_keys(user)
    # 把密码填入
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input').send_keys(pasw)
    # 点击登录按钮
    weibo.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
    time.sleep(10)
    while True:
        try:
          weibo.find_element_by_xpath('//*[@id="v6_pl_leftnav_group"]/div[2]/div[1]/div[5]/div[1]/a/span[2]')
          break
        except:
          print('wair for 15 secs')
          time.sleep(15)
    while True:
        iweibo()
        if weibo.window_handles.__len__() > 1:
            for i in weibo.window_handles[1:]:
              weibo.switch_to_window(i)
              weibo.close()
        weibo.switch_to_window(main_win)
        print('wair for 2000 secs')
        time.sleep(2000)


def address_filter(links, user_links, topic_links):
    for i in links:
        # if in form of #?# then topic
        regexp_topic = re.compile(r'^(#)(.*)(#)$')
        if regexp_topic.search(i.text):
            topic_links.append({i.text: i})
            print(i.text + 'topic matched')
            continue
        # if in form of @？ then user to follow
        regexp_user = re.compile(r'^(@)(.*)')
        if regexp_user.search(i.text):
            if i.text == '@微博抽奖平台':
                pass
            else:
                user_links.append({i.text:i})
                print(i.text+'user matched')




def iweibo_for_nest():
    pass

def iweibo():
    weibo.get('http://s.weibo.com/')
    weibo.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[2]/div/input').send_keys('微博抽奖平台')
    weibo.find_element_by_xpath('//*[@id="pl_searchHead"]/div[1]/div/div/div[1]/a').click()
    # wait for loading completed
    time.sleep(3)
    # find blog's root div list
    blogs_root_list = weibo.find_elements_by_css_selector(".WB_cardwrap.S_bg2.clearfix")
    time.sleep(3)
    for i in blogs_root_list:
        # if exceptes, not a real blog
        try:
            blog_info = i.find_element_by_xpath("./div[2]/div[1]/dl/div/div[3]/div[1]")
            buttons = i.find_element_by_xpath("./div[2]/div[2]/ul")
        except:
            try:
                blog_info = i.find_element_by_xpath('./ div / div[1] / dl / div / div[3] / div[1]')
                buttons = i.find_element_by_xpath('./div/div[2]/ul')
            except:
                continue
        if check_f_weibo(buttons) == 1:
            continue
        super_topic = []
        user_link = []
        topic_link = []

        owner_addr = {'@'+blog_info.find_element_by_xpath("./a[1]").text:blog_info.find_element_by_xpath("./a[1]")}

        content = blog_info.find_element_by_xpath("./p[@class='comment_txt']")
        # extract links
        links = content.find_elements_by_tag_name('a')
        user_link.append(owner_addr)

        for link in links:

            # check whether the address contains super topic
            try:
                temp = link.find_element_by_css_selector('.W_ficon.ficon_supertopic')
                s_topic = '#'+link.text[2:]+'[超话]#'
                super_topic.append({s_topic:link})
                print('super topic :' + s_topic)
            except common.exceptions.NoSuchElementException:
                print('no super topic')
                continue
            # extract user and topic
        address_filter(links, user_link, topic_link)
        follow(user_link,  super_topic)

        lweibo(buttons)

        fweibo(buttons, user_link, topic_link, super_topic)






def open_tab(a):

    # obtain url of gmail on the home page of Google
    addr = a.get_attribute("href")

    # open new blank tab
    weibo.execute_script("window.open();")

    # switch to the new window which is second in window_handles array
    weibo.switch_to_window(weibo.window_handles[1])

    # open successfully and close
    weibo.get(addr)

def close_tab():
    weibo.close()
    weibo.switch_to_window(main_win)



def follow( user_link,  s_topic_link):
    # do user
    # check empty
    if [] != user_link:
        for i in user_link:
            for j in i.values():
                count = 1
                open_tab(j)
                time.sleep(2)
                while True:
                 try:
                   weibo.find_element_by_xpath('// *[ @ id = "Pl_Official_Headerv6__1"] / div[1] / div / div[2] / div[4] / div / div[1] / a[1]').click()
                   break
                 except:
                     count += 1
                     if count > 3:
                         close_tab()
                         return
                time.sleep(2)
                close_tab()

    # do supertopic
    if [] != s_topic_link:
        for i in s_topic_link:
            for j in i.values():
                open_tab(j)
                time.sleep(2)
                weibo.find_element_by_xpath('//*[@id="Pl_Core_StuffHeader__1"]/div/div[2]/div/div[3]/div/div[2]/a').click()
                time.sleep(2)
                close_tab()


def fweibo(buttons,user_link, topic_link, super_topic):
    content = ''
    for i in user_link:
        for j in i.keys():
            content = content + j + ' '
    for i in topic_link:
        for j in i.keys():
            content = content + j + ' '
    for i in super_topic:
        for j in i.keys():
            content = content + j + ' '
    content = content + data
    print (content)
    c_weibo(buttons)
    print ('Collected!')
    buttons.find_element_by_xpath('./li[2]/a').click()
    time.sleep(5)
    tr = weibo.find_elements_by_class_name('W_layer')
    for i in tr:
        try:
            p = i.find_element_by_xpath('./div/table/tbody/tr/td/div/div[2]/div[2]/div/div[2]/div')
            l = p.find_element_by_tag_name('textarea')
            l.click()
            l.send_keys(content)
            p.find_element_by_xpath('./ div[2] / ul / li / label').click()
            p.find_element_by_xpath('. / p[2] / a / span').click()
            print ('forward successfully')
            time.sleep(2)
            continue
        except:
            print('Searching')


def check_f_weibo(buttons):
    t = buttons.find_element_by_xpath('./li[1]/a').text
    if t == '取消收藏':
        return 1
    else:
        return 0

def c_weibo(buttons):
    buttons.find_element_by_xpath('./li[1]/a').click()

def lweibo(buttons):
    while True:
        try:
            we = buttons.find_element_by_xpath('./li[4]/a')
            if we.get_attribute('title') == '取消赞':
                break
            else:
                we.click()
                break
        except:
            pass



# find comment
# input data
# summit
def main():
    """
    主函数
    """


    user = '13253312354'
    pasw = 'zsq1212'
    data = '我爱莹莹小仙女！！！！！！！！！！！！！！！！！'
    num = int(100)
    print('开始登陆微博')
    login(user, pasw)



if __name__ == '__main__':
    main()
