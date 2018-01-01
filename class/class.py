# -*- coding:utf-8 -*-
"""
 类定义
 class 类名（）：
    #类文档说明
    属性
    方法
 """
class person():
    """
    这是一个人类
    """
    country = 'China' #类属性,通过类名调用
    #实例属性通过构造方法来声明
    def __init__(self,name,age,sex,address):
        #  构造方法
        # 通过self穿件实例属性，并且赋值
        # print('我是构造方法，在实例化的时候调用')
        self.name = name
        self.age = age
        self.sex = sex
        self.__address = address #双下划线声明私有属性
    def getName(self):
        #类属性的使用通过类名，
        print('Name is %s from %s %s' %(self.name,person.country,self.__address))
    #外部要修改私有属性，预留一个接口去访问
    def GetAddr(self):
        return self.__address
people = person('joe',19,'men','上海')
people.getName()
print(people.GetAddr())
# 上海
# print(people._person__address)  #不建议这样使用
people.__address="Beijing"  #看上去好像改了，其实没有
print(people.GetAddr())
# 上海
# 上海
# 上海
# print(people.__address)
# AttributeError: 'person' object has no attribute '__address'
# 我是构造方法，在实例化的时候调用
# people.getName()  #通过对象访问属性方法
# # Name is joe from China
# print(people.name)
# # joe
# """
# 内置方法
# """
# print(getattr(people,'name'))
# # joe
# print(hasattr(people,'name'))
# # True
# setattr(people,'name','susan')
# print(people.name)
# susan
# delattr(people,'name')
# print(people.name)
# AttributeError: 'person' object has no attribute 'name'
"""
内置类属性
"""
# print(people.__dict__)  #将实例对象的属性和值通过字典的方式返回
# {'name': 'joe', 'age': 19, 'sex': 'men'}
# print(person.__name__)
# person
# print(person.__bases__)
# (<class 'object'>,)