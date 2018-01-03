#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
unix/linux 系统提供了fork调用，调用一次返回两次
因为操作系统自动把当前进程复制了一份，然后在父进程和子进程内返回
子进程永远返回0，父进程返回子进程的id
一个父进程可以fork出很多子进程，所以父进程要记下每个子进程的ID，
而子进程只要调用getppid()就可以拿到父进程的ID
"""

import os
print('process (%s) start....' %os.getpid())
#only works on unix/linux
pid = os.fork()

if pid == 0:
    print('I am child process (%s) and my parent is %s.' %(os.getpid(),os.getppid()))
else:
    print('I (%s) just created a child process  (%s).' %(os.getpid(),pid))
# Process (876) start...
# I (876) just created a child process (877).
# I am child process (877) and my parent is 876.