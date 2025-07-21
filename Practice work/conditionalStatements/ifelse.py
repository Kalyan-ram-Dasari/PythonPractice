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

#11. Check if number is zero

# num = input("enter number : ")
# if num.isdigit():
#   num = int(num)  
#   if num == 0 :
#     print(f"{num},Number is Zero")
#   else:
#     print(f"{num} is  not zero")    
# else:
#     print("Invalid Input") 
    
    
#12. Check if number is multiple of 10
# num = input("enter number : ")
# if num.isdigit():
#     num = int(num)
#     if num %10==0:
#         print(f"{num} is divisible by 10")  
#     else:
#         print(f"{num} is not divisible by 10")
# else:
#     print("Invalid input") 


#13. Check if age is eligible to vote (18+)

# age = int(input("Enter age : "))
# if age >=18:
#     print(f"your age is {age}, so you are eligible to vote")
# else:
#    print(f"your age is {age}, so you are not eligible to vote")       
   
   
#14. Check if number is between 1 and 100
# num = int(input("enter number range between 1 to 100 : "))
# if num >0 and num<=100:
#     print(f"your entered number is {num} is between 1 to 100")   
# else:
#     print(f"your entered number is {num} is not between 1 to 100")  


#15. Check if number is square of another

# a,b = map(int,input("Enter number : ").split(" "))
# print("a value is : ",a)
# print("bvalue is : ",b)
# if a == b*b:
#     print(f"{a} is square of {b}")
# else:
#     print(f"{a} is not square of {b}")        


#16. Check if two strings are equal
# a,b = map(str,input("Enter String : ").split(" "))
# if a == b:
#     print(f"{a} is equal to {b}")
# else:
#     print(f"{a} is not equal to {b}")    
   
   
#17. Check if a number is prime (basic logic)
# num = int(input("enter numeber : "))
# if num <=1 :
#     print("not a prime number") 
# else:
#     is_prime = True
#     if num %2==0 and   


#18. Check if number is positive and even

# num = int(input("Enter number"))
# if num >0 and num %2==0:
#     print(f"{num} is even and positive number")
# else:
#     print(f"{num} is not even and positive")    
            
            
            
            
            
#19. Check if character is uppercase
# char = input("Enter character : ")
# if char.isupper():
#     print(f"{char} is a upper case")
# else:
#     print(f"{char} is not a upper case")     



#Check if temperature is hot (>30°C)

# temp = int(input("Enter Temperature : "))
# if temp >= 30:
#     print("It's hot")
# else:
#     print("It's cold")    



#1. Check if a number is a 4-digit even number

# num = input("enter a number : ")
# l_num = 4
# if num.isdigit():
#     if len(num) == l_num:
#         num = int(num)
#         if num %2==0:
#             print(f"{num} is a four digit number and even number")
#     else:
#        print(f"{num} is not a four digit number and even number")        
# else:
#     print("Invalid input")     


#2. Check if a character is a consonant

# l = ['a','e','i','o','u']

# char = input("enter character : ".lower())
# if char not in l:
#     print(f"{char} is consonant")  
# else:
#     print(f"{char} is not a consonant")  


#3. Check if a number is divisible by 2 or 3 but not both

# num = input("enter number : ")
# if num.isdigit():
#    num = int(num)
#    if num%2==0 and num%3==0:
#        print(f"{num} is divisible by both 2 and 3")
#    elif num%2==0  :
#        print(f"{num} is divisible by  2 only")
#    elif num%3==0:
#        print(f"{num} is divisible by  3 only")  
#    else:
#        print(f"{num} is not divisible by both 3 and 2")
# else:
#     print("Invalid Input")       
          
  
  
          
# 4. Check if a number is negative and odd          
# num = int(input("Enter number : "))
# if num <0 and num %2!=0:
#     print(f"{num} is odd and Negative number")
# else:
#     print(f"{num} is not odd and negative")  



#5. Check if a string starts with a vowel
# val = input("Enter value of string : ")
# t = ('a','e','i','o','u')

# if val.startswith(t):
#     print(f"{val} Starts with a vowel ")
# else:
#     print(f"{val} not starts with a vowel")    


#7. Find the greatest among three numbers

# a,b,c = map(int,input("enter three values : ").split(" "))
# print("a vlaue is ",a)
# print("b value is ",b)
# print("c values is ",c)
  
