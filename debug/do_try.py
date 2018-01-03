# -*- coding:utf-8 -*-
try:
    print('try....')
    r = 10 / 0
    print('result:',r)
except ZeroDivisionError as e:
    print('except:',e)
finally:
    print('finally...')
print('END')

try:
    print(aaa)
except (ValueError,NameError) as e:
    print(e)
    # name 'aaa' is not defined
#所有异常
try:
    print(aaa)
except Exception as e:
    print(e)


    # name'aaa' is not defined
try:
    print('aaa')
except Exception as e:
    print(e)
else:
    print('no problem')