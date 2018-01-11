#!/usr/bin/env python3
# -*- coding:utf-8 -*-
class Restaurant():
    """
    餐馆类
    """
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        self.restaurant_name = restaurant_name #name
        self.cuisine_type = cuisine_type #菜系
        self.number_served = number_served
    def descibe_restaurant(self):
        print('名称：%s ,菜系：%s' %(self.restaurant_name,self.cuisine_type))
    def open_restaurant(self):
        print('欢迎光临%s，正在营业' %self.restaurant_name)
    #设置就餐人数
    def set_number_served(self,n):
        self.number_served = n
        print('当前就餐人数：%d'%self.number_served)
    #递增增加就餐人数
    def increment_number_served(self,n):
        for i in range(1,n+1):
            self.number_served += 1
            print('当前就餐人数：%d' %self.number_served)
if __name__ == '__main__':
    r1 = Restaurant('KFC','西餐')
    print(r1.restaurant_name)
    print(r1.cuisine_type)
    r1.descibe_restaurant()
    r1.open_restaurant()

    r1.set_number_served(40)
    r1.increment_number_served(40)
# KFC
# 西餐
# 名称：KFC ,菜系：西餐
# 欢迎光临KFC，正在营业
# 当前就餐人数：40
# 当前就餐人数：41
# 当前就餐人数：42
# .......