# if a >b and a>c:
#     print(f"{a} value is greater among all")
# elif b>a and b>c:
#   print(f"{a} value is greater among all")
# elif c>a and c>b:
#       print(f"{c} is the greatest among all")
# else:
#     print("Invalid input")


# 9. Check if a character is a digit
# num = input("enter the value : ")
# if num.isdigit():
#     print(f"{num} is a digit")
# else:
#     print(f"{num} is not a digit")   
    
    
#10. Check if a number is palindrome (integer)

# num = input("enter value : ")
# rev = int(str(num)[::-1])   
# if num == rev:
#     print("Palimdrone")
# else:
#     print("not a palimdrone")    



#11. Compare lengths of two strings
# str1 , str2 = map(str, input("enter strings values : ").split(" "))
# print(str1)
# print()
# print(str2)
# if len(str1) >len(str2):
#     print(f"{str1} is greater than {str2}")
# else:
#     print(f"{str2} is greater than {str1}")



#12. Check if a number is within a specific range (50 to 100) and divisible by 5

# num = int(input("enter a number : "))
# if num.isdigit():
#    num = int(num) 
#    if 50<=num <=100 and num%5==0:
#        print(f"the number is in range and divisible by 5 ")
#    else:
#       print(f"not satisfying the required input")
# else:
#     print("Invalid input")    


#13. Validate if a password length is strong (8 or more characters)
# password = input("Enter a password : ")
# if len(password)>8:
#     print(f" {password} is strong")
# else:
#     print(f"{password} is weak make sure to have length of 8")


#14. Check if sum of two numbers is even
# num1, num2 = map(int,input("enter two numbers : ").split(" "))
# print(num1)
# print(num2)
# ans = num1 + num2
# if ans %2==0:
#     print("it is even",ans)
# else:
#     print(ans,"not an even")    


#15. Check if the character is a special symbol (!, @, #, etc.)

# val = input("Enter a value : ")
# if val.isalnum():
#     print(f"{val} It is not a special symbol ")
# else:
#     print(f"{val} It is a special symbol") 



#16. Check if temperature is cold (<15°C), moderate (15–30°C), or hot (>30°C)
# c_temp = input("enter a temp : ")
# if c_temp.isdigit():
#     if c_temp < 15 :
#       c_temp = int(c_temp)  
#       print(f"{c_temp}, Its cold")  
#     elif 15>= c_temp <=30:
#       print(f"{c_temp}, it's moderate")
#     else :
#        print(f"{c_temp}, it's hot") 
# else:
#     print("Invalid input")   


#17. Check if a number lies outside the range 10 to 50

# num = int(input("enter num : "))
# if num >=10 and num <=50:
#     print(num, "it is in range")
# else:
#     print(num,"out of range")     



#18. Check if number is a perfect square (basic method)
# num = int(input("enter a num : "))
# num1 = num * num
# if num**2  == num1 :
#     print(f"{num} is a perfect square ")
# else:
#     print(f"{num} is not perfect square ")   


#19. Compare two ages and determine who is older or if same age

# per1, per2 = map(int,input("enter age of 2 persons : ").split(" "))
# print(per1) 
# print(per2)
# if per1 >per2:
#     print(f" Person 1 {per1} is older than person 2 {per2}")
# else:
#     print(f" Person 2 {per2} is older than person 1 {per1}")   


#20. Check if an angle is acute, right, or obtuse

# angle = int(input("Enter a angle : "))
# if 0<angle<90:
#     print(f"{angle} is an acute angle ")
# elif angle == 90:
#      print(f"{angle} is an right angle ")   
# elif angle>90 and angle<=180:
#     print(f"{angle} is an obtuse angle ")  
# else:
#     print("invalid input")   



#left with questions are 18,8, 17th in first 20     

# num = int(input("enter a number : "))
# for i in range(2,num):
#     if i %2==0:
#         print("Not a prime")
#         break
# else:
#     print("prime")        
   
   
# num = int(input()) 
# count =0
# if num >1:
#     for i in range(1,num+1):
#         if i %2==0:    #n%i==0
#             count += 1
#     if count == 2:
#         print("Prime")
#     else:
#         print("Not Prime")
        

                         
                         
                        
         
    
       
            




         
 