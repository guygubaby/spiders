import json


if __name__ == '__main__':
    # json_str='''
    # {
    #     "name": "crise",
    #     "age": 18,
    #     "parents": {
    #         "monther": "妈妈",
    #         "father": "爸爸"
    #     }
    # }
    # '''
    # data=json.loads(json_str)
    # with open('test.json','w',encoding='utf-8') as f:
    #     json.dump(data,f,ensure_ascii=False,indent=2)


    with open('test.json','r',encoding='utf-8') as f:
        data=json.load(f)
        print(data,type(data))