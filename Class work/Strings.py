#Strings    
print("Strings")
s = "hello world"
print(s) # output hello world
print(s[::2]) # output hlowrd

print( "Welcome to" +" " +  s)    # output Welcome to hello world  

print(s*10) # output hello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello worldhello world 
 
# Indexing 

print("Indexing")
print()
s = "welcome to python"
print(s[0]) # output w
print(s[1]) # output e
print(s[-1]) # output n
print(s[-2]) # output o
print(s[-5]) # output p


# Slicing
print("Slicing")
print()
s = "welcome to python"
print(s[0:5]) # output welco
print(s[10::]) # output python
print(s[0:5:2]) # output wco
print(s[::-1]) # output nohtyp ot emoclew
print(s[-17:-10]) # output welcome

#Membership 

s = "welcome to python"
print("Membership")

print("w" in s) # output True
print("z" in s) # output False
print("w" not in s) # output False
print("z" not in s) # output True


#Built-in String Functions
print()
print("Built-in String Functions")

s = "welcome to python"
print(s.upper()) # output WELCOME TO PYTHON
print(s.lower()) # output welcome to python 
print(s.title()) # output Welcome To Python
print(s.capitalize()) # output Welcome to python
print(s.strip()) # output welcome to python (removes leading and trailing spaces)
print(s.replace("python", "java")) # output welcome to java     
print(s.split()) # output ['welcome', 'to', 'python'] (splits the string into a list of words)
print(s.find("to")) # output 8 (finds the index of the first occurrence of the substring "to")
print(s.count("o")) # output 2 (counts the number of occurrences of the character "o")
print(s.startswith("welcome")) # output True (checks if the string starts with "welcome")
print(s.endswith("python")) # output True (checks if the string ends with "python")
print(s.isalpha()) # output False (checks if the string contains only alphabetic characters)
print(s.isdigit()) # output False (checks if the string contains only digits)
print(max(s)) # output w  
print(min(s)) # output  (space character is the smallest character in ASCII)
print(len(s)) # output 17 (length of the string)
print(chr(97)) # output a (converts ASCII value 97 to character 'a')
print(ord('a')) # output 97 (converts character 'a' to its ASCII value 97)
print(s.index("to")) # output 8 (finds the index of the first occurrence of the substring "to", raises ValueError if not found)
print(s.isalnum()) # output False (checks if the string contains only alphanumeric characters)
print(s.rfind("o")) # output 14 (finds the index of the last occurrence of the character "o")
s = "WelcoMe to pYthon"
print(s.casefold()) 



l = ['PFS31', 'PFS32', 'PFS3','JFS30', 'JFS22', 'JFS02', 'JFS35','DA10','DA13','DA06','DS22','DS11','DS10','DS31']
for i in l:
    if i.startswith("JFS"):
        print("starts with JFS :",i) 
    # output JFS30, JFS22, JFS02, JFS35
    print()
for i in l:
    if i.endswith("10"):
        print("ends with 10 : ",i)
    # output DA10, DS10    


 
# password Encryption
print()
print("Password Encryption")
password = "mysecretpassword"
encrypted_password = "k4819n(283)d2jhk"
 
print(password.translate(str.maketrans(password, encrypted_password)))  

s = "hello@world@python"
print(s.partition("@"))  # output ('hello', '@', 'world@python')  
print(s.rpartition("@"))  # output ('hello@world', '@', 'python') 
 
 
l = "kalyan"     




