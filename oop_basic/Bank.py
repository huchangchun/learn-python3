#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
模拟一个简单的银行进行业务办理的类

类：
    创建一个银行类
属性：
    一个属于银行的类属性
        用来存储所用银行的开户信息，包含卡号、密码、用户名、余额
        （外界不能随意访问和修改。开户时要进行卡号验证，查看卡号是否已经存在）

    每个对象拥有
        卡号、密码、用户名、余额
        （外界不能随意访问和更改）

方法：
    银行类拥有 (类方法)
        查看本银行的开户总数
        查看所有用户的个人信息（包含卡号、密码、用户名、余额）
    每个对象拥有
        实例化对象的时候传入相关参数
            初始化对象及类属性
        取钱（需要卡号和密码验证）
            通过验证卡号和密码对个人的余额进行操作，如果取钱大于余额，返回余额不足
        存钱（需要卡号和密码验证）
            通过验证卡号和密码对个人的余额进行操作，返回操作成功
        查看个人详细信息（需要卡号密码验证）
            返回个人的卡号，用户名，余额信息
"""

class Bank:
    #定义类属性
    __Users={}
    def __init__(self,CardId,Pwd,UserName,Balance):
        if CardId not in Bank.__Users:
            Bank.__Users[CardId] = {"Pwd": Pwd, "UserName": UserName, "Balance": Balance}
            self.__CardId = CardId
            self.__UserName = UserName
            self.__Pwd = Pwd
            self.__Balance = Balance
    #定义类方法：查看用户总数
    @classmethod
    def checkUserNumber(cls):
        print("当前储蓄用户数： %d" %(len(Bank.__Users)))

    #定义类方法：查看用户信息
    @classmethod
    def getInfo(cls):
        for user,value in Bank.__Users.items():
            print("卡号：%s 密码：%s 用户名：%s 余额：%d\n" %(user,value["Pwd"],value["UserName"],value["Balance"]))
    #定义静态方法访问类属性
    @staticmethod
    def checkUser(cardId,pwd):
        if Bank.__Users[cardId]["Pwd"] == pwd:
            return True
        else:
            return False

    @staticmethod
    def checkMoney(money):
        if isinstance(money,int):
            return True
        else:
            False

    #定义实例方法：取钱
    def withdraw(self,cardId,pwd,money):
        if Bank.checkUser(cardId,pwd):
            if Bank.checkMoney(money):
                if Bank.__Users[cardId]["Balance"] > money:
                    print("开始取钱:%d" %money)
                    Bank.__Users[cardId]["Balance"] -= money
                else:
                    print("您的余额不足")
            else:
                print("您输入的金额有误！")
        else:
            print("密码错误")
    #定义实例方法：存钱
    def deposit(self,cardId,pwd,money):
        if Bank.checkUser(cardId,pwd):
            print("开始存钱：%d" %money)
            Bank.__Users[cardId]["Balance"] += money
            return True
        else:
            print("密码错误")
            return False
    #定义实例方法：查看余额
    def getUserBalance(self,cardId,pwd):
        if Bank.checkUser(cardId,pwd):
            print("卡号：%s 用户名：%s 余额：%d" %(cardId,Bank.__Users[cardId]["UserName"],Bank.__Users[cardId]["Balance"]))
        else:
            print("密码错误")
Joe = Bank("612321325643","123456","joe",10000)
Jack = Bank("61232132564","234567","Jack",20000)

Bank.checkUserNumber()
Bank.getInfo()
Joe.getUserBalance("612321325643","123456")
Jack.getUserBalance("61232132564","234567")
Joe.deposit("612321325643","123456",8000)
Joe.getUserBalance("612321325643","123456")
Joe.deposit("612321325643","123456",4000)
Joe.getUserBalance("612321325643","123456")
Joe.withdraw("612321325643","123456",8000)
Joe.getUserBalance("612321325643","123456")


# 当前用户数1
# __________________________________________________
# 卡号：1001
# 用户名：joe
# 密码：111111
# 余额：100
#
# 余额不足
# __________________________________________________
# 当前卡号1001,当前存款金额300,当前余额400
# __________________________________________________
# 当前卡号1001,当前用户名joe,当前余额400