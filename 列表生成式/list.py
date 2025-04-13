#列表生成式。lis=[表达式 for 循环 if 语句]
list4 = [i ** 2 for i in range(1, 10) ]
print(list4)

list8 = [i + j for i in "abc" for j in "xyz"]
print(list8)

dict1 = {'a': 10, 'b': 20, 'c': 30}
# 方式一：传统方式
list9 = []
for key, value in dict1.items():
    list9.append(str(key) + str(value))
print(list9)
# 方式二：使用列表生成式
list10 = [key + str(value) for key, value in dict1.items()]
print(list10)

list_1 = ['hello', 10, 'Abc', 'asBd', True]
# 方式一：
newlist_1 = []
for s in list_1:
    if isinstance(s, str):  # isinstance()来判断是不是str类型
        newlist_1.append(s.upper())
print(newlist_1)
# 方式二：
newlist_2 = [s.upper() for s in list_1 if isinstance(s, str)]
print(newlist_2)
