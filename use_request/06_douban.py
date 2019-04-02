import requests
from retrying import retry


@retry(stop_max_attempt_number=3)
def get_hot_movies(url,params):
    headers={
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.75 Safari/537.36'
    }
    res=requests.get(url=url,headers=headers,params=params,timeout=5)
    return res


if __name__ == '__main__':
    url='https://movie.douban.com/j/search_subjects'
    for page_start in range(0,100,20):
        params={
            'type': 'movie',
            'tag': '热门',
            'sort': 'recommend',
            'page_limit': 20,
            'page_start': page_start
        }
        res=get_hot_movies(url,params)
        json_str=res.json()
        for movie in json_str['subjects']:
            img_res=requests.get(movie['cover'])
            img_name=movie['title']+movie['rate']
            img_format=movie['cover'].split('/')[-1].split('.')[1]
            print(f'current movie is : {img_name}')
            with open(f'../movies/{img_name}.{img_format}','wb') as f:
                f.write(img_res.content)
