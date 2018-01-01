# -*- coding:utf-8 -*-
"""
__str__用于给程序开发者
__repr__用户print显示出来给调试服务
"""
class Student():
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object(name=%s)' %self.name
    __repr__=__str__
s = Student('hcc')
s
print(s)
# Student object(name=hcc)