#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
将
[5,5,1,1,2,3,2,2,32,2,2,3,2,2,32,2,3,3,3,3,2]
转变为
[[5, 5], [1, 1], [2], [3], [2, 2], [32], [2, 2], [3], [2, 2], [32], [2], [3, 3, 3, 3], [3]]
"""
lst =[5,5,1,1,2,3,2,2,32,2,2,3,2,2,32,2,3,3,3,3,2]

def group_list(list):
    new_lst = [[]]
    count = len(list)
    for i in range(count-1):
        if list[i]==list[i+1]:
            new_lst[-1].append(list[i])
        else:
            new_lst[-1].append(list[i])
            new_lst.append([])
    new_lst[-1].append(list[i])
    return new_lst
nlst = group_list(lst)
# print(nlst)

"""
将
[5,5,1,1,2,3,2,2,32,2,2,3,2,2,32,2,3,3,3,3,2]
转变为
[[5, 5], [1, 1], 2, 3, [2, 2], 32, [2, 2], 3, [2, 2], 32, 2, [3, 3, 3, 3], 2]
append和extend都仅只可以接收一个参数
append 任意，甚至是tuple
extend 只能是一个列表
"""
def group_listtwo(list):
    new_lst = []
    templist=[]
    count = len(list)
    for i in range(count-1):
        if list[i]==list[i+1]:
            templist.append(list[i])
        else:
            templist.append(list[i])
            if len(templist) >1:
                new_lst.append([])
                for j in templist:
                    new_lst[-1].append(j)
            else:
                new_lst.extend(templist)
            templist.clear()
    if list[i+1] == new_lst[-1]:
        new_lst[-1].append(list[i+1])
    else:
        new_lst.append(list[i+1])
    return new_lst
nlst = group_listtwo(lst)
# print(nlst)

