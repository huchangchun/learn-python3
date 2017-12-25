# -*- coding:utf-8 -*-
"""
匿名函数
lambda def [参数]():表达式 return xx
默认会返回一个表达式
"""
s = lambda :'哈哈'
y = lambda x: x ** 2
z = lambda i,j: i+j ** 2
# print(s())
# print(y(10))

"""
字典排序
"""
dic= {'a':1,'c':3,'b':2}
# dic = sorted(dic.items(),reverse= True)
# dic = sorted(dic)

# print({ k:v for k,v in dic})
# print(dic)

# dic = sorted(dic.items(),key = lambda x:x[1],reverse = True)
# print(dic)
# print({ k:v for k,v in dic})
list02=[{'name':'joe','age':18},
         {'name':'susan','age':19},
         {'name':'tom','age':17}]
dic2 = sorted(list02,key= lambda x:x['age'],reverse = True)
# print(dic2)
#[{'name': 'susan', 'age': 19}, {'name': 'joe', 'age': 18}, {'name': 'tom', 'age': 17}]

"""
高阶函数
"""
list01 = [1,2,3,4,5]
new_list = map(lambda x:x*2,list01)
# print(new_list)
# print(list(new_list))
# <map object at 0x019751F0>
# [2, 4, 6, 8, 10]
"""
reduce
"""
from functools import reduce
list02 = [2,4,6,8,10]
new_list = reduce(lambda x,y:x+y,list02)
# print(new_list)
# 30
# 2+4+6+8+10 = 30
name = ['joe','susan','black','lili']
age= [18,19,20]
sex = ['m','w','m','w']
# format user name
new_name=map(lambda x:x.title(),name)
new_name =list(new_name)
# print(new_name)
# ['Joe', 'Susan', 'Black', 'Lili']
# 将用户名性格性别放一起
new_users = map(lambda x,y,z:(x,y,z),new_name,age,sex)
new_users = list(new_users)
# print(new_users)
# [('Joe', 18, 'm'), ('Susan', 19, 'w'), ('Black', 20, 'm')]

# 过滤男性

new_users = filter(lambda x:x[2] == 'm',new_users)
# print(list(new_users))
# [('Joe', 18, 'm'), ('Black', 20, 'm')]
new_user_list = list(new_users)
#求性别为男的的用户的平均年龄
age_total = reduce(lambda x,y:x+y[1],new_user_list,0)
# print(age_total)
# print(age_total/len(new_user_list))
# 38
# 19.0