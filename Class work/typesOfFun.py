# #Positional Agr 
# def function_name(arg1,arg2,arg3):
#     #block of code
#  function_name(val1,val2,val3)



# 2.key keyword Agr

# def function_name(agr1,agr2,agr3):
#     #block of code
#     function_name(agr1 = 'val1',agr3 = 'val2', agr2='val3')
    
# 3.Default Agr

# def function_name(agr1,agr2,agr3):
#     #block of code
#     function_name(val1,val2) 
#     function_name(val2,val1)
#     function_name(agr1,agr2,agr3)
 
 
 
 
# 3.Variable length

# def function_name(*agr):=>(tuple):
#     #block of code
# function_name(val1,val2) 
# function_name(val2,val1)
# function_name(agr1,agr2,agr3)    



# 4. 





#1.positional Agr 

# def student_details(name,rollno,marks,grade,course):
#     print("Name : ",name)
#     print("rollno : ",rollno)
#     print("marks : ",marks)
#     print("grade : ",grade)
#     print("course : ",course)
    
# name = input("name : ")
# rollno = int(input("roll no"))
# marks = int(input("Marks : "))
# grade = input("GRade : ")
# course = input("course : ")
# print(" Details are ".center(40,"*"))


# student_details(name, rollno, marks,grade,course)   

# student_details( rollno, grade,name,course,marks)  # the arg will pass to values as in order values     

# student_details( 22, grade,name,course,marks) 
  


#Keyword arg

# def student_details(name,rollno,marks,grade,course):
#     print("Name : ",name)
#     print("rollno : ",rollno)
#     print("marks : ",marks)
#     print("grade : ",grade)
#     print("course : ",course)
    
# name = input("name : ")
# rollno = int(input("roll no"))
# marks = int(input("Marks : "))
# grade = input("GRade : ")
# course = input("course : ")
# print(" Details are ".center(40,"*"))


# student_details(name=name, rollno=rollno, marks=marks,grade=grade,course=course)
# print()
# student_details(name= "kalyan", rollno=rollno, marks=22,grade=grade,course=course)





#3.Default 
# def student_details(name,rollno,course,marks=0,grade="F"):
#     print("Name : ",name)
#     print("rollno : ",rollno)
#     print("marks : ",marks)
#     print("grade : ",grade)
#     print("course : ",course)
    
# name = input("name : ")
# rollno = int(input("roll no"))
# marks = int(input("Marks : "))
# grade = input("GRade : ")
# course = input("course : ")
# print(" Details are ".center(40,"*"))


# student_details(name, rollno, marks,grade,course)
# print()



# def names(*stdnames):
#     for i in stdnames:
#         print(f"**{i.upper()}**")
# names("kalyan","adarsh","sai kumar")
# print()
# names("kalyan","ram")  



# def display_products(**prod):
#     print("\n Products and Prices : ")
#     for i in prod:
#         print(f"{i}: ${prod[i]}")
#         print()
#     print(prod)

# display_products(laptop = 60000,phone = 3500, watch = 1500,fridge = 200000)
# display_products(fashwash= 600,perfume = 2000, eyeline = "not available")

          




      