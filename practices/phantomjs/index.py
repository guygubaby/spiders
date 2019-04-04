from selenium import webdriver


# deprecated
class PhantomjsTest:
    url='https://baidu.com'
    driver=webdriver.PhantomJS(executable_path='../../phantomjs/phantomjs')
    driver.set_window_size(1366, 768)

    def __init__(self):
        self.driver.get(self.url)
        title=self.driver.title
        print(title)


if __name__ == '__main__':
    phantomjs=PhantomjsTest()
