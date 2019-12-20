er#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#time操作
# 1)将字符串的时间 "2017-12-31 23:40:00" 转换为时间戳和时间元组
# 2)字符串格式更改，如time = "2017-12-31 23:40:00" 改为time = "2017/12/31 23-40-00"
# 3)获取两天前的当前时间并以可读的字符串形式（格式如1题）
# 4)通过time输出时间'今天是2018年1月1日 08点08分08秒'
import time
t1 = "2017-12-31 23:40:00"
t1_tuple = time.strptime(t1,"%Y-%m-%d %H:%M:%S")
print(t1_tuple)
t1_stamp = time.mktime(t1_tuple)
print(t1_stamp)
t1_fmt = time.strftime("%Y/%m/%d %H-%M-%S",t1_tuple)
print(t1_fmt)

#返回当前时间的时间戳
now = time.time()
twodayago = now - 60*60*24*2
twodayago_tuple = time.localtime(twodayago)
twodayago_fmt = time.strftime("%Y/%m/%d %H-%M-%S",twodayago_tuple)
print("twodayago:%s" %twodayago_fmt)
nowfmt = time.localtime(now)
print("今天是%s年%s月%s日 %s点%s分%s秒"%(time.strftime('%Y',nowfmt),
                                time.strftime('%m',nowfmt),
                                time.strftime('%d',nowfmt),
                                time.strftime('%H',nowfmt),
                                time.strftime('%M',nowfmt),
                                time.strftime('%S',nowfmt)))
# time.struct_time(tm_year=2017, tm_mon=12, tm_mday=31, tm_hour=23, tm_min=40, tm_sec=0, tm_wday=6, tm_yday=365, tm_isdst=-1)
# 1514734800.0
# 2017/12/31 23-40-00
# twodayago:2018/01/19 22-55-02
# 今天是2018年01月21日 22点55分02秒