#Type Conversion

# Converting int to types
x = 10
x1 = float(x)  # Convert int to float
print("Float:", ) # Output: Integer: 10.0
x2 = complex(x)
print("Complex:", x2) # Output: Complex: (10+0j)
x3 = str(x)
print("String:", x3) # Output: String: 10
x4 = bool(x)
print("Boolean:", x4) # Output: Boolean: True
# x5 = list(x)
# print("List:", x5) # Output: TypeError: 'int' object is not iterable
# x6 = tuple(x)
# print("Tuple:", x6) # Output: TypeError: 'int' object is not
# x7 = set(x)
# print("Set:", x7) # Output: TypeError: 'int' object is not iterable 
# x8 = dict(x)
# print("Dict:", x8) # Output: TypeError: 'int' object is not iterable

#Converting float to types
y= 10.5
y1 = int(y)  # Convert float to int
print("Integer:", y1) # Output: Integer: 10
y2 = complex(y)
print("Complex:", y2) # Output: Complex: (10.5+0j)
y3 = str(y)
print("String:", y3) # Output: String: 10.5
y4 = bool(y)
print("Boolean:", y4) # Output: Boolean: True
# y5 = list(y)
# print("List:", y5) # Output: TypeError: 'float' object is not iterable
# y6 = tuple(y)
# print("Tuple:", y6) # Output: TypeError: 'float' object is not iterable
# y7 = set(y)
# print("Set:", y7) # Output: TypeError: 'float' object is not iterable
# y8 = dict(y)
# print("Dict:", y8) # Output: TypeError: 'float' object is not iterable





# Converting complex to types
a = 10 + 5j
a1 = int(a.real)  # Convert complex to int (using real part)
print("Integer:", a1) # Output: Integer: 10
a2 = float(a.real)  # Convert complex to float (using real part)
print("Float:", a2) # Output: Float: 10.0
a3 = str(a)
print("String:", a3) # Output: String: (10+5j)
a4 = bool(a)
print("Boolean:", a4) # Output: Boolean: True
# a5 = list(a)
# print("List:", a5) # Output: TypeError: 'complex' object is not iterable
# a6 = tuple(a)
# print("Tuple:", a6) # Output: TypeError: 'complex' object is not iterable
# a7 = set(a)
# print("Set:", a7) # Output: TypeError: 'complex' object is not iterable
# a8 = dict(a)
# print("Dict:", a8) # Output: TypeError: 'complex' object is not iterable








# Converting string to types
s = "123"
s1 = int(s)  # Convert string to int
print("Integer:", s1) # Output: Integer: 123
s2 = float(s)  # Convert string to float
print("Float:", s2) # Output: Float: 123.0 
s3 = complex(s)
print("Complex:", s3) # Output: Complex: (123+0j)
s4 = bool(s)  # Non-empty string is True
print("Boolean:", s4) # Output: Boolean: True
s5 = list(s)  # Convert string to list of characters
print("List:", s5) # Output: List: ['1', '2', '3']
s6 = tuple(s)  # Convert string to tuple of characters
print("Tuple:", s6) # Output: Tuple: ('1', '2', '3')
s7 = set(s)  # Convert string to set of characters
print("Set:", s7) # Output: Set: {'1', '2', '3'}
# s8 = dict(s)  # Cannot convert string directly to dict        
# print("Dict:", s8) # Output: TypeError: 'str' object is not iterable


# Converting boolean to types
b = True
b1 = int(b)  # Convert boolean to int
print("Integer:", b1) # Output: Integer: 1
b2 = float(b)  # Convert boolean to float
print("Float:", b2) # Output: Float: 1.0
b3 = complex(b)  # Convert boolean to complex
print("Complex:", b3) # Output: Complex: (1+0j)
b4 = str(b)  # Convert boolean to string
print("String:", b4) # Output: String: True
b5 = list(str(b))  # Convert boolean to list of characters
print("List:", b5) # Output: List: ['T', 'r', 'u', 'e']
b6 = tuple(str(b))  # Convert boolean to tuple of characters
print("Tuple:", b6) # Output: Tuple: ('T', 'r', 'u', 'e')
b7 = set(str(b))  # Convert boolean to set of characters
print("Set:", b7) # Output: Set: {'T', 'r', 'u', 'e'}
# b8 = dict(b)  # Cannot convert boolean directly to dict   
# print("Dict:", b8) # Output: TypeError: 'bool' object is not iterable 



