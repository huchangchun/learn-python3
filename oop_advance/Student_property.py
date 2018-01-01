# -*- coding:utf-8 -*-
"""
为了限制score的范围，可以通过一个set_score()方法来设置成绩，
再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
"""
class Student1():

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
"""
上面的调用方法又略显复杂，没有直接用属性这么直接简单。
有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？
还记得装饰器（decorator）可以给函数动态加上功能吗？
对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的：
"""

class Student2():
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value <0 or value >100:
            raise ValueError('score must between 0 ~100')
        self.__score = value
s = Student2()
s.score = 60
print('s.score : '%(s.score))
