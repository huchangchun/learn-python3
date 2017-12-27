# -*- coding:utf-8 -*-
"""
def hi(name="yasoob"):
    def greet():
        return "Now in greet"
    def welcome():
        return "Now in welcome"
    if name=="yasoob":
        return greet
    else:
        return welcome
a = hi()
"""
# when you put a pair of
# parentheses after it, the function gets executed;
# whereas if you don’t put parenthesis after it, then it can be passed around and can be assigned to other variables without executing it
# print(a)
# <function hi.<locals>.greet at 0x017A1D68>
# print(a())
# Now in greet
"""
7.4. Giving a function as an argument to another function
"""
def hi():
    return "hi yasoob!"
def doSomethingBeforehi(func):
    # print("I am doing some boring work")
    # print(func())
doSomethingBeforehi(hi)
"""
7.5. Writing your first decorator
"""
