l=[(1,2),(3,4)]
for i in range(len(l)):

    l[i]='{}:{}'.format(l[i][0],l[i][1])
print(','.join(l))

#输出结果：1:2,3:4，有，分隔改为由：分隔
