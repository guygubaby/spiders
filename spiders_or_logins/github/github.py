import requests
from bs4 import BeautifulSoup

'''
Your browser did something unexpected. Please contact us if the problem persists.
I don't know what's wrong , 😁 ， if anyone has a idea please contact me with 1907004005@qq.com
'''

class Github:
    def __init__(self):
        base_url = 'https://github.com/'
        # 登陆 url
        self.login_url = base_url + 'login'
        # 提交表单的 api
        self.post_url = base_url + 'session'
        # 个人资料页面的 url
        self.logined_url = base_url + 'settings/profile'
        # 构造一个会话对象
        self.session = requests.Session()

        self.session.headers={
            'Referer':'https://github.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
            'Host':'github.com'
        }

    def get_token(self):
        login_res=self.session.get(url=self.login_url)
        soup=BeautifulSoup(login_res.text,'html.parser')
        token=soup.find('input',attrs={'name':'authenticity_token'})
        return token['value'].strip()

    def login(self,name,pwd):
        token=self.get_token()
        post_data = {
            'commit': 'Sign in',
            'utf8': '✓',
            'authenticity_token': token,
            'login': name,
            'password': pwd
        }
        res=self.session.post(url=self.post_url,data=post_data)
        code=res.status_code
        info=BeautifulSoup(res.text,'html.parser').find('p').string
        if code==200:
            print('login success :) ')
        else:
            print('login failed :( ')
            print(info)


if __name__ == '__main__':
    name = input('user name : ')
    pwd = input('password : ')
    github=Github()
    github.login(name,pwd)