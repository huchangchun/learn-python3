# -*- coding:utf-8 -*-
# origin site :http://book.pythontips.com/en/latest/
# 1.1. Usage of *args
def test_var_args(f_arg, *argv):
    print("first normal args:",f_arg)
    for arg in argv:
        print("another arg through *argv:",arg)
test_var_args('yasoob','python','eggs','test')


# 1.2 Usage of **kwargs
# **kwargs allows you to pass keyworded variable length of arguments to a function.
# You should use **kwargs if you want to handle named arguments in a function. Here
# is an example to get you going with it:

def greet_me(**kwargs):
    for key,value in kwargs.items():
        print("{0} = {1}".format(key, value))
# greet_me(name="yasoob")

# 1.3 Using *args and **kwargs to call a function
def test_args_kwargs(arg1, arg2,arg3):
    print('arg1:',arg1)
    print('arg2:',arg2)
    print('arg3:',arg3)
args=("two",3,4)
test_args_kwargs(*args)
kwargs = {"arg3":3,"arg2":"two","arg1":5}
test_args_kwargs(**kwargs)
# arg1: two
# arg2: 3
# arg3: 4
# arg1: 5
# arg2: two
# arg3: 3
def some_func(fargs,**kwargs):
    print("first normal args:",fargs)
    for key,value in kwargs.items():
        print("{0} = {1}".format(key, value))
kwargs = {'fargs':3,'ac':5,'a2':"two",'a3':"ther"}
# some_func(**kwargs)

"""
Commands:
c: continue execution
w: shows the context of the current line it is executing.
a: print the argument list of the current function
s: Execute the current line and stop at the first possible occasion.
n: Continue execution until the next line in the current function is reached or it returns.
import pdb
pdb.set_trace()
"""
import pdb
def make_bread():
    pdb.set_trace()
    return "I don't have time"
# print(make_bread())

# 3.4 Generators
# Generators are iterators, but you can only iterate over them once. It’s because they do
# not store all the values in memory, they generate the values on the fly. You use them
# by iterating over them, either with a ‘for’ loop or by passing them to any function
# or construct that iterates. Most of the time generators are implemented as functions.
# However, they do not return a value, they yield it. Here is a simple example of a
# generator function:

def generator_function():
    for i in range(10):
        yield i
# for item in generator_function():
#     print(item)

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a ,b = b,a + b
# for x in fibon(100):
#         print(x)
#         print()

# This way we would not have to worry about it using a lot of resources. However, if
# we would have implemented it like this
def fibon2(n):
    a = b = 1
    result =[]
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result
# It would have used up all our resources while calculating a large input.


# 字符串是可迭代的
# int不可迭代
# As we can see that after yielding all the values next() caused a StopIteration error.
# Basically this error informs us that all the values have been yielded. You might be
# wondering that why don’t we get this error while using a for loop? Well the answer
# is simple. The for loop automatically catches this error and stops calling next. Do you
# know that a few built-in data types in Python also support iteration?
my_string ="Yassoob"
my_iter = iter(my_string)
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# print(next(my_iter))
# 4.1 Map
# Map applies a function to all the items in an input_list here is the blueprint:
# BluePrint
# map(function_to_apply, list_of_inputs)
# Most of the times we want to pass all the list
# elements to a function one-by-one and then
# collect the output ,for instance:
"""""
items = [1,2,3,4,5]
squared=[]
for i in items:
    squared.append(i**2)
Map allows us to implement this in a much simpler and nicer way ,here you go :
"""
"""
items =[1,2,3,4,5]
squared = list(map(lambda x:x**2,items))
print(squared)
"""
# Most of the times we use lambdas with map so
# I did the same ,Instead of a list of inputs we can
# even have a list of functions


def multiply(x):
    return (x*x)
def add(x):
    return (3*x)
func = [multiply,add]
for i in range(5):
    value = list(map(lambda x:x(i),func))
    # print(value)
# 4.2 Filter
"""
As the name suggests ,filter creates a list of
elements for which a function returns true.
Here is a short and concise example:
"""
number_list = range(-5,5)
less_than_zero=list(filter(lambda x:x>0,number_list))
# print(less_than_zero)
# output:[1, 2, 3, 4]
# The filter resembles a for loop but it is a builtin function  and faster.

# 4.3 reduce
from functools import reduce
product = reduce((lambda x,y:x*y),[1,2,3,4])
# print(product)
# output:24

# 5. set Data Structure
"""
Set is a really useful data structure ,sets behave mostly like
lists with the dictinction that they can not contains
duplicate values ,it is really userful in a lot of cases
For instance you might want to check whether there are duplicates
in a list or not ,The first one involes using a for loop
something like this:
"""
some_list=['a','b','c','b','d','m','n','n']
print(some_list)
duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)
# print(duplicates)

# But there is a simpler and more elegant solution invoing sets
#  you can simply do something like this:
duplicates = set([x for x in some_list if some_list.count(x)>1])
# print("duplicate:")
# print(duplicates)
duplicates = set([x for x in some_list if some_list.count(x)==1])
# print(duplicates)

# Intersection

# You can intersect two sets ,For Instance:
valid  = set(['yellow','red','blue','green','black'])
input_set = set(['red','brown'])
# print(input_set.intersection(valid))

# Difference

# You can find the invalid values in the above example using the difference method
# For example:
# print(input_set.difference(valid))
is_fat = True
state='fat' if is_fat else "not fat"
# print(state)
fat = True
fitness=("skinny","fat")[fat]
# print("Ali is ",fitness)
