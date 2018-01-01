# -*- coding:utf-8 -*-
class Animal():
    def __init__(self,name,food):
        self.name = name
        self.food = food
    def eat(self):
        print('%s like %s'%(self.name,self.food))
class Dog(Animal):
    def __init__(self,name,food,drink):
        #加载父类构造方法
        super(Dog,self).__init__(name,food)
        self.drink = drink
    def drinks(self):
        print('%s 爱喝 %s' %(self.name,self.drink))
kitty = Dog('kt','骨头','牛奶')
kitty.eat()
kitty.drinks()
print('kitty is Animal?',isinstance(kitty,Animal))
print('kitty is dog1?',isinstance(kitty,Dog))

# kt like 骨头
# kt 爱喝 牛奶
# kitty is Animal? True
# kitty is dog1? True
