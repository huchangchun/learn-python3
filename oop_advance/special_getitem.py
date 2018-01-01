# -*- coding:utf-8 -*-
"""
在 about__iter__.py中
Fib实例可作用域for循环，看起来和list有点像
但是把它当list用不行,
要变相得像list那样按照下表去除元素，需要实现__getitem()__()方法：
"""
class Fib(object):
    def __getitem__(self, item):
        if isinstance(item ,int): #item是索引
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item,slice): #item是切片
            start = item.start
            stop = item.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a,b = b,a+b
            return L

f = Fib()
print(f[0:5]) #切片
# [1, 1, 2, 3, 5]
print(f[10])  #索引
# 89
#to do
#虽然可以实现切片和索引，但是step参数还没有处理
#负数也没有处理，所以要正确实现一个__getitem__()还是有很多工作要做的。