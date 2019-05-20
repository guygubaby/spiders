import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json


class Woaidu:
    res=[]
    def __init__(self,end_page=10):
        self.url_template = 'https://www.woaidu.org/sitemap_{}.html'
        self.end_page=end_page

    def init_urls(self):
        return [self.url_template.format(i) for i in range(1,self.end_page+1)]

    async def fetch(self,session,url):
        async with session.get(url) as response:
            response.encoding='utf-8'
            return await response.text()

    async def run(self):
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            for url in self.init_urls():
                print(f'current url is : {url}')
                html = await self.fetch(session,url)
                soup=BeautifulSoup(html,'html.parser')
                article_list = soup.find_all('div', class_='sousuolist')
                for article in article_list:
                    if article.text.strip() is not None:
                        title=article.text.strip()
                        self.res.append(title)


if __name__ == '__main__':
    woaidu=Woaidu()
    loop=asyncio.get_event_loop()
    loop.run_until_complete(woaidu.run())
    loop.close()

    with open('woaidu_async.json','w',encoding='utf-8') as f:
        json.dump(woaidu.res,f,ensure_ascii=False,indent=2)
