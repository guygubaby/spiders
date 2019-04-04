#!/usr/bin/env python3
from selenium import webdriver
import time


class Email163:
    url='http://mail.163.com/'
    chrome_driver_path='../../chrome_driver/chromedriver'

    def __init__(self):
        self.account_num=input('input your email : ')
        if '@163' in self.account_num:
            self.account_num=self.account_num.split('@163')[0]
        self.passwd_str=input('input your password : ')
        # start browser
        self.browser = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.browser.get(self.url)
        time.sleep(5)
        iframe=self.browser.find_element_by_css_selector("iframe[id^='x-URS-iframe']")
        self.browser.switch_to.frame(iframe)

    def login(self):
        acount=self.browser.find_element_by_name('email')
        acount.clear()
        acount.send_keys(self.account_num)
        passwd=self.browser.find_element_by_name('password')
        passwd.clear()
        passwd.send_keys(self.passwd_str)
        login_btn=self.browser.find_element_by_id('dologin')
        login_btn.click()
        time.sleep(5)
        cookie=self.browser.get_cookies()[0]
        return cookie


if __name__ == '__main__':
    email=Email163()
    cookie=email.login()
    print(cookie)
    if cookie['value']=='':
        print('login failed , please try again')
        email.browser.close()
    else:
        print('login success')
        time.sleep(10)
        email.browser.close()
