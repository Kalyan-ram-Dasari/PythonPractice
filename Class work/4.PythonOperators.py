#4.python Operators

#1. Arithmetic Operators

print("Arithmetic Operators" )
print()

a = 10
b = 5
print("Addition :" , a + b)  # output Addition(a+b):15
print()
print("Subtraction :" , a - b) #output Subtraction(a-b):5
print()
print("Multiplication :" , a * b)  # output Multiplication(a*b):50  
print()
print("Division :" , a / b) #output Division(a/b):2.0
print()
print("Modulus :" , a % b) #output modulus(a%b):0
print()
print("Exponentiation :" , a ** b) #output Exponentiation(a**b):100000
print()
print("Floor Division :" , a // b)# output FloorDivision(a//b):2



#2. Comparison Operators 

print("Comparison Operators")
print()

print("Equal to :" , a == b) #output Equal to(a==b):False
print()
print("Not Equal to :" , a != b) #output Not Equal to(a!=b):True
print()
print("Greater than : ",a>b) #output Greater than(a>b):True
print()
print("Less than : " , a<b)# outpput Lessthan(a<b):Flase
print()
print("Greater than or Equal to : ",a>=b)# output Greater than or Equal to(a>=b):True
print()
print("Less than or Equal to : ", a<=b) #output Less than or Equal to(a<=b):False

#3. Assignment Operators

print("Assignment Operators")
print()
x = 20
print("x",x) #Assignment Operators(x=20)
print()
print("Addition Assignment : ", x + 5) #output Addition Assignment(x+=5):25
print()
print("Subtraction Assignment : ", x - 5) #output Subtraction Assignment(x-=5):15
print()
print("Multiplication Assigmenet: ", x*5) #output Multiplication Assignment(x*=5):100
print()
print("Division Assignment : ", x / 5) #output Division Assignment(x/=5):4.0
print()
print("Floor Division Assignment : ", x // 5) #output Floor Division Assignment(x//=5):4
print()
print("Modulus Assignment : ", x % 5) #output Modulus Assignment(x%=5):0
print()
print("Exponentiation Assignment : ", x ** 2) #output Exponentiation Assignment(x**=2):400

#4. Logical Operators
print("Logical Operators")
print()

a = 10
b = 5
print("Logical AND : ", a > 5 and b < 10) #output Logical AND(a>5 and b<10):True
print()
print("Logical OR : ", a > 5 or b > 10) #output Logical OR(a>5 or b>10):True
print()
print("Logical NOT : ", not(a > 5)) #output Logical NOT(not(a>5)):False
print(a%2==0) #output True if a is even, False if odd
print(b%2==0) #output True if b is even, False if odd
print(a %2==0 and b%3==0) 
print(a %2==0 or b%3==0)
print(a %2==0 != b%3==0) 

#5.   Membership Operators
print("Membership Operators")
print()
str = "kalyan ram"
l = [1, 2, 3]
k = [1,2,3]
t = (1, 2, 3)
s = {1,2,3,4,5,6,7,8,9,10}
data = {"name" : "kalyan", "Batch" : "PFS31", "city" : "Hyderabad"}
print("kal is in s", "kal" in str) # output True if "kal" is in str, False otherwise   True
print("hari is not in s", "hari" not in str) # output True if "hari" is not in str, False otherwise  True
print()
print("one is there in l :",1 in l) # output True 
print("four is not there in l :", 4 in l) # output False
print("one is there check using not:", 1 not in l) # output False
print("check using l and k", 1 in k and 1 in l)# output True  
print()
print("one is there in t :",1 in t)# output True
print("four is not there in t : ", 4 in t)# output True False
print("one is there check using not : ", 1 not in t) # output False 
print()
print("two is there in s:", 2 in s) # output True
print("four is not there in s:", 4 not in s)# output False
print()
print("name is there in data :  ", "name" in data)# output True
print() 
#6. Identity Operators
print("Identity Operators")
print()
a = 10
b = 10
print("a is b :", a is b) # output True 
print("a is not b :", a is not b) # output False
print()

print(id(a)) # output the identity of a is 140724689828568
print(id(b)) # output the identity of b is 140724689828568
print("a is b :", a is b) # output True 
a1 = a
print("a1 is a :", a1 is a) # output True 
print("a1 is not a :", a1 is not a) # output False  
print(id(a1)) # output the identity of a1 is 140724689828568
a2 = a1
print("a2 is a1 :", a2 is a1) # output True  
print(id(a2)) # output the identity of a2 is 140724689828568   


#7. Bitwise Operators
print("Bitwise Operators")
print()
a = 10  # 1010 in binary
b = 4   # 0100 in binary
print("Bitwise AND :", a & b)  # output Bitwise AND(a&b):0
print()
print("Bitwise OR :", a | b)   # output Bitwise OR(a|b):14
print()
print("Bitwise XOR :", a ^ b)  # output Bitwise XOR(a^b):14
print()
print("Bitwise NOT :", ~a)  # output Bitwise NOT(~a):-11
print()












