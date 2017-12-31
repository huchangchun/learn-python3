# -*- coding:utf-8 -*-
import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('call %s():'%func.__name__)
        return func(*args, **kwargs)
    return wrapper
@log
def now():
    print('now :2017-12-31')
now()

def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            print('%s %s():'%(text,func.__name__))
            return func(*args,**kwargs)
        return wrapper
    return decorator
@logger('DEBUG')
def today():
    print('today:2018-12-31')
today()
print(today.__name__)

# call now():
# now :2017-12-31
# DEBUG today():
# today:2018-12-31
# today
