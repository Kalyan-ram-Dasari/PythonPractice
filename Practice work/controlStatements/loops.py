#1. Print Numbers from 1 to N (Using for loop)
# n = int(input("Enter number : "))
# for i in range(1,n+1):
#     print(i , end=" ")
    
#2. Print Even Numbers from 1 to N (Using for loop)
# n = int(input("Enter number : "))
# for i in range(1,n+1):
#     if i %2==0:
#         print(i, end=" ")


#3. Sum of Numbers from 1 to N (Using for loop)
# n =  int(input("enter numbers : "))
# total = 0
# for i in range(1,n+1):
#     total += i
# print(total)


#4. Print Odd Numbers from 1 to N (Using for loop)
# n = int(input("Enter number : "))
# for i in range(1,n+1):
#     if i %2 != 0:
#         print("Odd number : ",i)




#5. Find Factorial of a Number (Using for loop)
# n = int(input("Enter a number : " ))
# fact = 1
# for i in range(1,n+1):
#     fact = fact *i
# print(fact) 


#6. Print Multiplication Table of N (Using for loop)

# n = int(input("Enter number : "))
# for i in range(1,n+1):
#     print(f"{n} * {i} = {n*i}")   

#7. Check Prime Number (Using for loop)
# n = int(input("enter a number : "))
# c =  0
# for i in range(2,n):
#     if n % i == 0:
#         c += 1
#         break 
# if c == 0:
#     print("prime")
# else:
#     print("not a prime")     


#8. Sum of Digits of a Number (Using while loop)

# n = int(input("enter number : "))
# total = 0 
# while n < 0:
          
          
 # reverse a string 
n = input("enter value : ").split()
for i in n:
    i[::-1]==n
    print(i)
    
    
    
l = list(map(int,input().split()))
while 0 in l:
    l.remove(0)
print(l)        


n = input("enter value")
d = {}
for i in n:
    if i != " " or i not in d:
      d[i]=n.count(i)
print(d)    