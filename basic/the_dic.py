# -*- coding:utf-8 -*-
d = {
    'Michael':95,
    'Bob':75,
    'Tracy':85
}
print('d[\'Michael\']=',d['Michael'])
#  通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value
print('d.get(\'Thomas\',-1)=',d.get('Thomas',-1))
# d['Michael']= 95
# d.get('Thomas',-1)= -1
d.get(\'Bob\',-1)=')