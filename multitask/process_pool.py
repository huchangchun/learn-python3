#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from multiprocessing import Pool
import pdb
import os,time,random
def long_time_task(name):
    print('Run task %s %s...'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print('Task %s run %0.2f seconds .'%(name,end-start))

if __name__=='__main__':
    # pdb.set_trace()
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waitting for all subprocess done...')
    p.close()   #调用close()之后就不能继续添加新的Process
    p.join()   #调用join()之前必须先调用close()
    print('All subprocess done.')

# Run task 0 3588...
# Run task 1 5492...
# Run task 2 3836...
# Run task 3 5280...
# Task 1 run 0.22 seconds .
# Run task 4 5492...   #Pool的默认大小是CPU的核数，因此task4需要等待一个执行完成
# Task 3 run 1.80 seconds .
# Task 4 run 1.71 seconds .
# Task 0 run 2.36 seconds .
# Task 2 run 2.82 seconds .
# All subprocess done.