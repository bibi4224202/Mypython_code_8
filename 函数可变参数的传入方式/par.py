a={'q':1,'e':2}
def add(x,y,**z):
    return print(x,y,z)

b=add(1,2,**a)
#键不能是数字，只能是字符
#是b=add(1,2,q=1,e=2)而不是b=add(1,2,'q'=1,'e'=2)

def add(x,y,*z):
    return print(x,y,z)

b=add(1,2,'y','i')


或
a=(5,6,7)

def add(x,y,*z):
    return print(x,y,z)

b=add(1,2,*a)
