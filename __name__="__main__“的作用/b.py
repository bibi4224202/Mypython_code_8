import a

b = 200

print('你好，我是模块B……')

print('模块B中__name__的值：{}'.format(__name__))

print(b)

#if __name__="__main__"解析，当哪个模块被直接执行时，该模块“__name__”的值就是“__main__”，当被导入另一模块时，“__name__”的值就是模块的真实名称。
#在b导入模块a时，模块a  __name__的值是:a,模块b  __name__的值是：__main__.
