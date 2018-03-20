a = [1,2,3]

b = [11,22,33]

c = [111,222,333]

var01 = [a,b,c]

var02 = var01

print(var01)

print(var02)

print(id(var01))  #id 获取变量在内存中的地址

print(id(var02))

print('-------------------------')

a.append(4)   # a插入一个新元素

print(var01)

print(var02)

print(id(var01))

print(id(var02))