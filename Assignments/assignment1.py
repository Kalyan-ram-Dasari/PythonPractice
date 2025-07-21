Booking_id = int(input("Enter Booking ID : "))#13

Service_name = input("Enter Service name : ") #Clear trip

price = float(input("ENter price : "))  #4999.50

categories = map(list,input("Enter Categories : "))   #["private dining ","Silver Service ","Buffet Service "]

Booking_Status = input("Enter Booking status m(confirmed|not confirmed): ")# Confirmed

Discount = float(input("Enter discount : "))#10.0

Customer_preference = map(set,input("Enter customer preference : "))#("sea view", "king view", "single room","Twin room")

HotelDetails = eval(input("Enter Hotel Details : "))#{"name" : "krishna Hotels","PH NO" : 1234567890,"Location" : "Hyderabad"} 

#1. Using Comma Separation (sep=',')
print("Booking_id", Booking_id, "Service_name", Service_name, "Price", price, sep=", ")

# 2. Using Percentage Formatting (% operator)
print("Discount Applied: %.2f%%" % Discount)

#Using f-strings (f"")
print(f"Booking_id : {Booking_id} \nPrice : {price} \nDiscount: {Discount}% \nBooking_Status: {Booking_Status} \nTotal fare is : {price - ((Discount / 100) * price)}")


#Using .format() method
print("Hotel Details :  Name -{} PH NO-{} Location-{}".format(HotelDetails["name"],HotelDetails["PH NO"], HotelDetails["Location"]))
