#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import threading
import time
def music(name,loop):
    for i in range(loop):
        print('listen music %s %s '%(name, time.ctime()))
        time.sleep(1)
def movie(name,loop):
    for i in range(loop):
        print('look movie %s %s' %(name, time.ctime()))
        time.sleep(1)
#创建多线程
t1 = threading.Thread(target=music,args=('爱的故事上集',3))
t2 = threading.Thread(target=music,args=('肖生克的救赎',4))
if __name__=='__main__':
    #守护主线程，主线程结束杀死子线程
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()  #启动线程
    t2.start()
    t1.join()  #阻塞线程，子线程结束完，继续执行主线程
    t2.join()
    print('end time is %s ' %time.ctime())
# listen music 爱的故事上集 Sat Jan  6 23:02:12 2018
# listen music 肖生克的救赎 Sat Jan  6 23:02:12 2018
# listen music 爱的故事上集 Sat Jan  6 23:02:13 2018
# listen music 肖生克的救赎 Sat Jan  6 23:02:13 2018
# listen music 爱的故事上集 Sat Jan  6 23:02:14 2018
# listen music 肖生克的救赎 Sat Jan  6 23:02:14 2018
# listen music 肖生克的救赎 Sat Jan  6 23:02:15 2018
# end time is Sat Jan  6 23:03:05 2018

"""
if __name__ == '__main__':
    # 守护主线程，主线程结束杀死子线程
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()  # 启动线程
    t2.start()
    print('end time is %s ' % time.ctime())
"""
# listen music 爱的故事上集 Sat Jan  6 23:10:21 2018
# listen music 肖生克的救赎 Sat Jan  6 23:10:21 2018
# end time is Sat Jan  6 23:10:21 2018