import requests,json,js2py

context=js2py.EvalJs()


class BaiduTranslate:
    url='https://fanyi.baidu.com/basetrans'
    extendtrans_url='https://fanyi.baidu.com/extendtrans'
    headers={
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
        'Referer':'https://fanyi.baidu.com/',
        "Cookie": 'BIDUPSID=CA885046A578E1F43601B168DE837DF0; PSTM=1536981387; BAIDUID=CA885046A578E1F43601B168DE837DF0:SL=0:NR=10:FG=1; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; MCITY=-300%3A; BDUSS=FhvT2ZKaVJDZDV2TUYwWEJ-NGF4YTdWNnp4Qng1ZEZhY3RacGtQRUZjbjNzcWxjQVFBQUFBJCQAAAAAAAAAAAEAAAAUi3dNZ3V5Z3ViYWJ5ZW5qb3kAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPclglz3JYJca; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1463_21098_28771_28723_28557_28832_28585_28604_28626_22157; pgv_pvi=5889657856; pgv_si=s8614663168; delPer=0; PSINO=7; locale=zh; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1554965027,1554965040,1554966195; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1554966195; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1554965040,1554966195; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1554966195'
    }
    session=requests.session()
    session.headers=headers
    base_data={
        'query':None,
        'from':'en',
        'to':'zh',
        'token':'78234a9306903b097f84d9919131a451',
        'sign':None
    }

    def __init__(self,query):
        self.base_data.update({'query':query})

    def get_sign(self):
        with open('./a.js','r',encoding='utf-8') as f:
            context.execute(f.read())
        sign=context.a(self.base_data['query'])
        return sign

    def translate(self):
        sign=self.get_sign()
        self.base_data['sign']=sign
        # res=self.session.post(self.url,data=self.base_data).json()['trans']
        res=self.session.post(self.extendtrans_url,data=self.base_data)
        res.encoding='utf-8'
        data=res.json()['data']
        with open(f"./tanslation/{self.base_data['query']}.json",'w',encoding='utf-8') as f:
            json.dump(data,f,ensure_ascii=False,indent=2)
            print('ok :) ')


if __name__ == '__main__':
    query=input('input a word : ')
    translater=BaiduTranslate(query)
    translater.translate()