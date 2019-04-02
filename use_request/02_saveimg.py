import requests

if __name__ == '__main__':
    url = "http://docs.python-requests.org/zh_CN/latest/_static/requests-sidebar.png"
    res=requests.get(url)
    with open('../imgs/hhh.png','wb') as f:
        f.write(res.content)