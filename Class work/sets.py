# A Set in Python is a collection of unique elements which are unordered and mutable.
# Python provides various functions to work with Set. In this article, we will see a list of all the functions provided by Python to deal with Sets.

d = set()

type(d)  # output <class 'set'>

d = {1,2,3,9,3,4,3,5, "hello",6,7,2,8,9,4,10}
print(d) #output {1, 2, 3, 4, 5, 'hello', 6, 7, 9, 8, 10}

#Add elements to a Set
d.add(2093)  # Adds a single element
print(d)
d.add("3.14")
d.add("kalyan")
d.add((1,2,3))
print(d)

d.discard('hello')  # Removes 'hello' if it exists
# print(d.remove('2')) # Removes '2', raises KeyError if not found

d.pop()  # Removes and returns an arbitrary element from the set
print(d)

a = {1,2,3}
b = {3,4,5}
c = {2,4,6,8,10}

#UNION 
print("a union b",a.union(b)) #output union {1, 2, 3, 4, 5}

print("a union b with symbol",a | b) # Union of two sets


print("union of 3 sets",a.union(b).union(c))
print("union of 3 sets ",a | b | c)  # Union of three sets 


#DIFFERENCE

print("a diffrence b",a.difference(b)) # Elements in 'a' but not in 'b'
print("a -b",a - b)  # Difference of two sets { 1, 2 }
print("b-a",b - a)  # Difference of two sets { 4, 5 }


print("diff of 3 sets",a.difference(b,c))  # Elements in 'a' but not in 'b' and 'c' {1, 2}
print("diff of 3 sets",a - b - c)  # Difference of three

#INTERSECTION
print(a.intersection(b))  # Elements common to both 'a' and 'b' 

print(a & b)  # Intersection of two sets     


# symmetric_difference() is an opposite to the Python Set intersection() method.   


set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {1, 0, 12}

print(set1.symmetric_difference(set2))
print(set1.symmetric_difference(set3))
print(set2.symmetric_difference(set3))



#DISJOINT

set2 = {7, 8, 9, 10}
set3 = {1, 2}

# checking of disjoint of two sets
print("set1 and set2 are disjoint?",set1.isdisjoint(set2)) # output True

print("set1 and set3 are disjoint?",set1.isdisjoint(set3))# output False


# Python set issubset() method returns True if all elements of a set A are present in another set B which is passed as an argument,
# and returns False if all elements are not present in Python.
# issubset()
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5}
print(s2.issubset(s1))  # output True


A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print(A.issubset(B))
print(B.issubset(A))

# Python Set issuperset() method returns True if all elements of a set B are in set A. Then Set A is the superset of set B.

A = {4, 1, 3, 5}
B = {6, 0, 4, 1, 5, 0, 3, 5}

print("A.issuperset(B) : ", A.issuperset(B))
print("B.issuperset(A) : ", B.issuperset(A))


# Python Method creates an immutable Set object from an iterable. It is a built-in Python function.
# As it is a set object, therefore, we cannot have duplicate values in the frozenset.
names = frozenset("Ram","Sita","Lakshman","Hanuman")
print(names)  # output frozenset({'Ram', 'Sita', 'Lakshman', 'Hanuman'})
print(names.add("Ravan"))  # Raises AttributeError as frozenset is immutable
 

