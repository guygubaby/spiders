import requests
from retrying import retry

@retry(stop_max_attempt_number=3)
def test(url):
    print(f'访问 {url}')
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
    }
    proxies={
        'http':'47.93.1.124:8090'
    }
    res=requests.get(url=url,proxies=proxies,headers=headers,timeout=5)
    return res.text


if __name__ == '__main__':
    url='http://www.baidu.com'
    try:
        html=test(url)
        print(f'ok : {html}')
    except Exception as e:
        print(e)