from PIL import Image
import requests
from bs4 import BeautifulSoup
import http.cookiejar as cookielib
from os import remove


class Douban:
    url = 'https://accounts.douban.com/login'
    datas = {'source': 'index_nav',
             'remember': 'on'}
    headers = {'Host': 'www.douban.com',
               'Referer': 'https://www.douban.com/',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:55.0) Gecko/20100101 Firefox/55.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate, br'}

    def __init__(self):
        self.session=requests.session()
        self.session.cookies=cookielib.LWPCookieJar(filename='cookies')
        try:
            self.session.cookies.load(ignore_discard=True)
        except:
            print('cookies load faild login please')
            self.datas['form_email']=input('please input your phone')
            self.datas['form_password']=input('please input your password')

    def get_capcha(self):
        '''
        获取验证码及其ID
        :return:
        '''

        res=requests.post(self.url,data=self.datas,headers=self.headers)
        html_str=res.text
        print(html_str)
        # soup=BeautifulSoup(html_str,'html.parser')
        # 利用bs4获得验证码图片地址


if __name__ == '__main__':
    douban=Douban()
    douban.get_capcha()

