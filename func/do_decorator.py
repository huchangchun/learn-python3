# -*- coding:utf-8 -*-
def log(text):
    def decor(func):
        def wrapper(*args,**kwargs):
            print('call %s %s():' %(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decor
#把 @log放在now()函数的定义出，相当于执行了语句：
# now=log(now),
@log('execute')
def now():
    print('2017-12-31')
#now=log('execute')(now)
now()
print(now.__name__)
# call execute now():
# 2017-12-31
# wrapper   #

# 一个完整的decorator写法：
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('call %s():'%func.__name__)
        return func(*args, **kwargs)
    return wrapper
#针对带参数的decorator
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator
