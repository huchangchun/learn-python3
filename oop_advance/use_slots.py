# -*- coding:utf-8 -*-
"""
__slots ：定义允许绑定的属性名称
        ：仅对当前类实例起作用，对继承的子类不起作用
"""
class Student():
    __slots__ = ('name','age')
class GraduateStudent(Student):
    pass
s = Student()
s.name = 'Jack'
s.age = 23
# AttributeError : 'Student' object has no attribute 'score'
try:
    s.score = 9
except AttributeError as e:
    print('AttributeError :',e)
g = GraduateStudent()
g.score = 99
print('child class can banding attribute score,g.score=',g.score)

# child class can banding attribute score,g.score= 99