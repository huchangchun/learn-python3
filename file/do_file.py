# -*- coding:utf-8 -*-
"""
open('文件名','打开的模式)
 r: 只读的方式打开，如果文件不存在会提示错误
 w: 只写的方式打开，如果文件存在则覆盖，不存在则创建
 a: 打开一个文件进行追加内容，如果存在则打开，不存在则创建新的
 文件

 r+ :读写，文件指针调到文件的头部
 w+ 读写，文件不存在则直接创建，存在覆盖文件
 a+ 追加读写，会将文件的指针调到文件的末尾

"""
# 打开文件
# files = open('python.txt','r',encoding='utf-8')
# print(files)
# i = 1
# for line in files:
#     print('%d ,%s'%(i,line))
#     i+=1
# content=files.read(3)
# files.close()
# print(content)

'''
写入文件
'''
files1=open('python.txt','r',encoding='utf-8')
# str=files.read(5)
# position=files.tell()
# print(position)
# print(str)
# str=files.read(10)
# position=files.tell()  #获取文件偏移量
# print(position)
# print(str)
# files.seek(4)       #设置文件指针
# position=files.tell()
# print(position)
# content='\nloveyou'
# # files.write(content)
# files.close()
file1=open('python.txt','r',encoding='utf-8')
content =file1.read()
files1.close()
file2=open('python.txt','w+',encoding='utf-8')
file2.write(content.replace("c++","python"))
file2.seek(0)
content = file2.read()
print(content)