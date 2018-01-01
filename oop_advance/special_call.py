# -*- coding:utf-8 -*-
class Student():
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' %self.name)
s = Student('Joe')
s()
# My name is Joe.
