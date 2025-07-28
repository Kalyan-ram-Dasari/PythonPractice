# Pattrens 

# for row in range(5):
#     for col in range(5):
#         print("*",end=' ')
#     print()    

# n = int(input("enter the size "))
# for i in range(n):
#     for j in range(n):
#         print("*",end=' ')
#     print()
   
'''
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''       


# n = int(input("enter the size "))
# for i in range(n):
#     for j in range(n):
#         print(j,end=' ')
#     print()


'''
enter the size 5
0 1 2 3 4 
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
0 1 2 3 4
'''


# n = int(input("enter the size "))
# for row in range(n):
#     for col in range(row+1):
#         print("*",end=' ')
#     print()
    
    
'''
enter the size 10
0 
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9
'''


# n = int(input("enter the size "))
# for row in range(n):
#     for col in range(n-row):
#         print("*",end=' ')
#     print()
 
 
'''
enter the size 5
* * * * * 
* * * *
* * *
* *
*
''' 

# n = int(input("enter the size "))
# for row in range(n):
#     for spc in range(n-row-1):
#         print(" ",end=' ')
#     for col in range(row+1):
#         print("*",end=' ')
#     print()

'''
enter the size 5
        * 
      * *
    * * *
  * * * *
* * * * *
'''


# n = int(input("enter the size "))
# for row in range(n):
#     for spc in range(row):
#         print(" ",end=' ')
#     for col in range(n-row):
#         print("*",end=' ')
#     print()


'''
enter the size 5
* * * * * 
  * * * *
    * * *
      * *
        *
'''    


# n = int(input("enter the size : "))
# for row in range(n):
#     if row<=n//2:
#       for col1 in range(row+1):
#         print("*", end = ' ')
#     else:
#        for col2 in range(n-row):
#           print("*",end=' ')
#     print()   
    
    
'''
* 
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * *
* * * *
* * *
* *
*
'''        



# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if row==0 or col == 0 or row==n-1 or col==n-1 :
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print()       
  
'''
enter size : 5
* * * * * 
*       *
*       *
*       *
* * * * *
'''  
# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if row==0 or col == 0 or row==n-1 or col==n-1 or row==n//2 :
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print()  


'''enter size : 5
* * * * * 
*       *
* * * * *
*       *
* * * * *
  '''


# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if row==0 or col == 0 or row==n-1 or col==n-1 or row==n//2 or col==n//2:
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print() 
  
  
'''
enter size : 5
* * * * * 
*   *   *
* * * * *
*   *   *
* * * * *
'''  

# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if row==0 or row==n-1 or col == n-row-1:
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print() 




# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if row==0 or row==n-1 or col+row==n-1:
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print() 
'''
enter size : 5
* * * * * 
      *
    *
  *
* * * * *
'''  


# n = int(input("enter size : "))
# for row in range(n):
#   for col in range(n):
#     if  col+row==n-1 or col == row:
#       print("*",end=' ')
#     else:
#       print(' ',end=' ')
#   print() 

'''
enter size : 5
*       * 
  *   *
    *
  *   *
*       *
'''






