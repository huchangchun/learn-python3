# -*- coding:utf-8 -*-
str='k:1|k1:2|k3:3|k4:4'
str_list =str.split('|')
d = {}
for i in str_list:
    key,value = i.split(':')
    d[key]=value
print(d)