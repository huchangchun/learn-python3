# -*- coding:utf-8 -*-
"""
reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，
map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# >>> def f(x):
# ...     return x * x
# >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# >>> list(r)
# [1, 4, 9, 16, 25, 36, 49, 64, 81]
"""
from functools import reduce
DIGITS={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8}
def str2int(s):
    def fn(x,y):
        return x*10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn,map(char2num, s))
print(str2int('1234567'))
# 1234567