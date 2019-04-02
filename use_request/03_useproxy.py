import requests

if __name__ == '__main__':
    headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    }
    proxies={
        'http':'http://guygubaby.top:8090'
    }
    res=requests.get('http://www.baidu.com',headers=headers,proxies=proxies)
    print(res.text)
