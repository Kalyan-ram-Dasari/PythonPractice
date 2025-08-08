#1. Add Two Numbers

# a,b = map(int,input().split(" "))
# # print(a)
# # print(b)
# def add(a,b):
#     return a+b    
# print(add(a,b))    


#2. Square a Number
# a = int(input("Enter number : "))
# def sqr():
#     return a*a
# print(sqr())


#3. Area of a Circle
# Area = int(input("Enter area : "))
# def AreaOfCircle():
#     return 22/7 * (Area*Area)
# print(AreaOfCircle())


#4. Greet the User
# name = input("Enter the name : ")
# def greet(name):
#     return f"Hello, {name}"
# print(greet(name))


#5. 5. Convert Celsius to Fahrenheit

# Celsius = int(input("Enter Celsius : "))
# def fahrenheit():
#     return  (9/5 * Celsius) +32
# print(fahrenheit())    
    
#6. Multiply Three Numbers
# a,b,c = map(int,input("Enter Numbers : ").split())
# def prod():
#     return a*b*c
# print(prod())  


#7. Calculate Simple Interest
# principal , Rate, Time = map(int,input("Enter values : ").split())
# def Simple_interest():
#     return (principal * Rate * Time)/100
# print("Simple interest is : ",Simple_interest())


#8. Find Length of a String
# s = input("Enter value : ")
# def lengthOfStr():
#     return len(s)
# print(lengthOfStr())


#9. Append to a List
# l = [1,2,3]
# def appendList(l):
#     l.append(4)
#     return l
# print(appendList(l)) 



#10. Double Each Element in a List
# l = list(map(int,input("enter : ").split()))
# def double_append():
#     for i in range(len(l)):
#         l[i] = l[i]*2
#     return l
# print(double_append())    


#11. Sort a List
# l = list(input("enter vlaues : ").split())
# def sort_list(l):
#     return sorted(l)
    
# print(sort_list(l))


#12. Clear a List Inside Function

# l = list(input("Enter values : ").split())
# def clear_list():
#     l.clear()
#     return l
# print(clear_list())


#13. Update Dictionary Value
# d = eval(input("enter value : "))
# def dict_val(d):
#     k = input("enter key : ")
#     v = input("enter value : ") 
#     d[k] = v
#     return d
# print(dict_val(d))   


#14. Remove Element from List by Value
# l = list(input("Enter value : ").split())
# def remove_l(l):
#     val = input("enter value to remove ")
#     if val in l:
#         l.remove(val)  
#     else:
#         print(f"{val} is not found ")
#     return l 

# print(remove_l(l))   



#15. Add Key to Dictionary
# d = eval(input("Enter dict : "))
# def add_key(d):
#     k = input("enter key ")
#     v = input("enter value")
#     d[k]=v
#     return d
# print(add_key(d))  



#16. Increment All Values in Dictionary 

# d = eval(input("Enter values : "))
# def inc_dic(d):
#     for i in d:
#         d[i] +=1
#     return d
# print(inc_dic(d))    
          
           
#17. Factorial of a Number
# n = int(input("enter value : "))
# def fact(n):
#     f =1
#     for i in range(1,n+1):
#         f = f*i
#     return f
# print(fact(n)) 



#19. Sum of First N Natural Numbers
# n = int(input("Enter number : "))
# def sumOfNum(n):
#     s = 0
#     for i in range(1,n+1):
#         s+= i
#     return s
# print(sumOfNum(n)) 


#20. Reverse a String Using Recursion


#25. Maximum of Three Numbers Using max()

# n = list(map(int, input("Enter values: ").split()))

# def max_val(n):
#     return max(n)

# print("Maximum value is:", max_val(n))


#26. Sort a List Using sorted()
# l = list(input("enter value : ").split())
# def sort_l(l):
#     return sorted(l)
   
# print(sort_l(l))



#27. Sum of Elements Using sum()


# s = list(map(int, input("Enter numbers separated by space: ").split()))

# def sumOfEle(s):
#     return sum(s)

# print("Sum of elements:", sumOfEle(s))


#29. Print Even Numbers up to N
# n = int(input("enter number : "))
# def even_num(n):
#     evens = []
#     for i in range( n+1):
#         if i%2==0:
#             evens.append(i)
#     return evens    
# print(even_num(n))        


#30. Return List of Squares
# n = list(map(int, input("Enter numbers separated by space: ").split()))
# def sqr(n):
#     for i in range(len(n)):
#         n[i] = n[i]**2
#     return n
# print(sqr(n))   


#31. Check if Number is Prime

# n = int(input("Enter number: "))

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2,n//2):
#         if n % i == 0:
#             return False
#     return True

# print("Is prime?", is_prime(n))


#32. Count Vowels in a String

# s = input("Enter string ")
# def vol(s):
#     c = 0
#     for i in range(len(s)):
#       if s[i] in "aeiouAEIOU":
#           c+=1
#     return c 
# print(vol(s))    

  
          
        

            
     
                            