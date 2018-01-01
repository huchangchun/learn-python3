# -*- coding:utf-8 -*-
def func(self, name='world'):
    print('Hello,%s.' %name)
Hello =type('Hello',(object,),dict(hello=func)) #创建Hello class
h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello)=',type(Hello))
print('type(h)', type(h))