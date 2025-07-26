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
# n = input("enter value : ").split()
# for i in n:
#     i[::-1]==n
#     print(i)
    
    
    
# l = list(map(int,input().split()))
# while 0 in l:
#     l.remove(0)
# print(l)        


# n = input("enter value")
# d = {}
# for i in n:
#     if i != " " or i not in d:
#       d[i]=n.count(i)
# print(d)  


#10. Count Numbers Divisible by 3 (Using for loop)

# n = int(input("enter number : "))
# count = 0
# for i in range(1,n+1):
#     if i%3==0 :
#         count+=1
# print(count) 


#11. Check if a Number is Palindrome (Using while loop)

# n = int(input("enter value : "))
# temp = n
# rev = 0
# while n>0:
#     rev = rev*10+(n%10)
#     n//10
# if rev == temp:
#     print("Palindrome")
# else:
#     print("Not a Palindrome ")   


#12. Print Multiples of 5 up to N (Using for loop)

# n = int(input("enter number : "))
# c = 0
# for i in range(1,n+1):
#     if i%5==0 :
#         print(i)
#         c+=1
# print("total count is ",c)  



#13. Find the Maximum of Three Numbers (Using for loop)

# a = list(map(int,input("enter values ").split()))
# greater = 0
# if len(a)!=3:
#     print("enter three numbers ")
# else:
#     greater = a[0]
#     for i in a:
#         if greater < i:
#             greater= i
#     print(greater)     
    
    
#14. Print Reverse of a Number (Using while loop)

# n = int(input("Enter number: "))
# temp = n
# rev = 0
# while n>0 :
#     rev = rev*10+(n%10)
#     n = n//10
    
# print(rev) 


#15. Sum of First N Natural Numbers (Using for loop)

# n = int(input("enter number : "))

# s = 0
# for i in range(1,n+1):
#     s+=i
# print(s)   



#16. Print Numbers from N to 1 (Using while loop)

# n = int(input("Enter number: "))

# while n >= 1:
#     print(n)
#     n -= 1


#17. Find Sum of Prime Numbers up to N (Using for loop)

# n = int(input("Enter number: "))
# s = 0

# for i in range(2, n + 1):  # Check all numbers from 2 to n
#     is_prime = True        # Assume i is prime
#     for j in range(2, i):  # Check if i is divisible by any number from 2 to i-1
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         s += i             # Add prime number to sum

# print("Sum of prime numbers up to", n, "is:", s)




n = int(input("Enter number: "))
s = 0
# for i in range(2, n+1):
#     c = 0
#     for j in range(1, i+1):
#         if i % j == 0:
#             c += 1
#     if c == 2:
#         s += i

# print(s)

  
            
             



        
        
          
           
               
          

