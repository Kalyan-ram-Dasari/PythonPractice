#Python Lists
# Lists are mutable, ordered collections of items that can contain mixed data types.        
# Lists are defined using square brackets [] and can be modified after creation.
# Lists can contain elements of different data types, including other lists.
# Lists can be indexed and sliced, similar to strings.


#1. Basic Features of Lists 
print("Lists")

l = [1, 2, 3, 4, 5 ,(1,2,3),"kalyan", 3.14, True, False,{"key1":"val1","key2":"val2"},[1,2,"k","a"]]

print()

print(l)  # output [1, 2, 3, 4, 5, (1, 2, 3), 'kalyan', 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a']]
print(type(l))  # output <class 'list'>
print(len(l))  # output 11 (length of the list)
l[0] = "updated value" # updating the first element 
print(l) # output ['updated value', 2, 3, 4, 5, (1, 2, 3), 'kalyan', 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a']]


l[2:3]= [10,30]
# list1= list(1,2,3,"kalyan")
# print(list1)
string_to_list = list("kalyan")
print(string_to_list)  # output ['k', 'a', 'l', 'y', 'a', 'n'] 

print(l[::-1])
print(l[0:5])
print(l[-7::])
print(l[-7:-13:-1]) 


#Adding Elements
l.append("new item")
print(l)  # output ['updated value', 2, 10, 30, 4, 5, (1, 2, 3), 'kalyan', 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a'], 'new item']
l.insert(4,"inserted item")
print(l)  # output ['updated value', 2, 10, 30, 'inserted item', 4, 5, (1, 2, 3), 'kalyan', 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a'], 'new item']
# print(l.extend(["extended item 1", "extended item 2"]))


#Removing Elements
l.remove("kalyan") 
print(l)  # output ['updated value', 2, 10, 30, 'inserted item', 4, 5, (1, 2, 3), 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a'], 'new item']
l.pop(2) 
print(l)  # output ['updated value', 2, 30, 'inserted item', 4, 5, (1, 2, 3), 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a'], 'new item']


del l[0] 
print(l) # output [2, 30, 'inserted item', 4, 5, (1, 2, 3), 3.14, True, False, {'key1': 'val1', 'key2': 'val2'}, [1, 2, 'k', 'a'], 'new item']

print(l.count(5))  # output 1  
print(l.count('k')) # output 0  
print(l.index(30))  # output 1 
print(l.index('inserted item'))  # output 2
print(l.count(l))  # output 0  
l.clear()
print(l)  # output [] 
l = [1, 9, 2, 4, 5, 7,6, 8, 3, 10]
l.sort()
print(l)   
l.sort(reverse=True)
print(l)  # output [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
l.reverse()
print(l)# output [1, 9, 2, 4, 5, 7, 6, 8, 3, 10] 

k = l.copy()
print("copy of l :",k)

max_value = max(l)
print("Maximum value in l:", max_value)  # output 10

min_value = min(l)
print("Minimum value in l:", min_value)  # output 1

sum_value = sum(l)
print("Sum of elements in l:", sum_value)  # output 55

# Check if an element exists in the list
element_to_check = 5
print(element_to_check in k)  # output True
print(element_to_check not in k)  # output False

 
x = any(k)
print(x)  #output True 

