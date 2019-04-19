from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
import time
import datetime
from os import mkdir,getcwd,path
import random


class Inke:
    url='http://inke8888.mikecrm.com/rM3ui9G'
    options=Options()
    mobileEmulation={
        'deviceMetrics':{ "width": 375, "height": 667, "pixelRatio": 3.0 },
        'userAgent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'}
    # options.add_argument('--headless')
    options.add_argument('window-size=380,680')
    options.add_argument('--disable-gpu')
    options.add_experimental_option('mobileEmulation',mobileEmulation)
    pwd=getcwd()
    try:
        driver=webdriver.Chrome(options=options,executable_path=path.join(pwd,'chrome_driver/linux'))
    except Exception as e:
        print('chrome driver error : ',e)
        driver=webdriver.Chrome(options=options,executable_path=path.join(pwd,'chrome_driver/mac'))
    fbc_selections={
        'normal':'200758045',
        'refine':'200758046'
    }
    level_selections={
        'a':'200758094',
        'b':'200758094',
        'c':'200758096'
    }
    time_value_list=[]

    random_num=random.randint(0,1000)

    def __init__(self,mode='normal',id=123456,name='比目鱼',level='a'):
        self.driver.get(self.url)
        self.mode=mode
        self.id=id
        self.name=name
        self.level=level

        self.folder_name='./imgs/{}_{}'.format(self.name,self.id)

    def init_time_list(self):
        # 0 : 00:00-00:30  1 : 00:30-01:00
        self.time_value_list=[(200758047+i) for i in range(47)]

    def do_submit_form(self):
        self.init_time_list()
        try:
            mkdir('imgs')
            mkdir(self.folder_name)
        except:
            pass

        # wait=WebDriverWait(self.driver,10)
        # 选择正常推荐或者精细化推荐
        selection=self.driver.find_element_by_class_name('fbc_innerSelect')
        selection=Select(selection)
        selection.select_by_value(self.fbc_selections.get(self.mode))
        time.sleep(1)

        # 推荐主播映客ID*
        input_id=self.driver.find_element_by_xpath('//*[@id="200931198"]/div[2]/div/div/input')
        input_id.clear()
        input_id.send_keys(self.id)

        # 公会名称（例如比目鱼）*
        input_guild_name=self.driver.find_element_by_xpath('//*[@id="200931199"]/div[2]/div/div/input')
        input_guild_name.clear()
        input_guild_name.send_keys(self.name)

        # 申请推荐日期（正常推荐）*
        input_date=self.driver.find_element_by_xpath('//*[@id="200931200"]/div/div[1]/div/div')
        input_date.click()
        # show_dialog_js="document.getElementsByClassName('fbi_input')[2].click()"
        # self.driver.execute_script(show_dialog_js)
        # self.driver.save_screenshot('choose_date.png')

        date_wrapper=self.driver.find_element_by_class_name('calendar_bWeekList')
        days=date_wrapper.find_elements_by_class_name('current-month')
        today=datetime.datetime.now().day
        for day in days:
            if day.find_element_by_tag_name('a').text == str(today):
                day.click()
                # self.driver.save_screenshot('ok.png')
                break

        # 申请推荐时间（正常推荐）*
        selection_time=Select(self.driver.find_element_by_xpath('//*[@id="200931247"]/div/div/select'))
        selection_time.select_by_value(str(self.time_value_list[0]))

        # 主播评级（正常推荐）*
        selection_lever=Select(self.driver.find_element_by_xpath('//*[@id="200931867"]/div/div/select'))
        selection_lever.select_by_value(self.level_selections.get(self.level))

        js_before_submit='window.scroll(0,390)'
        self.driver.execute_script(js_before_submit)
        self.driver.save_screenshot('{}/before_submit_{}.png'.format(self.folder_name,self.random_num))

        # submit
        # submit_js="document.getElementsByClassName('fb_submitBtn')[0].click()"
        # self.driver.execute_script(submit_js)
        submit_btn=self.driver.find_element_by_xpath('//*[@id="form_submit"]')
        submit_btn.click()
        time.sleep(3)

        js = 'window.scroll(0,1000)'
        self.driver.execute_script(js)

        self.driver.save_screenshot('{}/after_submit_{}.png'.format(self.folder_name,self.random_num))

    def close_driver(self):
        self.driver.close()


if __name__ == '__main__':
    inke=Inke(mode='normal',id=123456,name='比目鱼',level='a')

    time.sleep(3)
    try:
        inke.do_submit_form()
    except Exception as e:
        print('some error happened : {}'.format(e))
    finally:
        inke.close_driver()
