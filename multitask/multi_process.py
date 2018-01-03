#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
multiprocessing 模块是跨平台版本的多进程模块
"""
from multiprocessing import Process
import os
#子进程要执行的代码
def run_proc(name):
    print('Run child process %s(%s)...Parent is %s' % (name, os.getpid(),os.getppid()))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()  #启动进程
    p.join()   #等待子进程结束后继续运行，常用于进程同步
    print('Child process end.')
# Parent process 7396.
# Child process will start.
# Run child process test(5120)...Parent is 7396
# Child process end.

