def update(n):
    return n+10

print(update(20))

u = lambda n : n+10
#var = lambda para/argv : Exp

print(u(10))
print(u(20))


cube = lambda n:n**3
print(cube(5))

s = lambda s:s[0]
print(s("python"))


add = lambda a,b : a+b
print(add(10,20))
print(add(100,20))


greater = lambda a,b :  a if a>b else b
print(greater(10,20))
print(greater(30,50))

evenorodd = lambda n: "Even" if n%2==0 else "odd"
print(evenorodd(15))

sumofnum = lambda a,b,c :a+b+c
print(sumofnum(30,10,22))


#map,filter,reduce

s = 'python programming'
changestr = list(map(lambda i :i.upper(),s))
print(changestr)

asci = list(map(lambda i : ord(i),s))
print(asci)


vol = 'aeiouAEIOU'
frmt = list(map(lambda i : "*" if i in vol else "0",s))
print(frmt)


vol = 'aeiouAEIOU'
frmt = list(map(lambda i : "*" if i in vol else i,s))
print(frmt)


l =  [1,2,3,4,5,6,7,8,9,10]
lstup = list(map(lambda i: i+1,l))
print(lstup)

#filter 
elst = list(filter(lambda i: i%2==0,l))
print(elst)

t = (20,40,30,50,12,34,24,89)
tupup = tuple(map(lambda i:i//10,t ))
print(tupup)


#filter 
divtup = tuple(filter(lambda i : i%10==0,t))
print("using filter : ",divtup)



s = {'python','html','css','java','mysql'}
setup = set(map(lambda i :i.upper(),s))
print(setup)


stset = set(filter(lambda i:i.startswith('p'),s))
print("startswith : ",stset)

# d = {1:"afrin",2:"ramya",3:"keerthana",4:"revathi",5:"sunitha"}
# dup = dict(map(lambda i:d[i].title(),d))
# print(dup)

prod = {'mouse':10,'keyboard':0,'laptop':30,'phone':0,'charger':13}
proddisplay = list(filter(lambda i : prod))
#filter 

vol = 'aeoiuAEOIU'
frmt = list(filter(lambda i: i in vol,s))
print(frmt)