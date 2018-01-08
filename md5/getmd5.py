# -*- coding:utf-8 -*-
import hashlib
import os
import time
import datetime

def get_md5_02(file_path):
    f = open(file_path, 'rb')
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5
def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S', timeStruct)

def get_fileCreateTime(file_path):
    # filePath = os.unicode_literalsode(file_path,'utf-8')
    ct=os.path.getctime(file_path)
    return TimeStampToTime(ct)
def main(file_path):
    fns = [os.path.join(root, fn) for root, dirs, files in os.walk(file_path) for fn in files]
    for fn in fns:
        # 将路径分解为目录名和文件名
        #a,b=os.path.split(r'c:\a\ab.img') a=c:\a\ , b=ab.img
        fpath, fname = os.path.split(fn)
        #分解文件名的扩展名
        # a,b=os.path.split(r'c:\a\ab.img') a=c:\a\ab , b=.img
        fpath_name, extendname = os.path.splitext(fn)
        #跳过txt
        if extendname == '.txt':
            continue
        #计算md5
        md5value = get_md5_02(fn)
        #获取文件创建时间
        ft = get_fileCreateTime(file_path)
        #写md5文件
        mf5filepath =fpath +'\\' + fname + '.md5.txt'
        with open(mf5filepath, 'w+') as fw:
            fw.write('文件名:%s\n' % fname)
            fw.write('创建时间:%s\n' % ft)
            fw.write('MD5:%s\n' % md5value)
if __name__ == "__main__":
    # file_path = input('请输入需要计算的文件的文件夹目录:')
    file_path = r'z:\version'
    main(file_path)


