#prime number
# n = int(input("enter num : "))
# c=0        
# for i in range(2,n):
#     if n%i==0:
#         c+=1
# if c=0:
#     print("prime")
# else:
#     print("not prime")   

                 
# for i in range(2,n//2+1):
#     if n%i==0:
#         c=1
#         break
# if c==0:
#     print("prime")
# else:
#     print("not prime") 



# isprime = False
# for i in range(2,n//2):
#     if n%i==0:
#         isprime = True
#         break
# if isprime:
#     print("not a prime")
# else:
#     print("prime number")       




#factorial 

# n = int(input("enter a number : "))
# fact = 1
# for i in range(1, n+1):
#     fact = fact*i
# print(f"{n}! = {fact}")    


#sum of numbers

# n = int(input("enter number"))
# summ = 0
# for i in range(1,n+1):
#     summ += i 
# print(f"for {n} sum is {summ}")    


#missing number 

# l = [1,2,3,8,9,10,6,5,7]

# s=0
# for i in l:
#     s = s+i

# n=10
# sn = (n*(n+1))/2
# print(sn)
# Missing = s - sn
# print(Missing)



#Second highest
# l = [2, 3, 40, 23, 45, 10, 60, 35]
# f = l[0]
# s = None

# for i in range(1, len(l)):
#     if f < l[i]:
#         s = f
#         f = l[i]
#     else:
#         if s is None or s < l[i]:
#             s = l[i]
#     print(f"Step {i}: Current element = {l[i]}, f = {f}, s = {s}")

# print(f"\nFinal first max (f) = {f}")
# print(f"Final second max (s) = {s}")



# l = [2, 3, 40, 23, 45, 10, 60, 35]
# f = l[0]
# for i in range(1,len(l)):
#     if f<l[i]:
#         f=l[i]
# print(f)  



#first least number 
# l = [2, 3, 40, 23,1, 45, 10, 60, 35]
# f = l[0]
# for i in range(1,len(l)):
#     if f>l[i]:
#         f=l[i]
# print(f) 


#Second least
l = [2, 3, 40, 23, 45, 10, 60, 35]
f = l[0]
s = None

for i in range(1, len(l)):
    if f > l[i]:
        s = f
        f = l[i]
    else:
        if s is None or s > l[i]:
            s = l[i]
    print(f"Step {i}: Current element = {l[i]}, f = {f}, s = {s}")
print(f"\nFinal first min (f) = {f}")
print(f"Final second min (s) = {s}")



l = [2, 3, 40, 23, 45, 10, 60, 35]
for i in range(len(l)//2):
    l[i],l[len(l)-1-i] = l[len(l)-1-i] ,l[i]
print(l)        
