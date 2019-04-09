import requests,time,json
from bs4 import BeautifulSoup
from itertools import chain
from functools import reduce


class BookSpider:
    url_template='https://book.douban.com/tag/{}?start={}&type=T' # 第一个参数是类别，第二个是数量(每隔20个一页)
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Host':'book.douban.com'
    }
    session=requests.session()
    session.headers=headers

    res_list=[]

    def __init__(self,book_types=('机器学习','小说'),end_count=40):
        self.book_types=book_types
        self.end_count=end_count

    def init_urls(self):
        urls=[]
        for type in self.book_types:
            urls.append([self.url_template.format(type,start) for start in range(0,self.end_count,20)])
        return list(chain.from_iterable(urls))

    def crawl(self):
        urls=self.init_urls()
        for i,url in enumerate(urls):
            print(f'magic happen in crawing page {i+1} ...')
            time.sleep(3)
            res=self.session.get(url)
            self.save_data(res.text)
            print(f'page {i+1} complete')

    def save_data(self,data):
        soup = BeautifulSoup(data, 'html.parser')
        lis=soup.find_all('li',attrs={'class':'subject-item'})
        book_info={}
        for li in lis:
            info=li.select('.info')[0]
            star_info=info.find('div',class_='star')
            try:
                book_name=info.find('a')['title']
                pub=info.find('div',class_='pub').string.strip()
                rating_nums=star_info.find('span',class_='rating_nums').string.strip()
                rate_count=star_info.find('span',class_='pl').string.strip()
                short_desc=info.find('p').string.strip()

                book_info['name']=book_name
                book_info['pub']=pub
                book_info['rating_nums']=rating_nums
                book_info['rate_count']=rate_count
                book_info['short_desc']=short_desc
            except Exception as e:
                print(f'some errors accure {e}')
                continue

            self.res_list.append(book_info)
            book_info={}


if __name__ == '__main__':
    book_spider=BookSpider()
    book_spider.crawl()
    data=book_spider.res_list
    json_name_prefix=reduce(lambda prev,next:f'{prev}-{next}',book_spider.book_types)
    with open(f'{json_name_prefix}-books-total-{len(data)}.json','w',encoding='utf-8') as f:
        json.dump(data,f,ensure_ascii=False,indent=2)
    print('all done :) ')

