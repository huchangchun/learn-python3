# -*- coding:utf-8 -*-
import time
import os
def sqrt(x):
    EPS=0.0000001
    if x == 0:
        return 0
    result = x
    num = 0
    while True:
        num +=1
        print("this is %dth time"%num)
        lastvalue = result
        #牛顿迭代法：x1 = x0/2 + num/2/x0
        result = result / 2 + x / 2 / result
        if abs(result-lastvalue) <EPS:
            return result
if __name__ == '__main__':
    print(sqrt(int(input("请输入数字："))))