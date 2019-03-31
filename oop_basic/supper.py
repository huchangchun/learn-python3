#encoding=utf-8
class Animal(object):
    def __init__(self, name):
        self.name = name
    def greet(self):
        print("Hello ,I am %s",self.name)
class Dog(Animal):
    def greet(self):
        super().greet()
        super(Dog,self).greet()
        print("Wangwang...")
    
class Base(object):
    def __init__(self):
        print("enter Base")
        print("leave Base")

class A(Base):
    def __init__(self):
        print("enter A")
        super(A, self).__init__()
        print("leave A")

class B(Base):
    def __init__(self):
        print("enter B")
        super(B, self).__init__()
        print("leave B")

class C(A, B):
    def __init__(self):
        print("enter C")
        super(C, self).__init__()
        print ("leave C")
if __name__=="__main__":
    dog = Dog("heihei")
    dog.greet()
    #Hello ,I am %s heihei
    #Hello ,I am %s heihei    
    c = C()
    print(C.mro())
    """
    Wangwang...
    enter C
    enter A
    enter B
    enter Base
    leave Base
    leave B
    leave A
    leave C
    [<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class '__main__.Base'>, <class 'object'>]
    """
    """
    总的来说，一个类的 MRO 列表就是合并所有父类的 MRO 列表，并遵循以下三条原则：

子类永远在父类前面
如果有多个父类，会根据它们在列表中的顺序被检查
如果对下一个类存在两个合法的选择，选择第一个父类
super 原理
super 的工作原理如下：

def super(cls, inst):
    mro = inst.__class__.mro()
    return mro[mro.index(cls) + 1]
其中，cls 代表类，inst 代表实例，上面的代码做了两件事：

获取 inst 的 MRO 列表
查找 cls 在当前 MRO 列表中的 index, 并返回它的下一个类，即 mro[index + 1]
当你使用 super(cls, inst) 时，Python 会在 inst 的 MRO 列表上搜索 cls 的下一个类。

现在，让我们回到前面的例子。

首先看类 C 的 __init__ 方法：

super(C, self).__init__()
这里的 self 是当前 C 的实例，self.class.mro() 结果是：

[__main__.C, __main__.A, __main__.B, __main__.Base, object]
可以看到，C 的下一个类是 A，于是，跳到了 A 的 __init__，这时会打印出 enter A，并执行下面一行代码：

super(A, self).__init__()
注意，这里的 self 也是当前 C 的实例，MRO 列表跟上面是一样的，搜索 A 在 MRO 中的下一个类，发现是 B，于是，跳到了 B 的 __init__，这时会打印出 enter B，而不是 enter Base。

整个过程还是比较清晰的，关键是要理解 super 的工作方式，而不是想当然地认为 super 调用了父类的方法
    
    """