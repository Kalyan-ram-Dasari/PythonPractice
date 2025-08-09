# def add(a,b):
#     a+b
# def sub(a,b):
#     a-b
# def mul(a,b):
#     a*b
# def div(a,b):
#     a/b
# def mod(a,b):
#     a%b
# def exp(a,b):
#     a**b
    
    
    
data = {
    12345:{'pin':123,'balance':5678,'history':[]},
    36783:{'pin':123,'balance':5678,'history':[]},
    23451:{'pin':123,'balance':5678,'history':[]},
    54321:{'pin':123,'balance':5678,'history':[]},
    
}    
    
def welcome():
    print("Welcome to Bank ".center(50,'*'))
def Menu():
    print("/n Check Balance")
    print("Deposit")
    print("withdraw")
    print("View Transactions")
    print("Exit")
    
def Login(account_number,pin):
    global acc_num
    if account_number  in data:
        if data[account_number]['pin'] == pin:
            print("Login successfull")
            acc_num = account_number
            return True
        else:
            print("invalid pin")
            return False
    else:
        print("Invalid account number")
        return False
def Check_balance():
    if acc_num:
        print(f'\n Current balance : {data[acc_num]['balance']}')  
    else:
        print("You need to login again")
def Deposit():
    if acc_num:
        amount = int(input("Enter amount to deposit : "))
        data[acc_num]['balance']+=amount
        data[acc_num]['history'].append(f'Deposited - ${amount}')
        print(f'${amount} is successfully deposited')
    else:
        print("you need to login again")
        
def Withdraw():
    if acc_num:
        amount=int(input("Enter the amount to withdraw: "))
        if data[acc_num]['balance']>=amount:
            data[acc_num]['balance']-=amount
            data[acc_num]['history'].append(f'Withdraw - ${amount}')
            print(f'${amount} is successfully Withdraw')
        else:
            print("Insufficient Balance")
    else:
        print("You need to login again")

def View_transaction():
    if acc_num:
        if data[acc_num]['history']:
            print("Transactions History".center(50,'-'))
            for i in data[acc_num]['history']:
                print(i)
            else:
                print("End of the history".center(50,'-'))

        else:
            print("No Transactions")
    else:
        print("You need to login again")              
  
                                                         
    
            
                        