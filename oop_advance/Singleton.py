#encoding='utf-8'
class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
obj1 = Singleton()
obj2 = Singleton()
print(obj1 == obj2)

