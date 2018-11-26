#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
赋值：
Python中string、tuple和number是不可变对象，而dict、list等是可变对象；
不可变对象在进行重新赋值的时候，实际上是将原始值丢弃，将变量指向一个新值；
可变对象的可变性实质上是指更改可变对象中的子对象，比如list中的item元素的更改。
"""
#直接赋值：其实就是对象的引用（别名）
# 列表和字典可变对象的赋值，比如a=b，a和b的id地址一样
"""
a = [1,2,3]
b = [11,22,33]
c = [111,222,333]
var01 = [a,b,c]
var02 = var01
print(var01)
print(var02)
print(id(var01))
print(id(var02))
a.append(4)
print(var01)
print(var02)
print(id(var01))
print(id(var02))
"""
#深拷贝，浅拷贝
# 浅拷贝：
# 不拷贝子对象(针对子对象中的item)，当子对象进行更改的时候，
# 原始对象也会改变。常见操作：列表的切片[:]操作、list()操作，
# 字典的copy()函数、copy模块的copy()函数（两个一模一样的双胞胎）
# 深拷贝：会拷贝子对象，当对原始对象子对象进行更改的时候，
# 原始对象不会改变。
# 常见操作：copy模块的deepcopy()函数
import copy
list_0 = ["A","B",["C","D"],"E"]
list_1 = copy.copy(list_0)
list_2 = list_0.copy()
list_3 = list_0[:]
list_4 = list(list_0)
#深拷贝的拷贝方式
list_d = copy.deepcopy(list_0)

#深浅拷贝的区别
#1.对第一层数据进行赋值
list_0[0] = "X0"
list_1[0] = "X1"
list_2[0] = "X2"
list_3[0] = "X3"
list_4[0] = "X4"
list_d[0] = "Xd"
#打印结果：
print(list_0)
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_d)
# ['X0', 'B', ['C', 'D'], 'E']
# ['X1', 'B', ['C', 'D'], 'E']
# ['X2', 'B', ['C', 'D'], 'E']
# ['X3', 'B', ['C', 'D'], 'E']
# ['X4', 'B', ['C', 'D'], 'E']
# ['Xd', 'B', ['C', 'D'], 'E']

# 2.对第二层的list引用进行赋值
list_0[2][0] = "Y0"
list_1[2][0] = "Y1"
list_2[2][0] = "Y2"
list_3[2][0] = "Y3"
list_4[2][0] = "Y4"
list_d[2][0] = "Yd"
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_d)
# 打印结果: 0-1都被改成了同一个值,这说明浅拷贝只拷贝了第二层list的引用;
# 而深拷贝则拷贝了数据结构
# ['X1', 'B', ['Y4', 'D'], 'E']
# ['X2', 'B', ['Y4', 'D'], 'E']
# ['X3', 'B', ['Y4', 'D'], 'E']
# ['X4', 'B', ['Y4', 'D'], 'E']
# ['Xd', 'B', ['Yd', 'D'], 'E']
# 3. 对第三层的Ls对象引用进行赋值
list_0[3]= "Z0"
list_1[3]= "Z1"
list_2[3]= "Z2"
list_3[3]= "Z3"
list_4[3]= "Z4"
list_d[3]= "Zd"
print(list_1)
print(list_2)
print(list_3)
print(list_4)
print(list_d)
# ['X1', 'B', ['Y4', 'D'], 'Z1']
# ['X2', 'B', ['Y4', 'D'], 'Z2']
# ['X3', 'B', ['Y4', 'D'], 'Z3']
# ['X4', 'B', ['Y4', 'D'], 'Z4']
# ['Xd', 'B', ['Yd', 'D'], 'Zd']

# 思路一：利用切片操作和list方法拷贝等就叫浅拷贝，只是拷贝了最外围的对象本身，内部的元素都只是拷贝了一个引用而已。
# 思路二：利用copy中的deepcopy方法进行拷贝就叫做深拷贝，外围和内部元素都进行了拷贝对象本身，而不是引用。
#     但是对于数字，字符串和元组类型对象，没有被拷贝的说法，即便是用深拷贝，查看id的话也是一样的，如果对其重新赋值，
# 也只是新创建一个对象，替换掉旧的而已

a = [1,2,3, [3,4,5]]
b = a[:]
print(b)
#[1, 2, 3, [3, 4, 5]]
a[3].append(6)
print(a)
#[1, 2, 3, [3, 4, 5, 6]]
print(b)
#[1, 2, 3, [3, 4, 5, 6]]
#切片只拷贝了最外围的对象

 
def my_deepcopy(arr):
    rt = []
    for item in arr:
        if isinstance(item,list):
            rt.append(my_deepcopy(item))
        else:
            rt.append(item)
    return rt
if __name__ == '__main__':
    a =  [1,2,3, [3,4,5]]
    b = my_deepcopy(a)
    b[3][2] = 'test'
    print(a)
    print(b)