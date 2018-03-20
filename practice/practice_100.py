# -*- coding:utf-8 -*-
# Python数学计算，编程练习题实例一：
# 简述：这里有四个数字，分别是：1、2、3、4
# 提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
#  Python解题思路分析：可填在百位、十位、个位的数字都是1、2、3、4。
# 组成所有的排列后再去 掉不满足条件的排列。
count = 0
uiqueList=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j !=k:
                # print("%d"%(i*100+j*10+k))
                uiqueList.append(i*100+j*10+k)
                count += 1
# print("总数：%d"%(count))
# print(uiqueList)

# Python数轴、长整型，编程练习题实例二：
# 简述：企业发放的奖金根据利润提成。
# 利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成.
# 提问：从键盘输入当月利润I，求应发放奖金总数？

# lirun = int(input("请输入当月利润："))
# iarr = [1000000,600000,400000,200000,100000,0]
# tichenarr = [0.01,0.015,0.03,0.05,0.075,0.1]
# bonus = 0
# for idx in range(0,6):
#     if lirun>iarr[idx]:
#         bonus += (lirun - iarr[idx])*tichenarr[idx]
#         lirun = iarr[idx]
# print("bonus:%d" %bonus)

# Python完全平方数，编程练习题实例三：
# 简述：一个整数，它加上100和加上268后都是一个完全平方数
# 提问：请问该数是多少？
# Python解题思路分析：在10000以内判断，将该数加上100后再开方，加上268后再开方，如果开方后的结果满足如下条件，即是结果。

import math
for i in range(100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+268))
    if (x * x == i+100) and (y * y == i + 268):
        # print("i:%d" %i)
        pass

# Python日期计算，编程练习题实例四
# 简述：要求判断今天是当年中的第几天
# 闰月时月份大于2时需考虑多加一天
import time
times=time.time()  #返回当前时间的时间戳
nowfmt=time.localtime(times) #返回当前时间的时间元祖
# print(nowfmt)
year = int(time.strftime('%Y',nowfmt))
month = int(time.strftime('%m',nowfmt))
day = int(time.strftime('%d',nowfmt))
print("今天是%d年%d月%d日" %(year,month,day))
daysofmonth = (0,31,59,90,120,151,181,212,243,273,304,334)
sum = daysofmonth[month-1] + day
leap = 0
if (year % 400 ==0) or (year % 4 ==0 and year %100 != 0):
    if (month>2):
        sum +=1
# print("今天是今年的第%d天"%sum)

# Python斐波那契数列应用，编程练习题实例六

# def fibon(n):
#     a = b = 1
#     for i in range(n):
#         yield a
#         a ,b = b,a + b
# for x in fibon(10):
#         print(x)

# Python列表数据复制，编程练习题实例七
# 提问：将一个列表的数据复制到另一个列表中。

x = [1,2,3]
y = x[:]
# print(y)

# 利用切片操作和list方法拷贝等就叫浅拷贝，只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。
# y.append(5)
# x.append(4)
# print(x)
# print(y)
# [1, 2, 3, 4]
# [1, 2, 3, 5]

# Python乘法口诀计算，编程练习题实例八
# 简述：9*9乘法口诀表。 要求：逐项单位输出。例如1的一行，2的一行，以此类推。
# 左下三角形
# for i in range(1,10):
#     for j in range(1,i+1):
#         print("%d*%d=%d"%(j,i,i*j),end=" ")
#     print()
# 左上三角形
# for i in range(1,10):
#     for j in range(i,10):
#         print("%d*%d=%d"%(j,i,i*j),end=" ")
#     print()
# Python判断素数，编程练习题实例九
#质数（Prime number），又称素数，指在大于1的自然数中，
# 除了1和该数自身外，无法被其他自然数整除的数
# （也可定义为只有1与该数本身两个因数的数）。——via维基百科
def isPrime(n):
    ret = False
    if n <= 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            print("%d is not a prime"%n)
            ret = False
            break
    else:
        print("%d is a prime" % n)
        ret = True
    return ret
for i in range(1,201):
    # isPrime(i)
    pass
