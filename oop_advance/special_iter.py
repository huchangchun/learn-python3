# -*- coding:utf-8 -*-
"""
如果一个类箱被用于for ..in 循环
类似list或tuple那样，就必须实现一个__iter__方法
该方法返回一个迭代对象，然后python的for循环
就会不断的调用该迭代对象的__next__()方法返回一个值
知道遇到StopIteration错误时退出循环
"""
class Fib(object):
    def __init__(self):
        self.a = 0 #初始化两个计数器a，b
        self.b = 1
    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a >10:
            raise StopIteration()
        return self.a #返回下一个值

for n in Fib():
    print(n)
# TypeError: 'Fib' object does not support indexing
Fib()[5]
