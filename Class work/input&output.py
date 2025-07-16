# # Input     and Output

# # name = input("ENter ypur name:")
# # print("Hello", name)
# # print(type(name))  # Output: <class 'str'>

# # age = int(input("Enter your age:"))
# # print("Your age is", age)
# # print(type(age))  # Output: <class 'int'>

# # price = float(input("Enter the price:"))
# # print("The price is", price)
# # print(type(price))  # Output: <class 'float'>



# # input as list
# # l = input("Enter names separated by spaces: ").split()
# # print("names are:",l) # Output: names are: ['name1', 'name2', ...]

# # l = input("Enter numbers separated by spaces: ").split()
# # print("numbers are:", l)  # Output: numbers are: ['30', '40', ...]

# l = list(map(int, input("Enter numbers separated by spaces: ").split()))
# print("List of integers:", l)  # Output: List of integers: [30, 40, ...]

# #List of floats
# l_float = list(map(float, input("Enter numbers separated by spaces: ").split()))
# print("List of floats:", l_float)  # Output: List of floats: [30.0, 40.0, ...]

# #Tuple inpput

# t = tuple(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Tuple of integers:", t)  # Output: Tuple of integers: (30, 40, ...)
# # Tuple of floats
# t_float = tuple(map(float, input("Enter numbers separated by spaces: ").split()))
# print("Tuple of floats:", t_float)  # Output: Tuple of floats: (30.0, 40.0, ...)

# t = tuple(input("Enter names separated by spaces: ").split())
# print("Tuple of names:", t)  # Output: Tuple of names: ('name1', 'name2', ...)


# #set input
# s = set(map(int, input("Enter numbers separated by spaces: ").split()))
# print("Set of integers:", s)  # Output: Set of integers: {30, 40, ...}
# # Set of floats
# s_float = set(map(float, input("Enter numbers separated by spaces: ").split()))
# print("Set of floats:", s_float)  # Output: Set of floats: {30.0, 40.0, ...}
# # Set of names
# s_names = set(input("Enter names separated by spaces: ").split())
# print("Set of names:", s_names)  # Output: Set of names: {'name1', 'name2', ...}



# # Dictionary input
# d = eval(input("Enter a dictionary (e.g., {'key1': value1, 'key2': value2}): "))  # input has to give in valid dictionary format 
# # Example input: {'key1': 1, 'key2': 2}
# print("Dictionary:", d)  # Output: Dictionary: {'key1': value1, 'key2': value2} 


# # multiple inputs with unpacking 
# a, b, c = input("Enter three values separated by spaces: ").split() # input kalyan ram dasari
# print("Values are:", a, b, c)  # Output: Values are: a b c
# print(a) # Output: kalyan
# print(b) # Output: ram
# print(c) # Output: dasari

# # Eval is used for evaluating expressions or converting strings to data structures like dictionaries.
# l  = eval(input("Enter a list (e.g., [1, 2, 3]): "))  # input has to give in valid list format
# print("List:", l)  # Output: List: [1, 2, 3] 

# t = eval(input("Enter a tuple (e.g., (1, 2, 3)): "))  # input has to give in valid tuple format
# print("Tuple:", t)  # Output: Tuple: (1, 2, 3)

# s = eval(input("Enter a set (e.g., {1, 2, 3}): "))  # input has to give in valid set format
# print("Set:", s)  # Output: Set: {1, 2, 3}











#OUTPUT 

# what is print()
# It is used to display output on the console. It can take multiple arguments and will print them in the order they are given, separated by spaces by default.
# It can also format the output using f-strings or the format method.

print("Hello", "World")  # Output: Hello World
print("The answer is", 42)  # Output: The answer is 42
print("kalyan ram dasari" , sep="@")  # Output: kalyan@ram@dasari

print("kalyan ram dasari", end="!")  # Output: kalyan ram dasari!
print("kalyan ram dasari", end="\n")  # Output: kalyan ram dasari


# using modulo Operator for formatting
name = "kalyan"
age = 25
print("My name is %s and I am %d years old." % (name, age))  # Output: My name is kalyan and I am 25 years old.
# using format method for formatting
print("My name is {} and I am {} years old.".format(name, age))  # Output: My name is kalyan and I am 25 years old.
# using f-strings for formatting  
print(f"My name is {name} and I am {age} years old.")  # Output: My name is kalyan and I am 25 years old.



