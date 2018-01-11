#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class person():
    """
    this is a person class
    """
    country = 'China'  #声明类属性，并且复制
    #实例属性通过构造方法来声明
    #self不是关键字，代表的是当前对象
    def __init__(self, name, age, sex, address, country):
        #构造方法不需要调用，在实例化的时候自动调用
        self.name = name #创建实例属性，并且复制
        self.age = age
        self.sex = sex
        self.__address = address #双下划线开头的属性是私有属性
        person.country = country
    def getName(self):
        #类属性的使用通过类名.属性名使用，这是规范
        #私有属性在类里面可正常使用
        print('name: %s ,from :%s %s'%(self.name,person.country,self.__address))
    #创建一个静态方法
    @staticmethod
    def staticfun():  #不需要传递实例
        #静态方法不能访问实例属性
        #静态方法只能访问类属性
        print('from %s' %person.country)
    #类方法
    @classmethod
    def classfun(cls,n):   #class也不是关键字
        #类方法不能访问实例属性
        cls.country = n
        print('from %s' %cls.country)  #就用cls.类属性
#实例化对象
people01 = person('joe',19,'男','外滩十八号','上海')
#通过对象来调用静态方法
# people01.staticfun()
#通过对象来调用类方法
# people01.classfun('南京')

#静态方法和类方法的调用，推荐使用类名的方法去调用
#通过类名调用静态方法
person.staticfun()
person.classfun('USA')