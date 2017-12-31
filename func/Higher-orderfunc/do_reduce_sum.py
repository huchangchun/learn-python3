# -*- coding:utf-8 -*-
"""
Python提供的sum()函数可以接受一个list并求和，
编写一个prod()函数，可以接受一个list并利用reduce()求积：
"""
from functools import reduce

def t(x,y):
    return x*y
def prod(L):
    return reduce(t,L)
list = [1,2,3,4,5,6]

if prod(list) == 720:
    print('测试成功')
else:
    print('测试失败')