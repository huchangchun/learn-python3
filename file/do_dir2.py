# -*- coding:utf-8 -*-
"""
文件夹与文件的操作
"""
import os
# 获取当前路径
print(os.getcwd())
# D:\AI\pythonProject\samples\file
#列出当前或指定目录的下的文件或文件夹
print(os.listdir())
# ['do_dir.py', 'do_dir2.py', 'do_file.py', 'do_file_append.py', 'python.txt', 'use_json.py', 'use_pickle.py']
# 判断文件是否存在
print(os.path.exists('.\\do_dir.py'))
# True

#重命名文件
# os.rename('python.txt','pytxt')
#删除文件
# os.remove('pytxt.txt')
print(os.path.split('D:\AI\pythonProject\samples\file\do_dir.py'))
# ('D:\\AI\\pythonProject\\samples\x0cile', 'do_dir.py')
# 创建文件夹
# os.mkdir('study')
# os.rmdir('study')