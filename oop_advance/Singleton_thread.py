#encoding='utf-8'
import threading
def synchronized(func):
    func.__lock__ = threading.Lock()
    def lock_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)
    return lock_func
class Singleton(object):
    instance = None
    @synchronized
    def __new__(cls, *args, **kwargs):
        """
        :type kwargs:object
        """
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self, num):
        self.a = num + 5
    def printf(self):
        print(self.a)
    
a = Singleton(3)
a.printf()
print(id(a))
b = Singleton(4)
b.printf()
print(id(b))

"""
 下面分析一下上段代码，看不懂装饰器的去我上一篇博文去看。这里我们先忽略装饰器，先看类，可以看出这里我们先定义了一个类属性instance，接着我们重写了父类的__new__方法，这个方法就是我们在实例化一个对象时最先调用的一个方法。和其他静态语言不一样，其他静态语言，直接调用了构造方法，一般情况下初始化的程序也写在构造方法之中。而python实例化一个对象和初始化是分开的。__new__是类方法，__init__是实例方法，也就是说，__init__是在对象已经创建完成之后，才执行。

   在python3中，调用父类的方法是用super()来调用。所以我们这里的思路就是，还是用父类的方法去创造，但是我们要加一个判断，就是说，当这个对象也就是类属性并不为空的时候，我们就不在实例化，而是返回一个已经实例化的类属性。

  那么这里思考一个问题，如果就这样可以吗，答案是可以的，但是这种不具备通用性，多线程的时候依然会造成实例化出几对象。所以再做项目时，一定要考虑这种情况。所以我们这里通过锁来进行保护，保证多线程的情况下同一时刻只有一个线程访问，这就保证了单例模式的安全。

   怎么验证呢，代码也有体现，id方法是内置方法，作用是打印对象的引用地址。运行结果如下：
--------------------- 
作者：抱剑观花一书生 
来源：CSDN 
原文：https://blog.csdn.net/qq_33324878/article/details/81170736 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""