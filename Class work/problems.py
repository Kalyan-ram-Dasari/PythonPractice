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

l = [1,2,3,8,9,10,6,5,7]

s=0
for i in l:
    s = s+i

n=10
sn = (n*(n+1))/2
print(sn)
Missing = s - sn
print(Missing)
