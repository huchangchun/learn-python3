# -*- coding:utf-8 -*-
# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple
import math
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x
def move(x,y,step,angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

if __name__ =='__main__':
    n = my_abs(-20)
    print(n)
    x , y = move(100, 100, 60, math.pi/60)
    print(x,y)
    # my_abs('123')

# TypeError: bad operand type
