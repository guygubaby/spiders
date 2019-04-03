import requests


class Tieba:
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    url='https://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'

    def __init__(self,kw,max_pn=100):
        self.kw=kw
        self.max_pn=max_pn

    def init_urls(self):
        return [self.url.format(self.kw,pn) for pn in range(50,self.max_pn+1,50)]

    def get_content(self,url):
        res = requests.get(url=url,headers=self.headers)
        return res.content

    def get_data(self):
        urls=self.init_urls()
        for i,url in enumerate(urls):
            content=self.get_content(url)
            self.save_data(f'{self.kw} - {(i+1)*50}',content)

    @staticmethod
    def save_data(name,content):
        with open(f"./htmls/{name}.html",'wb') as f:
            f.write(content)


if __name__ == '__main__':
    tieba=Tieba('英雄联盟',100)
    tieba.get_data()
    print('ok ：）')