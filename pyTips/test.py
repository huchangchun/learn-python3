# -*- coding:utf-8 -*-
def getage(n):
    if n == 1:
        age = 10
    else:
        age = getage(n-1) + 2
    return age
print("第 %d 个人 age:%d" %(5,getage(5)))