# #1. positive and negative numbers

# num = int(input("Enter a number:"))
# if num > 0:
#     print("The number is positive.")
# else:
#     print("The number is negative") 
    
# #2. Even or odd

# num = input("Enter the number ")
# if num.isdigit():
#     num = int(num)
#     if num%2==0:
#       print(f"{num} is even number")
#     else:
#        print(f"{num} is odd number") 
# else :
#     print(f"{num} is not a number")       
              
# #3. Divisible by 5 or not              
# num = input("Enter a number Divisibel by 5 : ")
# if num.isdigit():
#     num = int(num)
#     if num %5==0:
#         print(f"{num} is divisible by 5")
#     else:
#         print(f"{num} is not divisible by 5")
# else:
#     print(f"{num} is not a expected input")
                              
# 4. Divisible by 3 and 7
# num = input("Enter a number divisible by 3 and 7 : ")
# if num.isdigit():
#     num = int(num)
#     if num %3==0 and num %7==0:
#         print(num," is divisible by 3 & 7 ")
#     else:
#         print(f"{num} is not divisible by 3 and 7")
# else:
#     print(f"{num} is expected input")                                          
  
  
#5.Check leap year
# year = input("Enter the year : ")
# if year.isdigit():
#     year = int(year)
#     if (year % 4 ==0 and year % 100 != 0) or (year % 400==0):
#         print(f"{year} is Leap year")
#     else:
#         print(f"{year} is not a Leap year")
# else:
#     print("{year} is expected input")   


#6. check if marks is >40 pass or fail
# marks = input("Enter the Marks : ")
# if marks.isdigit():
#     marks = int(marks)
#     if marks >= 40:
#         print(f"Congrats You have secured {marks} and your pass")
#     else:
#         print(f"{marks} is Fail, Better luck next time")
# else:
#     print("Invalid input")      


# 7. Check if number is 3 digit or not
# len_num = 3
# num = input("Enter a number : ") 
# if num.isdigit(): 
#     if len(num) == len_num:
#         print(f"{num} is a 3 digit number")
#     else:
#         print(f"{num} is not a 3 digit number")   
# else:
#      print("Invalid input")



#8. Check if character is vowel  

# vowels = ['a','e','i','o','u']
# char = input("enter the char : ".lower())
# if char in vowels:
#     print(f"{char} is vowel character")
# else:
#     print(f"{char} is not a vowel character")                   


# #9. Check greatest of two numbers

# num1,num2 = map(int,input("enter a number").split())
# print("Number one is : ",num1)
# print("Number two is : ",num2)
# if num1 > num2:
#     print(f"{num1} is greatest number ")
# else:
#      print(f"{num2} is greatest number ")   


#9. Check Smallest of two numbers

# num1,num2 = map(int,input("enter a number").split())
# print("Number one is : ",num1)
# print("Number two is : ",num2)
# if num1 < num2:
#     print(f"{num1} is Smallest number ")
# else:
#      print(f"{num2} is Smallest number ")  
    