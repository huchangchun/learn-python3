# -*- coding:utf-8 -*-

# r+中,替换内容相当于追加内容
# with open('python.txt','r+',encoding='utf-8') as fw:
#     contents=fw.read()
#     fw.write(contents.replace('java','python'))
#     fw.flush()
#     fw.seek(0)
#     contents_1=fw.read()
#     print(contents_1)


# file1=open('test.txt','r+',encoding='utf-8')
# content_1=file1.read()
# file1.close()
# w+存在则覆盖，不存在则创建
with open('python.txt','w+',encoding='utf-8') as fw:
    contents2=fw.read()
    fw.write(content_1.replace('python','java'))
    fw.flush()
    fw.seek(0)
    contents2=fw.read()
    print(contents2)
    fw.close()