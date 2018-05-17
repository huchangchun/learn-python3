<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
定义一个班级类
1、班级人数（初始为0人，外部不能随便访问）
班级类类方法：
1、执行班级人数增加操作（在子类实例化对象是完成增加操作）
2、获取班级总人数
定义一个学生类，学生类继承班级类。有下面的实例属性：
1、姓名
2、年龄
3、成绩（语文，数学，英语) [各科为整数]
学生的普通方法：
1、获取学生的姓名：返回姓名
2、获取学生的年龄：返回姓名加年龄
3、获取学生的单科成绩：返回学科加成绩
4、返回3门科目中最高的分数：返回学科加成绩
测试如下：
大家好我叫joe
姓名：joe 年龄：20
这是我的语文：69
我最好的成绩是英语：100
---------------------------------
大家好我叫Bank
姓名：Bank 年龄：21
这是我的语文：90
我最好的成绩是数学：100

"""
class Banji():
    __Num = 0
    # __Users={}
    def __init__(self):
        Banji.__Num += 1
    @classmethod
    def getNum(cls):
        print('班级总人数为：%d'%cls.__Num)
        return cls.__Num;
class Student(Banji):

    def __init__(self,name,age,scores):
        super(Student,self).__init__()
        self.name = name
        self.age = age
        self.scores=scores
    def getname(self):
        print('大家好我叫：%s' % self.name)
    def getage(self):
        print('姓名：%s年龄:%s' % (self.name,self.age))
    def getscore(self,kemu):
        print('这是我的%s：%d' % (kemu,self.scores[kemu]))
    def getMaxscore(self):
        sortlst = sorted(self.scores.items(),key=lambda e:e[1])
        print('我最好的成绩是%s：%d' % (sortlst[-1][0],sortlst[-1][1]))


stu1 = Student('joe',20,{"数学":90,"英语":100,"语文":69})
stu2 = Student('susan',20,{"数学":100,"英语":70,"语文":99})
stu1.getname()
stu1.getage()
stu1.getscore("语文")
stu1.getMaxscore()
print('---------------')
stu2.getname()
stu2.getage()
stu2.getscore("语文")
stu2.getMaxscore()
# 大家好我叫：joe
# 姓名：joe年龄:20
# 这是我的语文：69
# 我最好的成绩是英语：100
# ---------------
# 大家好我叫：susan
# 姓名：susan年龄:20
# 这是我的语文：99
# 我最好的成绩是数学：100
=======
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
定义一个班级类
1、班级人数（初始为0人，外部不能随便访问）
班级类类方法：
1、执行班级人数增加操作（在子类实例化对象是完成增加操作）
2、获取班级总人数
定义一个学生类，学生类继承班级类。有下面的实例属性：
1、姓名
2、年龄
3、成绩（语文，数学，英语) [各科为整数]
学生的普通方法：
1、获取学生的姓名：返回姓名
2、获取学生的年龄：返回姓名加年龄
3、获取学生的单科成绩：返回学科加成绩
4、返回3门科目中最高的分数：返回学科加成绩
测试如下：
大家好我叫joe
姓名：joe 年龄：20
这是我的语文：69
我最好的成绩是英语：100
---------------------------------
大家好我叫Bank
姓名：Bank 年龄：21
这是我的语文：90
我最好的成绩是数学：100

"""
class Banji():
    __Num = 0
    __Users={}
    def __init__(self):
        Banji.__Num += 1
    @classmethod
    def getNum(cls):
        print('班级人数：%d'%cls.__Num)
        return cls.__Num;
class Student(Banji):

    def __init__(self,name,age,scores):
        super(Student,self).__init__()
        self.name = name
        self.age = age
        self.scores=scores
    def getname(self):
        return self.name
    def getage(self):
        return self.name,self.age
    def getscore(self,kemu):
        return self.scores[kemu]
    def getMaxscore(self):
        sortlst = sorted(self.scores.items(),key=lambda e:e[1])
        return sortlst[-1][0],sortlst[-1][1]

stu1 = Student('joe',20,{"数学":90,"英语":80,"语文":89})
stu2 = Student('Tom',10,{"数学":95,"英语":70,"语文":99})
print('我的名字：%s'%stu1.getname())
print('姓名：%s年龄:%s'%stu1.getage())
print('这是我的语文：%d'%stu1.getscore("语文"))
print('我最好的成绩是%s：%d'%stu1.getMaxscore())

print('我的名字：%s'%stu2.getname())
print('姓名：%s年龄:%s'%stu2.getage())
print('这是我的语文：%d'%stu2.getscore("语文"))
print('我最好的成绩是%s：%d'%stu2.getMaxscore())
stu1.getNum()

# 我的名字：joe
# 姓名：joe年龄:20
# 这是我的语文：89
# 我最好的成绩是数学：90
# 我的名字：Tom
# 姓名：Tom年龄:10
# 这是我的语文：99
>>>>>>> c352954ac35edc7aa2593da2f426884a7948709d
