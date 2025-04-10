def use_name(name,age=18):
    print(f"name:{name}\nage:{age}")
use_name("ybc",18)

#关键词实参：
use_name(age=30,name='bob')
#默认值
use_name('lili')
#传递任意数量实参，形参得到一个元组：
def age(*num):
    print(num)
    for i in num:
        print(-i)

age(1,2,3,4)
#使用任意关键词实参,形参user为字典

def abc(a,b,**user):
    user['a']=a
    user['b']=b
    return user
print(abc(1, 2,d=4,f=6))

#function函数调用方法kehu.py里面有函数use_name(),从另一python文件中导入：
'''
1  import kehu
2  from kehu import * 有可能函数和变量重名
3  from kehu import use_name
4  from kehu import use_name,use_age 导入多个函数
5  from kehu import use_name as us
6  import kehu as kh

'''
