import requests
from bs4 import BeautifulSoup


class Douban:
    url = 'https://accounts.douban.com/j/mobile/login/basic'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Referer':'https://accounts.douban.com/passport/login_popup?login_source=anony'
    }
    session=requests.session()
    data={
        'ck':'',
        'remember': 'false',
        'ticket':''
    }

    def __init__(self):
        self.data['name']=input('phone number here : ')
        self.data['password']=input('password then : ')

    def login(self):
        login_res = self.session.post(url=self.url, headers=self.headers, data=self.data).json()
        login_status=login_res['status']
        if login_status=='success':
            self.account_info=login_res['payload']['account_info']
            self.id=self.account_info['id']
            print(f"login success , your name is {self.account_info['name']}")
        else:
            print(f"login failed with reasons here {login_res['description']}")

    def get_user_statuses(self):
        url=f'https://www.douban.com/people/{self.id}/statuses'
        self.headers['Referer']=url
        statuses_res=self.session.get(url=url,headers=self.headers).text
        soup=BeautifulSoup(statuses_res,'html.parser')
        new_status=soup.find_all('div',class_='new-status')
        movie_item={}
        movies=[]
        for status in new_status:
            title=status.find('a',class_='media')['title']
            movie_item['name']=title
            movies.append(movie_item)
        return movies


if __name__ == '__main__':
    douban=Douban()
    douban.login()
    movies=douban.get_user_statuses()
    for movie in movies:
        print(movie.get('name'))
