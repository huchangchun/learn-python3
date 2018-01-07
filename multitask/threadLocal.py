#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import threading
#创建全局ThreadingLocal对象
local_school=threading.local()
def process_student():
    #获取当前线程关联的student:
    std = local_school.student
    print('Hello,% (in %s)' %(std, threading.current_thread().name))
def process_thread(name):
    #绑定ThreadLocal的student
    local_school.student=name
    process_student()

t1 = threading.thread(target= process_thread())
