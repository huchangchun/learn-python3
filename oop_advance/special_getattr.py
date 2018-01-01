# -*- coding:utf-8 -*-
"""
__getattr__动态返回一个属性
当调用不存在的属性时，比如score，
Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性
这样，我们就有机会返回score的值：
"""
"""
class Student(object):
    def __init__(self):
        self.name = 'Joe'
    def __getattr__(self, attr):
        if attr =='score':
            return 99
        raise AttributeError('\'Student\' object has no attribute \'%s\''%attr)

s = Student()
print(s.name)
print(s.score)
# AttributeError: 'Student' object has no attribute 'other'
s.other
"""
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__
api = Chain().status.user.timeline.list
print(api)
# /status/user/timeline/list