# Python水仙花数for循环应用，编程练习题实例十三
def shuixianhua(n):
    bai = n // 100
    shi = n % 100 // 10
    ge = n  % 10
    # print("%d:百：%d,十:%d,个:%d"%(n,bai,shi,ge))
    if n == bai**3 +shi**3 + ge**3:
        print("%d is a shuixianshu"%n)
for i in range(100,10000):
    # shuixianhua(i)
    pass
# Python字母排序，编程练习题实例十四
# 有两个磁盘文件A和B,各存放一行字母,要求把这两个文件中的信息合并(按字母顺序排列), 输出到一个新文件C中
import string
# fa = fb = None
# with open("a.txt","r") as fr:
#     fa = fr.read()
#     fr.close()
#
# with open("b.txt","r") as fr:
#     fb = fr.read()
#     fr.close()
#
# lst = list(fa+fb)
# lst.sort()
# s = ""
# s = s.join(lst)
# with open("ab.txt",'w+',encoding='utf-8') as fw:
#     fw.write(s)
#     fw.close()
# with open("ab.txt","r") as fr:
#     content = fr.read()
    # print("content:")
    # print(content)
    # fr.close()
# Python　矩阵对角线，编程练习题实例十五
#
# a = []
# sum = 0
# for i in range(3):
#     a.append([])
#     for j in range(3):
#         a[-1].append(float(input("num:\n")))
# for i in range(3):
#     sum += a[i][i]
# print(sum)

# Python　回推与递推，编程练习题实例十六
# 题目：已知有五位朋友在一起。
# 第五位朋友他说自己比第4个人大2岁；
# 问第4个人岁数，他说比第3个人大2岁；
# 问第三个人，又说比第2人大两岁；
# 问第2个人，说比第一个人大两岁；
# 最后问第一个人，他说是10岁
# 求第5个人的年龄
def getage(n):
    if n == 1:
        age = 10
    else:
        age = getage(n-1) + 2
    return age
# print("the %d age:%d" %(5,getage(5)))

# Python　查找列表中出现最频繁的数，编程练习题实例十七
# 题目：找到列表中出现最频繁的数，
# 例如：test = [1,2,3,4,2,2,3,1,4,4,4]
test = [1,2,3,4,2,2,3,1,4,4,4]
a = {}
for i in test:
    if test.count(i) > 1:
        a[i] = test.count(i)
# print(a)

# Python 阶乘计算，编程练习题实例十八
# 题目：一行代码计算任何数的阶乘
#阶乘的函数实现
def functionjiecheng(n):
    if n == 1:
        return 1
    else:
        return n * functionjiecheng(n - 1)

# print(functionjiecheng(4))
#阶乘的一行代码实现
from functools import reduce
# print(reduce(lambda x,y:x*y,range(1,int(input("请输入一个数字打印其阶乘："))+1)))


# Python 切片，编程练习题实例十九
# 列举python列表的成员方法，并给出以下列表操作的答案：
# (1) a=[1, 2, 3, 4, 5], a[::2]=?, a[-2:] = ?
# (2) 一行代码实现对列表a中的偶数位置的元素进行加3后求和？
# (3) 将列表a的元素顺序打乱，再对a进行排序得到列表b，然后把a和b按元素顺序构造一个字典d。
a=[1, 2, 3, 4, 5]

# print(a[-2:])
# [4, 5]
# print(a[::2])
# [1, 3, 5]
# print(a[:2])
# [1,2]
# reduce(求和,偶数位加上后的列表)
result = reduce(lambda x,y:x+y,[x +3  for x in a if ((a.index(x) + 1) % 2) == 0 ])
# print("result:%d" % result)
from random import shuffle
shuffle(a)
# print(a)
# [3, 1, 5, 2, 4]
b = sorted(a,reverse=True)
print(b)
# [5, 4, 3, 2, 1]
# zip 并行迭代，将两个序列“压缩”到一起，然后返回一个元组列表，最后，转化为字典类型。
dic = dict(zip(a,b))
# {3: 5, 1: 4, 5: 3, 2: 2, 4: 1}
# print(dic)
z = zip(a,b)
for i in z:
    pass
    # print("%d = %d" %(i[0],i[1]))
    # 3 = 5
    # 5 = 4
    # 2 = 3
    # 4 = 2
    # 1 = 1


