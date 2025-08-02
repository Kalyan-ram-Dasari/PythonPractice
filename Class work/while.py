# moves = 10
# winning = int(input("enter winning point"))
# while moves >0:
#     if moves == winning :
#       print("congrats!!! you won the game")
#       break
#     print(f"{moves} left. you have chancces are to win ")
#     moves-=1
#     print(f"{moves} left. you have chancces are to win ")
# else:
#     print("Game over. try again")    
    
    
    
# num = list(int(input("enter numbrs : ").split()))
# total = 0
# while num:
#     total = total +num  
#     print(total) 

# num = list(input("enter a number : "))
# s = 0
# i = 0
# while num >len(i):
#     s +=i
#     i+=1
# print(s)       


#5,4,3,2,1
# n = 5
# while n>0:
#     print(n)
#     n = n-1 


#3  6 9 12 15 18
# n = 3
# while n<19:
#     print(n)
#     n=n+3
    
# n = 1
# while n<10:
#     print(n*3)
#     n=n+1    
    
 
# l = [1,2,3,4,5]
# ind = 0
# total = 0
# while ind<len(l):
#     # print(l[ind])
#     total += l[ind]
#     ind += 1
# print(total)
#     # ind+=1

# num = list(map(int, input("Enter space-separated digits: ").split()))
# i = 0
# s=0
# while i<len(num):
#     s+=num[i]
#     i+=1
# print(s)


    
    
# n = int(input("enter value : ")) #121
# s=0
# while n>0:
#     s+=(n%10)
#     n//=10
# print(s)       #4



# n = int(input("enter value : "))
# s= 1
# while n>0:
#     s = n%10
#     n//=10
# if s == n:
#         print("palindrome")  



# n = 12134
# rev = 0


# rev = rev*10+4=4
# n = 1213

# rev = rev*10+3 = 43 
# n = 121

# rev = rev*10+1 = 431
# n = 12


# n = int(input("enter : "))
# temp = n
# rev = 0
# while n >0:
#   rev = rev*10+(n%10)
#   n//=10
# if rev == temp:
#     print("Palindrome")
# else:
#     print("not palindrome")    







n = input()
full = len(n)-1
length = len(n)//2
ind = 0

while ind <= length:
    if n[ind]==n[full]:
        pass
    else:
        print("not palindrome")
        break
    ind+=1
    full-=1
else:
    print("palindrome")    




n = input()
full = len(n)-1
length = len(n)//2
ind = 0

while ind <= length:
    if n[ind]==n[full]:
        print("not palindrome")
        break
    ind+=1
    full-=1
else:
    print("palindrome")  


    
 
    