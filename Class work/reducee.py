from functools import reduce

l = [1,2,3,4]
sum1 = reduce(lambda s,a:s+a,l)
print("reduce",sum1)


s = {'python','html','css','java','mysql'}
names = reduce(lambda n,name :n + " "+ name,s)
print(names)


# t = (1,2,3,4,5)
# product = reduce(lambda pro,item : item:pro*item,t)
# print(product)


d = {'mysql':90,'python':80,'java':70,'html':80}
sumup = reduce(lambda s,i:s+)