#Python 内存管理，编程练习题实例二十
'''
 python 内存空间是以Python私有堆得形式进行管理。
 所有的python对象和数据结构都存放在一个私有堆中。
 解释器可以访问私有对，而程序员不可以
 将Python堆空间中的内存分配给Python对象的工作是由Python内存管理完成的。
 而内核API则会提供给程序员一些相关的工具来完成涉及到内存的编码工作
 Python还内置垃圾回收器，从而进行回收释放内存到堆空间
  
'''
#Python extendlist，编程练习题实例二十一
# 以下代码的输出是什么？
def extendList(val,list=[]):
    list.append(val)
    return list
list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
# 新的默认列表仅仅只在函数被定义时创建一次。
# 随后当 extendList 没有被指定的列表参数调用的时候，其使用的是同一个列表
# print("list01:%s" %list1)
# list1 = [10, 'a']
# print("list01:%s" %list2)
# list2 = [123]
# print("list01:%s" %list3)
# list3 = [10, 'a']
def extendList01(val,list = None):
    if list == None:
        list = []
    else:
        list.append(val)
    return list

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')
# print("list01:%s" %list1)
# list1 = [10]
# print("list01:%s" %list2)
# list2 = [123]
# print("list01:%s" %list3)
# list1 = ['a']

#Python except，编程练习题实例二十二
# 介绍一下except的用法和作用？
# 答案：
# try…except…except…[else…][finally…]
# 执行try下的语句，如果引发异常，则执行过程会跳到except语句。对每个except分支顺序尝试执行，如果引发的异常与except中的异常组匹配，执行相应的语句。如果所有的except都不匹配，则异常会传递到下一个调用本代码的最高层try代码中。
# try下的语句正常执行，则执行else块代码。如果发生异常，就不会执行
# 如果存在finally语句，最后总是会执行。

#Python 逆向打印，编程练习题实例二十三
# 题目：raw_input获取给定的一个不多于5位的正整数。
# 要求：
# 一、求它是几位数；
# 二、逆序打印出各位数字
'''
x = int(input("请输入一个数：\n"))
12300
a = x // 10000
b = x % 10000 //1000
c = x % 1000 //100
d = x % 100 //10
e = x % 10
if a != 0:
    print("5 位数 :%d%d%d%d%d"%(a,b,c,d,e))
elif b != 0:
    print("4 位数:%d%d%d%d"%(b, c, d, e))
elif c != 0:
    print("3 位数:%d%d%d"%(c, d, e))
elif d != 0:
    print("2 位数:%d%d"%(d,e))
else:
    print("1 位数:%d"%(e))
'''
#Python 算法，编程练习题实例二十三
# 题目：365天，丈夫工作5天休息2天，妻子工作3天，休息1天。
# 丈夫工作的第一天正好是妻子休息的第一天，请问两人一年内共同休息天数为多少?

a = []
b = []
for i in range(392):
    a.append(0)
b = a[:]

for i in range(0,392-7,7):
    a[i+5] = 1
    a[i+6] = 1
for i in range(0,392-5,4):
    b[i] = 1
cout = 0
for i in range(365):
    if a[i] & b[i] == 1:
        # print("%d:%d:%d"%(i,a[i],b[i]))
        count += 1
# print("Count:%d" %count)


#Python 算法，编程练习题实例二十四
# 有一个列表a[],里面有若干个整数未知。
# 我希望将里面的整数两两做差（即a[1]-a[0],a[3]-a[2]....），
# 并将得数保存在另一个列表b[]中，请问如何实现？
lista=[1,3,3,4,2,6,8,10,9,13,15]
listb = []

while i<len(lista):
    listb.append(lista[i] -lista[i-1])
    i += 2
# print(listb)


