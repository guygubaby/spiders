from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#WebDriverWait库，负责循环等待
from selenium.webdriver.support.ui import WebDriverWait
#expected_conditions类，负责条件触发
from selenium.webdriver.support import expected_conditions as EC
import time


# 无界面的chrome
class HeadlessChrome:
    url='https://baidu.com'
    options=Options()
    options.add_argument('-headless')

    driver=webdriver.Chrome(executable_path='../../chrome_driver/chromedriver',options=options)

    def __init__(self):
        print(f'loading {self.url} ...')
        self.driver.get(self.url)
        print(self.driver.title)
        print('load complete :) ')
        self.driver.save_screenshot('baidu.png')

    def search_sth(self,search_str):
        kw_input=self.driver.find_element_by_id('kw')
        kw_input.clear()
        kw_input.send_keys(search_str)

        search_btn=self.driver.find_element_by_id('su')
        search_btn.click()

        print(f'searching {search_str} ...')
        time.sleep(3)

        js_str='''
            const suEl=document.getElementById('su');
            suEl.style.backgroundColor='red';
        '''
        self.driver.execute_script(js_str)

        self.driver.save_screenshot(f'search_{search_str}.png')
        # self.driver.close() # Close the current window, quitting the browser if it's the last window currently open.
        self.driver.quit() # Quits this driver, closing every associated window.
        print('search complete : ) ，go to current folder to see the screen shot')


if __name__ == '__main__':
    headless_chrome=HeadlessChrome()
    search_str=input('please input something you want to search : ')
    headless_chrome.search_sth(search_str)
