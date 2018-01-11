# -*- coding:utf-8 -*-
class Student():
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def print_score(self):
        print('%s :%s'%(self.__name,self.__score))
    #通过方法来修改属性，方法可以对参数做检查，避免传入无效的参数：
    def set_score(self,score):
        if 0<score<=100:
            self.__score = score
        else:
            raise ValueError('Bad score')
    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >=60:
            return 'B'
        else:
            return 'C'
Joe = Student('Joe',59)

print('Joe.name',Joe.get_name())
Joe.set_score(90)
print('Joe.score',Joe.get_score())
print('Joe grade：%s'%(Joe.get_grade()))
print('Do not user Joe.__Student__name:',Joe._Student__name)
# Joe.name Joe
# Joe.score 90
# Joe grade：A
# Do not user Joe.__Student__name: Joe

def classobject():
     num = 0
    def __init__(self):
    def get_name(self):
        return self.__name
    def get_num(self):
        return num
