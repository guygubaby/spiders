from functools import reduce

if __name__ == '__main__':
    a=('机器学习','小说')
    a_str=reduce(lambda prev,next:f'{prev}-{next}',a)
    print(a_str)