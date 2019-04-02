import requests

if __name__ == '__main__':
    url='https://www.12306.cn/mormhweb/'
    res=requests.get(url,verify=False,timeout=5)
    print(res.text)
