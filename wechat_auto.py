# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium import common
from selenium.webdriver.common.keys import Keys
import time
from threading import Thread

curr_mess = ''
def import_handler():
    thr = Thread(target=check_mess)
    thr.start()

def check_mess():
    while(True):
        t = wechat.find_element_by_xpath('//*[@id="chatArea"]/div[2]/div[1]/div[1]/div[14]/div/div/div/div/div/div/div/pre')
        if curr_mess == t.text:
            # continue wait
            pass
        else:
            curr_mess = t.text

        return t.text
wechat = webdriver.Chrome()
wechat.maximize_window()

# Login
def login():
    wechat.get('https://wx2.qq.com/')
    time.sleep(12)
    cwechat()

def getdata(i):
    if i == 0:
        return '小可爱，爱你么么哒！！！！！问我为什么还没睡！'
    if i == 1:
        return '因为这是我程序自动回复的消息呀。现在我的程序还很 简单，不能和你互动，以后我会分析你的句子，给你相应的回复。'
    if i == 2:
        return '不牛逼！不牛逼！哈哈 么么哒！'
    if i == 3:
        return '小仙女！饿了吗？订外卖请吃成猪好吗，么么哒'
    if i == 4:
        return '小可爱，累不累！累的话就偷个懒，么么哒 爱你'
    if i == 5:
        return '小可爱！我突然想起来我的离散数学老师，当他完成一个证明的时候，总是会用乐章终止符代替QED (Quod Erat Demonstrandum:it has been proved) \n 只能说很优雅了。'
    if i == 6:
        return '过去有人曾对我说，“一个人爱上小溪，是因为没有见过大海。”而如今我终于可以说，“我已见过银河，但我仍只爱你一颗星。”（七堇年）'
    if i == 7:
        return '山有木兮木有枝，心悦君兮君不知。（《越人歌》）'
    if i == 8:
        return '小可爱！教你一个单词，你肯定记得住，poem poetry '
    if i == 9:
        return '小可爱！别忘了你还有一个空姐梦！记得多背一些单词，我很清楚的知道，你那点词汇量，这样背单词是不行的，一定要多背！ '
    if i == 10:
        return '小可爱！要想发音准确，就锲而不舍的念音标，跟着念，记得录音，和音标有不一样的地方，记得自己纠正自己，一天只学一个音标都行的！ '
    if i == 11:
        return '小可爱！我要休息了！ 等我八点起床吧~ 晚安！记得晚饭多吃点。 '
    if i == 12:
        return '小可爱！这是最后一条了，其实我是来自过去的我，是不是像穿越了时空一样？ '
    if i == 13:
        return '小可爱！这是最后最后一条了，爱你 么么哒'
    if i == 14:
        return '么么哒！你猜隔多久发一次消息？'
    if i == 15:
        return '爱你！ 答案是8分25秒！'
    if i >= 16 and i<=30:
        return '爱你！ 小可爱 你为什么这么可爱？'
    if i >= 31 :
        return '爱你！ 么么哒！'

def cwechat():
   # for i in range(0,40,1):
   #     data = getdata(i)

       wechat.find_element_by_xpath('//*[@id="editArea"]').send_keys("背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！背单词！现在背单词！")
       # print('messages input %d', i)
       time.sleep(19740)
       wechat.find_element_by_xpath('//*[@id="chatArea"]/div[3]/div[3]/a').click()
       # print('messages sent %d', i)
       # print('sleep 505 secs')
       # time.sleep(505)

def getnewmess():
    t = wechat.find_element_by_xpath('//*[@id="chatArea"]/div[2]/div[1]/div[1]/div[14]/div/div/div/div/div/div/div/pre')
    print(t.text)
    return t.text

def main():
    """
    主函数
    """

    login()
    # import_handler()


if __name__ == '__main__':

    main()

