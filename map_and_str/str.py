map函数的原型是map(function, iterable, …)，它的返回结果是一个列表。

参数function传的是一个函数名，可以是python内置的，也可以是自定义的。
参数iterable传的是一个可以迭代的对象，例如列表，元组，字符串这样的。
map(str, iterable)
a=(1,2,3,4,5)
b=[1,2,3,4,5]
c="zhangkang"

la=map(str,a)#得到的是对象，用for 循环才能得到里面的元素。
lb=map(str,b)#
lc=map(str,c)#

print(la)#得到的是对象，内存地址
print(lb)
print(lc)

la=list(map(str,a))#把对象转为列表
la = [str(x) for x in a]#列表表达式
str()可以把数据、元组、列表、字典变为一个字符串。
