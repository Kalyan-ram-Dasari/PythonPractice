# from collections import deque,defaultdict,Counter

from datetime import date,time,datetime,timedelta

# s = "hello world "
# d={}
# for i in s:
#     if i in d:
#         d[i] +=1
#     else:
#         d[i]=1
# print(d)


# feq = Counter(s)
# print(feq)   


# l = [1,2,3,4,5,5,4,3,2,17,8,0]
# feq = Counter(l)
# print(feq)   

# s= {1:0,2:0,3:0,4:1}
# d = defaultdict(int)
# for i in s:
#     d[i]+=1
# print(d)


# |   |
# |   |
# |   |
# |   |
# |   |
# _ _ _   ----> Que

# ------------  ---> stack


# l = []
# l.append(12)
# 1.append(13)
# l.pop()


# d = deque()
# d.appendleft(12)
# d.pop()

# d.append(12)
# d.popleft()
# print(d)


'''
     ----------------
IN       65432        OUT
     ----------------

'''

'''
     ----------------
OUT     123456        IN
     ----------------

'''


today = date.today()

print(today)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday)
print(today.isoweekday)

print(date(2019,2,3))

print(time(3,5,33))


now = datetime.now()
print(now)
print(now.year)
print(now.day)
print(now.hour)


print(now.strftime('%y-%m-%d'))
print(now.strftime('%B %d, %Y %H:%M:%S %p'))  #August 13, 2025 14:41:56 PM



future = today + timedelta(days=10)
print(future)

future = today - timedelta(days=10)
print(future)


future = today - timedelta(weeks=1)
print(future)

future = now  + timedelta(minutes=30)
print(future)


    
          