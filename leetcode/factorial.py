#encoding=utf-8
def factorial(num):
    if num == 1:
        return num
    else:
        return factorial(num-1)*num
#print(factorial(365*5))

import decimal
def factorial2(num,value):
    if num == 1:
        return value
    else:
        return  factorial2(num-1,value)*value

print(factorial2(900,1.01))  #1.01 的900次方
#7748.834840250834
print(factorial2(900,0.99))  #0.88 的900次方
#0.00011794380589564402


 