# favorite_places = {'jack':['newYork,','Tokoy'],'job':'北京','tom':'南京'}
# # input("输入你喜欢的地方：")
# name = input('请输入名称：')
# for k in favorite_places:
#     if name==k:
#         print("喜欢的城市是：%s" %favorite_places[k])
# for k ,v in favorite_places.items():
#     print(k,v)
#
# for i in range(1,10):
#      for j in range(1,i+1):
#             # print(i)
#             print('%d x %d = %d'%(j,i,(i*j)),end ='\t')
#             # print('{0} * {1} = {2}'.format(j,i,r))
#      print()
#
# sum=0
# for i in range(1,101):
#     print(i)
#     sum=sum+i
# print(sum)
# # str = input("请输入一串字符串：")
# i = 1
# while i<10:
#     print(i)
#     j=1
#     while j<=i:
#
#         print('%d x %d = %d'%(j,i,i*j),end=' ')
#         j+=1
#     i+=1
#     print()

# str = input("input a string:")
# list1 = []
# for i in str:
#     if i.isdecimal == True:
#         list1.append(int(i))
#     else:
#         list1.append(i.upper())
# print(list1)
# inputok = False
# num = 0
# while inputok==False:
#     num = input("输入一个8位以内的数:")
#     if len(num) <=8:
#         inputok = True
#     else:
#         print("number invalid,input again!")
# print("len:%d" %len(num))
# print(num[::-1])

# high = float(input("输入高度:"))
# sum = 0
# x = int(input("第几次落地:"))
# i = 1
# while i<=x:
#     if i == 1:
#         sum += high
#     else:
#         high /= 2
#         sum += high*2
#     i += 1
# print('行程%f'%sum)
#Python 算法，编程练习题实例二十五
# 题目：假设一直皮球从100米高度自由落下，条件，每次落地后反跳会高度的一半后，再落下
# 要求：算出这支皮球，在它在第10次落地时，共经过多少米？第10次反弹多高

def gethigh(n):
    high = 100
    sum = 100
    sn = 50
    i = 0
    while i<n:
        if i == 0:
            sum = high
        else:
            sum += sn*2
            sn =sn/2
        i += 1
    print("第次共经过:%d"%sum)
    print("第%d次反弹:%d"%(i,sn))
gethigh(2)

#

# list02 = list(range(6))
# print(list02)
# list03= [i for i in list02]
# print(list03)
# list04=[i for i in range(3,10) if i%2==0]
# print(list04)
# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]
#      ]
# k = [[2,2,2],
#      [3,3,3],
#      [4,4,4]
#      ]
# print(m)
# print(k)
# for i in range(0,3):
#     for n in range(0,3):
#         print(m[i][n])
# list04 = [m[i][n] + k[i][n] for i in range(0,3) for n in range(0,3)]
# print(list04)
# list05=['joe','susan','black']
# print(list(enumerate(list05)))
# dict02 = {k:v for k,v in enumerate(list05)}
# print(dict02)
# dict01 = {'name':'joe','age':'18'}
# print(dict01)
# print(list(dict01.items()))
# for k ,v in dict01.items():
#     print(k,v)

# 水仙花数
# for i in range(100,1000):
#     x = i // 100
#     y = i % 100 // 10
#     z = i  % 10
#     if i == x**3 +y**3 + z**3:
#         print(i)
# i= 143
# print(i//100)
# print(i%100)

# i ='*'
# m='***'
# print(i.center(7))
# print(m.center(7))

# for i in range(1,8,2):
#     print(('*'*i).center(7))
# for i in range(5,0,-2):
#     print(('*'*i).center(7))
# 判断回文
# n =input('输入一个5位数：')
# # if len(n) != 5:
# #     print('输入有误')
# if n == n[::-1]:
#     print(n)

# 对角线求和
# m = [[1,2,3],
#      [4,5,6],
#      [7,8,9]]
# sum = 0
# print(len(m))
# for i in range(len(m)):
#     j = i-1
#     sum += m[i][j]
# print(sum)
# sum = 0
# for i in range(len(m)):
#     j = 2-i
#     sum += m[i][j]
# print

