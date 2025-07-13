# Dictnaries are mutable, tuples are immutable
#A dictionary in Python is an ordered, mutable collection that stores key-value pairs. Unlike lists or tuples, which are indexed by position, dictionaries are indexed by unique keys.


d1 = {"name":"kalyan", 1 :"one",float : 3.14, bool: True, }

d = {"name": "kalyan", "age": 25, "city": "Hyderabad"}
print(d)  # output {'name': 'kalyan', 'age': 25, 'city': 'Hyderabad'}

# Key Features of Dictionaries:
# 1. Keys must be unique – If you use duplicate keys, the last value will overwrite the
# previous one.
# 2. Keys must be immutable – Strings, numbers, and tuples can be used as keys, but
# lists and dictionaries cannot.
# 3. Values can be of any data type – Integers, floats, lists, tuples, another dictionary,
# etc.
# 4. Dictionaries are mutable – You can modify, add, or remove items after the
# dictionary is created.


#Accessing Values 

print(d["name"]) # output kalyan

print(d["age"]) # output 25

print(d.get("city")) # output Hyderabad

print(d.get("country", "Not Found")) # output Not Found 


#Adding and Updating Items
d["country"] = "India"  # Adding a new key-value pair
print(d)  # output {'name': 'kalyan', 'age': 25, 'city': 'Hyderabad', 'country': 'India'}
d["age"] = 23
print(d)  # output {'name': 'kalyan', 'age': 23, 'city': 'Hyderabad', 'country': 'India'}

#Removing Items
d.pop("city")  # Removes the key 'city'
print(d)  # output {'name': 'kalyan', 'age': 23, 'country': 'India'}
d.popitem()  # Removes the last inserted key-value pair
print(d)  # output {'name': 'kalyan', 'age': 23}
del d["age"]  # Deletes the key 'age'   
print(d)  # output {'name': 'kalyan'}
d.clear()  # Clears the dictionary
print(d)  # output {}



d = {"name": "kalyan", "age": 25, "city": "Hyderabad"}

#Dictionary Methods for Accessing Data

print(d.keys())  # output dict_keys(['name', 'age', 'city'])
print(d.values())  # output dict_values(['kalyan', 25, 'Hyderabad'])
print(d.items())  # output dict_items([('name', 'kalyan'), ('age', 25), ('city', 'Hyderabad')])
print(d.get("Qualification","Not Found"))  # output Not Found

#Dictionary Methods for Adding and Updating Data 
d.update({"country": "India"})  # Adds a new key-value pair
print(d)  # output {'name': 'kalyan', 'age': 25, 'city': 'Hyderabad', 'country': 'India'}

d.setdefault("hobby","reading") # Adds a new key-value pair if the key does not exist if value exists it does not change the value
print(d)  # output {'name': 'kalyan', 'age': 25, 'city': 'Hyderabad', 'country': 'India', 'hobby': 'reading'}



