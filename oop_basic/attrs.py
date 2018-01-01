# -*- coding:utf-8 -*-
class Myobject():
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = Myobject()
print('hasattr(obj,\'x\') = ', hasattr(obj, 'x')) #有属性'x'吗
print('hasattr(obj,\'y\') = ', hasattr(obj, 'y')) #有属性'y'吗
print('hasattr(obj,\'y\') = ', hasattr(obj, 'y')) #有属性'y'吗
setattr(obj,'y',1) #设置一个属性'y'
print('hasattr(obj,\'y\') = ', hasattr(obj, 'y')) #有属性'y'吗
print('getattr(obj,\'y\') = ', getattr(obj, 'y')) #有属性'y'吗
print('obj.y=', obj.y) #获取属性'y'
print('getattr(obj,\'z\') =',getattr(obj,'z',404)) #获取属性‘z',如果不存在，返回默认值404
f = getattr(obj,'power')
print(f)
print(f())
# hasattr(obj,'x') =  True
# hasattr(obj,'y') =  False
# hasattr(obj,'y') =  False
# hasattr(obj,'y') =  True
# getattr(obj,'y') =  1
# obj.y= 1
# getattr(obj,'z') = 404
# <bound method Myobject.power of <__main__.Myobject object at 0x01795230>>
# 81