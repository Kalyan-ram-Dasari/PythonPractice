#TUPLES 

# A tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Tuples are defined using parentheses () and can contain mixed data types. 
# Tuples are immutable, meaning they cannot be modified after creation.
# Tuples can contain elements of different data types, including other tuples.

# Empty Tuple
empty_tuple = ()

t = (5,)
print(t) # output (5,)

#2. Accessing Tuple Elements

t = (1, 2, 3, 4, 5, "kalyan", 3.14, True, False, {"key1": "val1", "key2": "val2"}, [1, 2, "k", "a"])
print(t)  # output (1, 2, 3, 4, 5, 'kalyan', 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a'])
print(type(t))  # output <class 'tuple'>
print(len(t))  # output 11  
print(t[0])  # output 1  
print(t[1:5])  # output (2, 3, 4, 5)  
print(t[-1])  # output [1, 2, 'k', 'a']  
print(t[-2])  # output {'key1': 'val1', 'key2': 'val2'}
print(t[-5:-1])  # output (5, 'kalyan', 3.14, True, False)
print(t[::-1])  # output ([1, 2, 'k', 'a'], {'key1': 'val1', 'key2': 'val2'}, False, True, 3.14, 'kalyan', 5, 4, 3, 2, 1)

t1 = (1,2,"hello")
t2 =("world", 3.14, True)
print(t1+ t2) # output (1, 2, 'hello', 'world', 3.14, True)

print(t1*4) # output (1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello', 1, 2, 'hello')

# 3. Membership in Tuples

print("Membership")
print(1 in t1)  # output True
print("hello" in t1)  # output True
print(10 in t1)  # output False
print(1 not in t2)  # output True
print("hello" not in t2)  # output True

t1 = (1,2,"hello")
t1.count(1) #output 1 
t2.index(3.14)  # output 1
t2.index("world")  # output 0 
  

t1 = (1,2,3)
print(min(t1) )
print(max(t1) ) # output 3
print(sum(t1))  # output 6 (sum of elements in

t1 = (1,2,3,4 ,[12,11],(2,5,6))
print(t1[4][1])
print(t1[5][2])  # output 6 





