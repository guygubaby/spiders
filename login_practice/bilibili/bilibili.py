from selenium import webdriver
from selenium.webdriver import ActionChains
import time


class Bilibili:
    url='https://passport.bilibili.com/login'
    driver=webdriver.Chrome(executable_path='../../chrome_driver/chromedriver')

    def __init__(self,name='1',pwd='1'):
        self.driver.get(self.url)
        self.name=name
        self.pwd=pwd

    def fill_form(self):
        user_name_input=self.driver.find_element_by_xpath('//*[@id="login-username"]')
        user_name_input.clear()
        user_name_input.send_keys(self.name)

        pwd_input=self.driver.find_element_by_xpath('//*[@id="login-passwd"]')
        pwd_input.clear()
        pwd_input.send_keys(self.pwd)

        time.sleep(3)

    def move_slide_knob(self): #移动滑块
        toggle_class_js="document.querySelector('.gt_widget').classList.toggle('gt_show')"
        self.driver.execute_script(toggle_class_js)

        block_wrapper=self.driver.find_element_by_class_name('gt_hide')
        # block_wrapper

        slide_btn=self.driver.find_element_by_xpath('//*[@id="gc-box"]/div/div[3]/div[2]')
        slide_action=ActionChains(self.driver)
        slide_action.click_and_hold(slide_btn).perform()

        slide_action.reset_actions()

        slide_action.move_by_offset(110,0).perform()

        time.sleep(3)

        self.driver.execute_script(toggle_class_js)
        slide_action.release(slide_btn).perform()



    def close_browser(self):
        self.driver.close()


if __name__ == '__main__':
    bilibili=Bilibili()

    bilibili.fill_form()
    bilibili.move_slide_knob()


    # bilibili.close_browser()
