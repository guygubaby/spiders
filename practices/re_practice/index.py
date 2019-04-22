import re

'''
* 0 无限
+ 1 无限
？ 0 1
'''

if __name__ == '__main__':
    re_str=r'\w?'
    pattern=re.compile(re_str)
    res=pattern.findall('asdfasdsafasd asdf asdf')
    print(''.join(res),len(res),len('asdfasdsafasd asdf asdf'))
