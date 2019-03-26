# -*- coding:utf-8 -*-
import time
#返回格林威治西部的夏令时地区的偏移秒数
# print(time.altzone)
#返回当前时间 Wed Jan  3 20:49:33 2018
# print(time.asctime())
#返回进程时间
# print(time.clock())

# print(time.ctime()) #Wed Jan  3 20:55:14 2018

#返回当前时间的时间戳
# 从1970 0点到现在的秒数
# print(time.time()) #1514984172.5781288
times=time.time()
# print(time.ctime(times)) #返回可读形式的当前时间

#返回格林威治时间元组 time.struct_time(tm_year=2018, tm_mon=1, tm_mday=3, tm_hour=12, tm_min=59, tm_sec=56, tm_wday=2, tm_yday=3, tm_isdst=0)
# print(time.gmtime())

#返回当前时间的时间元组
# print(time.localtime())
# time.struct_time(tm_year=2018, tm_mon=1, tm_mday=3, tm_hour=21, tm_min=5, tm_sec=10, tm_wday=2, tm_yday=3, tm_isdst=0)
"""
时间戳转换为时间元组，将时间元组转换未字符串
"""
times=time.time()
# print(times) #1514985036.8365617

# print(time.localtime(times)) #time.struct_time(tm_year=2018, tm_mon=1, tm_mday=3, tm_hour=21, tm_min=10, tm_sec=36, tm_wday=2, tm_yday=3, tm_isdst=0)
formattime=time.localtime(times)
# print(formattime) #time.struct_time(tm_year=2018, tm_mon=1, tm_mday=3, tm_hour=21, tm_min=10, tm_sec=36, tm_wday=2, tm_yday=3, tm_isdst=0)
# print(time.strftime('%Y-%m-%d %H:%M:%S',formattime)) #2018-01-03 21:11:24
# times = time.strftime('%Y-%m-%d %H:%M:%S',formattime)
# print(time.strptime(times,'%Y-%m-%d %H:%M:%S'))# time.struct_time(tm_year=2018, tm_mon=1, tm_mday=3, tm_hour=21, tm_min=12, tm_sec=41, tm_wday=2, tm_yday=3, tm_isdst=-1)
#将字符创时间转换为时间元组
# t1='2017-01-03 23:40:00'
# t2=time.strptime(t1,"%Y-%m-%d %H:%M:%S")
# print(t2)
# print(time.strftime('%Y/%m/%d %H-%M-%S',t2))
# # 2017/01/03 23:40:00   #格式转换
# #j将时间元组转换为时间戳
# print(time.mktime(t2))
# 1483458000.0

t1='2017-01-03 23:40:00'
t2=time.strptime(t1,"%Y-%m-%d %H:%M:%S")
print(t2)
print(time.strftime('%Y/%m/%d %H:%M:%S',t2))  # 2018/01/03 21:11:24
print(time.mktime(t2))
now = time.time()#1514985084.0
formatTime=time.localtime(now) #2018/01/03 21:11:24
twoDayago= now - 60*60*24*2
print('three days ago: %s ' %time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(twoDayago)))

times=time.time()
formattime=time.localtime(times)
print(formattime)

print(time.strftime('今天是%Y年%m月%d日 %H点%M分%S秒',formattime)) #