# list= []
# for x in range(1,5):
#     for y in range(1,5):
#         for z in range(1,5):
#             if x !=y and x != z and y !=z:
#                 list.append(x*100 + y*10 +z)
# list01 = [x*100 + y*10 +z for x in range(1,5) for y in range(1,5) for z in range(1,5) if x!=y and y!=z and x!=z]
# print(list01)
# name=['Tom','Bill','Jeffer']
# # dict={k:v for k,v in enumerate(name)}
# # print(dict)
# print(list(enumerate(name)))
# name={'Tom':'p1','Jeffer':'p2'}
# login = False
# flag =0
# while flag <=3:
#     if flag == 3:
#         print('login failed exceed 3 times')
#         break
#     flag +=1
#     user = input('input Account:')
#     pwd = input('input password:')
#     if user in name:
#         if pwd  == name[user]:
#             print('%s login success!' % user)
#             break
#         else:
#             print('password error !')
#     else:
#         print('accout error!')

# 阶乘
# a = int(input('输入一个数：'))
# x =1
# for i in range(1,a+1):
#     x*=i
# print(x)

# 冒泡排序
list01 = [2,6,1,4,19,12,12312,12,32,1232]
listlen = len(list01)
for i in range(listlen):
    for j in range(i+1,listlen):
        if list01[j] < list01[i]:
            list01[i],list01[j]=list01[j],list01[i]
print(list01)


import copy
list_0 = ["A", "B", ["C", "D"], "E"]
list_1 = copy.copy(list_0)
list_2 = list_0.copy()
list_3 = list_0[:]
list_4 = list(list_0)

# --- 深拷贝的拷贝方式 ---
list_d = copy.deepcopy(list_0)


# --- 深浅拷贝的区别 ---
# 1. 对第一层数据进行赋值
list_0[0] = "X0"
list_1[0] = "X1"
list_2[0] = "X2"
list_3[0] = "X3"
list_4[0] = "X4"
list_d[0] = "Xd"

# 打印结果: 理所当然,所有列表都发生了变化
# list_0: ['X0', 'B', ['C', 'D'], E]
# list_1: ['X1', 'B', ['C', 'D'], E]
# list_2: ['X2', 'B', ['C', 'D'], E]
# list_3: ['X3', 'B', ['C', 'D'], E]
# list_4: ['X4', 'B', ['C', 'D'], E]
# list_d: ['Xd', 'B', ['C', 'D'], E]

# 2. 对第二层的list引用进行赋值
list_0[2][0] = "Y0"
list_1[2][0] = "Y1"
list_2[2][0] = "Y2"
list_3[2][0] = "Y3"
list_4[2][0] = "Y4"
list_d[2][0] = "Yd"

# 打印结果: 0-1都被改成了同一个值,这说明浅拷贝只拷贝了第二层list的引用;而深拷贝则拷贝了数据结构
# list_0: ['X0', 'B', ['Y4', 'D'], E]
# list_1: ['X1', 'B', ['Y4', 'D'], E]
# list_2: ['X2', 'B', ['Y4', 'D'], E]
# list_3: ['X3', 'B', ['Y4', 'D'], E]
# list_4: ['X4', 'B', ['Y4', 'D'], E]
# list_d: ['Xd', 'B', ['Yd', 'D'], E]

# 3. 对第三层的Ls对象引用进行赋值
list_0[3]= "Z0"
list_1[3]= "Z1"
list_2[3]= "Z2"
list_3[3]= "Z3"
list_4[3]= "Z4"
list_d[3]= "Zd"

# 执行结果: 继续验证了上方论点
# list_0: ['X0', 'B', ['Y4', 'D'], Z4]
# list_1: ['X1', 'B', ['Y4', 'D'], Z4]
# list_2: ['X2', 'B', ['Y4', 'D'], Z4]
# list_3: ['X3', 'B', ['Y4', 'D'], Z4]
# list_4: ['X4', 'B', ['Y4', 'D'], Z4]
# list_d: ['Xd', 'B', ['Yd', 'D'], Zd]
print(list_0)
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_d)