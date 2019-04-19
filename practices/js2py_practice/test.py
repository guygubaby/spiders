import js2py
import datetime


if __name__ == '__main__':
    # context=js2py.EvalJs()
    # with open('./getPwd.js','r',encoding='utf-8') as f:
    #     js=f.read()
    #     context.execute(js)
    #     res=context.getPwd('mistletoe',23)
    #     print(res)

    time=datetime.datetime.now().day
    print(time)
