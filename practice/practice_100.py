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
for i in range(1,10):
    for j in range(1,i+1):
        print("%d*%d=%d"%(j,i,i*j),end=" ")
    print()
# 左上三角形
for i in range(1,10):
    for j in range(i,10):
        print("%d*%d=%d"%(j,i,i*j),end=" ")
    print()
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
    isPrime(i)
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
    shuixianhua(i)