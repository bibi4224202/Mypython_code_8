#列表有sort()和 reverse（）,而字符串没有
l='asdbfgh'
p=list(l)
p.sort(reverse=True)
#p.reverse()
print(p)

#字符串的反转，用列表奥切片
l='asdbfgh'
p=l[::-1]
print(p)

