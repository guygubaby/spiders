import requests,random,json,os
from bs4 import BeautifulSoup
from pymongo import MongoClient

import multiprocessing as mp
import asyncio


class WoaiDu:
    requests.packages.urllib3.disable_warnings()
    url_template='https://www.woaidu.org/sitemap_{}.html'
    session=requests.session()
    user_agent_list=[]

    res_list=[]

    # mongo_client=MongoClient('127.0.0.1',27017)
    # woaidu_db=mongo_client.mydb.woaidu

    def __init__(self,end_page=100):
        self.end_page=end_page
        self.session.headers=self.get_random_user_agent(1)

    def init_urls(self):
        return [self.url_template.format(i) for i in range(1,self.end_page+1)]

    def crawl(self):
        print('Run task %s...'% os.getpid())
        urls=self.init_urls()
        article_info={}
        for i,url in enumerate(urls):
            if i%20==0:
                self.session.headers=self.get_random_user_agent(len(urls))
            res=self.session.get(url,verify=False)
            res.encoding='utf-8'
            soup=BeautifulSoup(res.text,'html.parser')
            article_list=soup.find_all('div',class_='sousuolist')
            for index,article in enumerate(article_list):
                try:
                    info=article.find('a')
                    print(f'current article is : {info.string.strip()}')

                    if index%5==0:
                        self.session.headers=self.get_random_user_agent()

                    addition_info_url=f"https://www.woaidu.org{info['href']}"
                    addition_info=self.session.get(url=addition_info_url,verify=False)
                    addition_info.encoding='utf-8'
                    addition_soup=BeautifulSoup(addition_info.text,'html.parser')
                    img_url_temp=addition_soup.find('div',class_='hong').find('img')['src']
                    img_url=f'https://www.woaidu.org/{img_url_temp}' if 'no_images' in img_url_temp else img_url_temp
                    description=addition_soup.find('div',class_='lili').string.strip()
                    last_edit_time=addition_soup.find('div',class_='jiewei').string.strip()
                    author=addition_soup.find('div',class_='xiaoxiao').string.strip()

                    download_urls=addition_soup.find_all('div',class_='xiazai_xiao')[1:]
                    urls=[]
                    for download_url in download_urls:
                        try:
                            url=download_url.find('div',class_='pcdownload').find('a')['href']
                            urls.append(url)
                        except:
                            continue

                    article_info['title']=info.string.strip()
                    article_info['author']=author
                    article_info['img_url']=img_url
                    article_info['description']=description
                    article_info['last_edit_time']=last_edit_time
                    article_info['url']=addition_info_url
                    article_info['download_urls']=urls

                    img_res=self.session.get(url=img_url,verify=False).content
                    img_format=img_url.split('.')[-1]
                    img_name=f"./imgs/{article_info['title']}.{img_format}" if '/' not in addition_info['title'] else f"./imgs/{article_info['title']}.{img_format}"
                    with open(img_name,'wb') as f:
                        f.write(img_res)

                except Exception as e:
                    continue

                self.res_list.append(article_info)
                article_info={}
                urls=[]
            # print(len(self.res_list))

    def get_random_user_agent(self,times=20):
        if len(self.user_agent_list) == 0:
            with open('../user_agents.txt','r') as f:
                self.user_agent_list=f.readlines()
        user_agent_str = self.user_agent_list[
            random.randint(0, times if len(self.user_agent_list) > times else len(self.user_agent_list))]
        return {
            "User-Agent":user_agent_str.strip()[1:-1]
        }


if __name__ == '__main__':
    pool=mp.Pool(mp.cpu_count())

    end_page=5
    woaidu=WoaiDu(end_page)

    for i in range(5):
        pool.apply_async(woaidu.crawl)

    pool.close()
    pool.join()

    # woaidu.crawl()
    print('length->',len(woaidu.res_list))
    # woaidu.woaidu_db.insert_many(woaidu.res_list) # save data to mongodb
    # with open('./woaidu/woaidu.json','w',encoding='utf-8') as f:
    #     json.dump(woaidu.res_list,f,ensure_ascii=False,indent=2)
    print('ok :)')
    print(f'finally get {len(woaidu.res_list)} articles')