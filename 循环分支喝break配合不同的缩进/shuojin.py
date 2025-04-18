#if  else不同的缩进，求输入两个数间所有的素数
min=eval(input("min"))
max=eval(input('max'))


for num in range(min+1,max):

    if num>1:

            for j in range(2,num):
                if num%j==0:

                   break
            else:
                print(num)
