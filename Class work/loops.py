seats = {
    "u1":{'price': 1029,'booking_status' : True},
    "u2":{'price': 1029,'booking_status' : False},
    "u3":{'price': 1029,'booking_status' : True},
    "u4":{'price': 1029,'booking_status' : False},
    "l1":{'price': 2029,'booking_status' : True},
    "l2":{'price': 2029,'booking_status' : False},
    "l3":{'price': 2029,'booking_status' : True},
    "l4":{'price': 2029,'booking_status' : False},
    "l5":{'price': 2029,'booking_status' : False},
}
for i in seats:
    if seats[i]["booking_status"]:
        print(f"**{i}**")
    else:
        print(f"{i}-{seats[i]["price"]}")
        
seatno = input("Enter the seatno : ").lower()
if seatno in seats:
    if seats[seatno]['booking_status']:
        print(f"{seatno} is already booked")
    else:
        name = input("enter name : ")
        age = input("enter age : ")
        gender = input("enter your gender(F-M) : ")
        if age<=5:
            print(f"hello {name} your seat booked sucessfully with 0 cost..")
        elif age <=16:
            print(f" hello {name} your seat booked suceddfully with 50% discount \n Total pay is : {seats[seatno]['price']*0.5}")
        else :
            print(f" hello {name} your seat booked suceddfully with 50% discount \n Total pay is : {seats[seatno]['price']*0.5}")    
                                 
else:
    print(f"enter input valid ")  
    
    
                                   