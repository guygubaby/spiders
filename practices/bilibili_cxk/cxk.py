import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient


class CXK:
    cxk_db=MongoClient(host='127.0.0.1',port=27017).my_db.cxk
    url_template='https://search.bilibili.com/all?keyword=蔡徐坤&page={}'
    headers={
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Referer':'https://www.bilibili.com/',
    }

    session=requests.session()
    session.headers=headers

    res=[]

    def __init__(self,end_page=2):
        self.urls=[self.url_template.format(i) for i in range(1,end_page+1)]

    def get_content(self):
        for url in self.urls:
            try:
                res=self.session.get(url).text
                soup=BeautifulSoup(res,'html.parser')
                videos=soup.find_all(class_='video matrix')
                for item in videos:
                    try:
                        title =item.find('a',class_='title')['title']
                        # cover = item.find('div',class_='lazy-img')
                        # print(cover)
                        time =list(item.find('span',class_='so-icon time').strings)[0].strip()
                        watch_count =list(item.find('span',class_='so-icon watch-num').strings)[0].strip()
                        last_time = item.find('span',class_='so-imgTag_rb').string
                        self.res.append({
                            'title':title,
                            'time':time,
                            'watch_count':watch_count,
                            'last_time':last_time,
                        })
                    except Exception as e:
                        print(e)
                        continue

            except Exception as e:
                print(url,e)
                continue
            print('saving page of {} data into mongo ... '.format(url.split('page=')[1]))
            self.cxk_db.insert_many(self.res)
            self.res=[]

    def get_total_count(self):
        count = self.cxk_db.find().count()
        print('total get {} cxk videos ~'.format(count))


if __name__ == '__main__':
    cxk=CXK(50)
    cxk.get_content()
    cxk.get_total_count()
