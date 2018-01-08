#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
# ，multiprocessing需要“模拟”出fork的效果，
# 父进程所有Python对象都必须通过pickle序列化再传到子进程去，
# 所有，如果multiprocessing在Windows下调用失败了，要先考虑是不是pickle失败了。
在父进程中创建两个进程，一个往Queue里写数据
一个从Queue里读数据
"""

from multiprocessing import Process, Queue
import os, time, random

#写数据进行执行的代码：
def write(q):
    print('Process to write :%s' % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())
#读数据进程执行的代码：
def read(q):
    print('Process to read :%s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' %value)
if __name__=='__main__':
    #父进程创建Queue,并传给各个子进程
    q=Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw,写入
    pw.start()
    #启动子进程pr，读取
    pr.start()
    #等待pw结果
    pw.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止：
    pr.terminate()

# Process to read :3896
# Process to write :8184
# Put A to queue...
# Get A from queue.
# Put B to queue...
# Get B from queue.
# Put C to queue...
# Get C from queue.

