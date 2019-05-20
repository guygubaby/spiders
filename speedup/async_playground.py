import asyncio


async def crawl(url):
    print(f'start crawl {url}')
    await asyncio.sleep(2)
    print(f'complete {url}')


def init_urls(end_page=10):
    url_template='https://baidu.com?page={}'
    return [url_template.format(i) for i in range(end_page)]


async def run(loop):
    tasks=[
     loop.create_task(crawl(url)) for url in init_urls()
    ]
    await asyncio.wait(tasks)


if __name__ == '__main__':
    loop=asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()