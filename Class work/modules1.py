# import modules;

# print(modules.add(2,3))
# print(modules.sub(2,3))
# print(modules.mul(2,3))
# print(modules.div(2,3))
# print(modules.mod(2,3))
# print(modules.exp(2,3))

# from modules import add,sub
# print(add(2,3))
# print(sub(30,20))

# from modules import *

# print(add(2,3))
# print(sub(2,3))
# print(mul(2,3))
# print(div(2,3))
# print(mod(2,3))
# print(exp(2,3))



import modules as atm

atm.welcome()

if atm.Login():
    while True:
        atm.Menu()
        ch=input("Enter the choice: ").upper()
        if ch=='C':
            atm.Check_balance()
        elif ch=='D':
            atm.Deposit()
        elif ch=='W':
            atm.Withdraw()
        elif ch=='V':
            atm.View_transaction()
        elif ch=='E':
            print("Thankyou".center(50,'_'))
            break
        else:
            print("Invalid Choice")    