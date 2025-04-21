a=[1,2,3]
print(id(a))
b=a#b是a的别名，存储地址相同
print(id(b))

b.reverse()
print(b)
print(a)
