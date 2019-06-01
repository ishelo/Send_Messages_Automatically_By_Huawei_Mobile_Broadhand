# -*- coding:utf-8 -*-
import time
from splinter import Browser
import xlrd

def datainput():    #导入数据
    path = 'sms.xlsx'
    rb = xlrd.open_workbook(path)
    data_sheet = rb.sheets()[0]
    rowNum = data_sheet.nrows
    pop_Num = []
    pop_Text = []
    for i in range(1, rowNum):
        pop_Num.append(int(data_sheet.cell_value(i, 0)))
        pop_Text.append(data_sheet.cell_value(i, 1))
    print("手机号和内容导入成功")
    # print(pop_Num)
    # print(pop_Text)
    return pop_Num, pop_Text

def sms(send_Num, send_Text):
    url = 'http://192.168.8.1/html/home.html'
    browser = Browser()
    browser.visit(url)    # login Huawei telenor websize
    time.sleep(1)    # wait web element loading
    browser.find_by_id('logout_span').click()    # click the button of login
    browser.find_by_id('username').fill('admin')    # fill in account and password
    browser.find_by_id('password').fill('zxcvbnm123')
    browser.find_by_id('pop_login').click()    # click the button of login
    time.sleep(1)
    browser.find_by_id('sms').click()  # click the button of sms
    time.sleep(1)
    browser.find_by_id('message').click()    # click the button of message
    time.sleep(1)
    browser.find_by_id('recipients_number').fill(send_Num)  # fill in recipients_number and message_content
    browser.find_by_id('message_content').fill(send_Text)
    browser.find_by_id('pop_send').click()  # click the button of send
    time.sleep(5)
    browser.find_by_id('pop_OK').click()  # click the button of OK
    browser.quit()  # close the window of brower

if __name__ == '__main__':
    pop_Num, pop_Text = datainput()
    n = int(len(pop_Num))
    for i in range(n):
        send_Num = pop_Num[i]
        send_Text = pop_Text[i]
        sms(send_Num, send_Text)
        print('''收信人：{}
内容：{}
发送成功'''.format(send_Num, send_Text))