# Converting list to types
l = [1, 2, 3]
l1 = tuple(l)  # Convert list to tuple
print("Tuple:", l1) # Output: Tuple: (1, 2, 3)
l2 = set(l)  # Convert list to set
print("Set:",l2) # Output: Set: {1, 2, 3}
l3 = str(l)  # Convert list to string
print("String:", l3) # Output: String: [1, 2, 3]
l4 = bool(l)  # Non-empty list is True  
print("Boolean:", l4) # Output: Boolean: True
# l5 = int(l)  # Cannot convert list directly to int
# print("Integer:", l5) # Output: TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
# l6 = float(l)  # Cannot convert list directly to float
# print("Float:", l6) # Output: TypeError: float() argument must be a string or a number, not 'list'    
# l7 = complex(l)  # Cannot convert list directly to complex
# print("Complex:", l7) # Output: TypeError: complex() first argument must be a string or a number, not 'list'
# l8 = dict(l)  # Cannot convert list directly to dict
# print("Dict:", l8) # Output: TypeError: cannot convert dictionary update sequence to a sequence



# Converting tuple to types
t = (1, 2, 3)
t1 = list(t)  # Convert tuple to list
print("List:", t1) # Output: List: [1, 2, 3]
t2 = set(t)  # Convert tuple to set 
print("Set:", t2) # Output: Set: {1, 2, 3}
t3 = str(t)  # Convert tuple to string
print("String:", t3) # Output: String: (1, 2, 3)
t4 = bool(t)  # Non-empty tuple is True
print("Boolean:", t4) # Output: Boolean: True
# t5 = int(t)  # Cannot convert tuple directly to int
# print("Integer:", t5) # Output: TypeError: int() argument must be a string, a bytes-like object or a number, not 'tuple'
# t6 = float(t)  # Cannot convert tuple directly to float
# print("Float:", t6) # Output: TypeError: float() argument must be a string or a number, not 'tuple'
# t7 = complex(t)  # Cannot convert tuple directly to complex
# print("Complex:", t7) # Output: TypeError: complex() first argument must be a string or a number, not 'tuple'
# t8 = dict(t)  # Cannot convert tuple directly to dict
# print("Dict:", t8) # Output: TypeError: cannot convert dictionary update sequence to a sequence








# Converting set to types
s = {1, 2, 3}
s1 = list(s)  # Convert set to list
print("List:", s1) # Output: List: [1, 2, 3]
s2 = tuple(s)  # Convert set to tuple       
print("Tuple:", s2) # Output: Tuple: (1, 2, 3)
s3 = str(s)  # Convert set to string 
print("String:", s3) # Output: String: {1, 2, 3}
s4 = bool(s)  # Non-empty set is True
print("Boolean:", s4) # Output: Boolean: True
# s5 = int(s)  # Cannot convert set directly to int
# print("Integer:", s5) # Output: TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
# s6 = float(s)  # Cannot convert set directly to float
# print("Float:", s6) # Output: TypeError: float() argument must be a string or a number, not 'set'
# s7 = complex(s)  # Cannot convert set directly to complex 
# print("Complex:", s7) # Output: TypeError: complex() first argument must be a string or a number, not 'set'
# s8 = dict(s)  # Cannot convert set directly to dict
# print("Dict:", s8) # Output: TypeError: cannot convert dictionary update sequence to a sequence



# Converting dict to types
d = {'a': 1, 'b': 2}
d1 = list(d)  # Convert dict keys to list
print("List:", d1) # Output: List: ['a', 'b']
d2 = tuple(d)  # Convert dict keys to tuple
print("Tuple:", d2) # Output: Tuple: ('a', 'b')
d3 = str(d)  # Convert dict to string
print("String:", d3) # Output: String: {'a': 1, 'b': 2}
d4 = bool(d)  # Non-empty dict is True
print("Boolean:", d4) # Output: Boolean: True
# d5 = int(d)  # Cannot convert dict directly to int
# print("Integer:", d5) # Output: TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
# d6 = float(d)  # Cannot convert dict directly to float
# print("Float:", d6) # Output: TypeError: float() argument must be a string or a number, not 'dict'
# d7 = complex(d)  # Cannot convert dict directly to complex    
# print("Complex:", d7) # Output: TypeError: complex() first argument must be a string or a number, not 'dict'
# d8 = set(d)  # Cannot convert dict directly to set
# print("Set:", d8) # Output: TypeError: 'dict' object is not iterable



# input_string = input("Enter a string of numbers separated by spaces: ")
# l = list(map(int, input_string.split()))
# print("List of integers:", l) # Output: List of integers: [<list of integers>]



 
