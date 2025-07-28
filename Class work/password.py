password = 1234
chk_password = int(input("enter value : "))
while True:
    if password==chk_password:
        print("Login success")
    else:
        print("Invalid ")    
    
n = int(input())

for i in range(n):
    name,msg= input().split(":")
    if name in chat:
        chat[name].append(i,msg.strip())
    else:
         chat[name]=[(i,msg.strip())]
         
while True:
    print("1.count total msgs")
    print("2.Identify unique")
    print("0-exit")
    ch = int(input("enter your choice"))
              
print(chat)
