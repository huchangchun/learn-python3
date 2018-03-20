#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# print('mm333'.
# dic ={"a":1,"b":2}
# print(dic.get("c"))
# print([1,3] in [1,2,3,4])
# print([5,2,8].sort())

#有一堆士力架，第一天吃一半加1个，后面每天都吃一半加1个，直达第6天时只剩下1个
# 问有多少个
d = 6
n = 0
while d>=1:
    if d == 6:
        n = 1
    else:
        n = 2*(n+1)
    print('the %d day:last n:%d' % (d,n))
    d -= 1
print('共:%d个'%(n))

def fun01(day):
    if day == 6:
        sum =1
    else:
        sum = 2*(fun01(day + 1) +1)
    return sum
print("共买了:%d个士力架"%fun01(1))
# the 6 day:last n:1
# the 5 day:last n:4
# the 4 day:last n:10
# the 3 day:last n:22
# the 2 day:last n:46
# the 1 day:last n:94
# 共:94个


#一次性输入任意不少于5个数字（数字以逗号分界）保存在列表中并且对输入的数字进行排序
# 封装成函数
def sortlist(list):
    listlen =len(list)
    for i in range(listlen):
        for j in range(i + 1, listlen):
            if list[j] < list[i]:
                list[i], list[j] = list[j], list[i]
# 1,2,3,2,2,2,12,321,12,23,31,1231
str = input("输入不少于5个数:")
list01 = str.split(',')
newlist=[]
for i in range(len(list01)):
    newlist.append(int(list01[i]))
print(newlist)
sortlist(newlist)
print(newlist)

# 输入不少于5个数:1,4,3,2,7,8
# ['1', '2', '3', '4', '7','8']

#写一个程序，可任意输入一个文件名打开该文件，如果文件不存在则创建
#然后开始写入内容，可重复输入追加到文件中，若写入失败则退出程序
# 当输入#时结束输入，并打印文件的所有内容，将程序封装成函数
def writefile():
    filename = input("输入一个文件名：")
    try:
        with open(filename,'a+') as fw:
            while True:
                content = input('输入')
                if content == '#':
                    break;
                fw.write(content)
    except BaseException :
        return
    with open(filename,'r') as fr:
        content = fr.read()
        print(content)
# writefile()

#time操作
# 1)将字符串的时间 "2017-12-31 23:40:00" 转换为时间戳和时间元组
# 2)字符串格式更改，如time = "2017-12-31 23:40:00" 改为time = "2017/12/31 23-40-00"
# 3)获取两天前的当前时间并以可读的字符串形式（格式如1题）
# 4)通过time输出时间'今天是2018年1月1日 08点08分08秒'
import time
t1 = "2017-12-31 23:40:00"
t1_tuple = time.strptime(t1,"%Y-%m-%d %H:%M:%S")
# print(t1_tuple)
t1_stamp = time.mktime(t1_tuple)
# print(t1_stamp)
t1_fmt = time.strftime("%Y/%m/%d %H-%M-%S",t1_tuple)
# print(t1_fmt)

#返回当前时间的时间戳
now = time.time()
twodayago = now - 60*60*24*2
twodayago_tuple = time.localtime(twodayago)
twodayago_fmt = time.strftime("%Y/%m/%d %H-%M-%S",twodayago_tuple)
# print("twodayago:%s" %twodayago_fmt)
nowfmt = time.localtime(now)
 # print("今天是%s年%s月%s日 %s点%s分%s秒"%(time.strftime('%Y',nowfmt),
 #                                time.strftime('%m',nowfmt),
 #                                time.strftime('%d',nowfmt),
 #                                time.strftime('%H',nowfmt),
 #                                time.strftime('%M',nowfmt),
 #                                time.strftime('%S',nowfmt)))

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
print(nlst)

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
print(nlst)


def fun01(a, *tup_args, **dict_args):
    print(a)
    print(tup_args)
    print(dict_args)
fun01("a1", "a2", name='joe', age=18)
