# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
people = ('Michael','Bob','Tracy')
print('people =',people)
print('people[0]=',people[0])
print('people[1]=',people[1])
print('people[2]=',people[2])
print('people[-1]=',people[-1])
 #cannot modify tuple:
# people[0] = 'Bank'
people = ('Michael', 'Bob', 'Tracy')
# people[0]= Michael
# people[1]= Bob
# people[2]= Tracy
# people[-1]= Tracy
# Traceback (most recent call last):
#   File "D:/AI/pythonProject/samples/basic/tuple.py", line 10, in <module>
#     people[0] = 'Bank'
# TypeError: 'tuple' object does not support item assignment