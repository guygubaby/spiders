import requests,json


def get_json():
    url='http://www.lagou.com/lbs/getAllCitySearchLabels.json'
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    res=requests.get(url,headers=headers)
    # 在获取网页的html代码时常常使用res的text属性: html = res.text，在下载图片或文件时常常使用res的content属性:
    return res.content


def read_json_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        data=json.load(f)
    return data


if __name__ == '__main__':
    json_str=get_json()
    data=json.loads(json_str)
    citys=data['content']['data']['allCitySearchLabels']['A']
    with open('cities.json','w',encoding='utf-8') as f:
        json.dump(citys,f,ensure_ascii=False,indent=2)

    file_res=read_json_file('cities.json')
    print(file_res)