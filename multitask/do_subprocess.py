#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import subprocess

"""
print('$ nslookup www.python.org')
# subprocess模块可以让我们非常方便地启动一个子进程，
# 然后控制其输入和输出
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)
"""
# $ nslookup www.python.org
# ��Ȩ��Ӧ��:
# ������:  cache-fz.fj133165.com
# Address:  58.22.96.66
#
# ����:    python.map.fastly.net
# Addresses:  2a04:4e42:36::223
# 	  151.101.228.223
# Aliases:  www.python.org
#
# Exit code: 0
print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)