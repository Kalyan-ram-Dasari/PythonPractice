# Inputs
Order_ID = int(input("Enter Order ID: "))  # e.g., 101

Product_Name = input("Enter Product Name: ")  # e.g., Fortune Sunflower Oil

Price = float(input("Enter Price: ₹"))  # e.g., 499.50

Categories = list(map(str.strip, input("Enter Categories (comma-separated, e.g., Edible Oil, Cooking Essentials): ").split(',')))

Order_Status = input("Enter Order Status (Delivered | Pending | Cancelled): ")  # e.g., Delivered

Discount = float(input("Enter Discount (%): "))  # e.g., 10.0

Customer_Preferences = set(map(str.strip, input("Enter Customer Preferences (comma-separated, e.g., Fast Delivery, Eco Packaging): ").split(',')))

# Example: {"Name": "Blinkit Warehouse 4", "Contact": 9876543210, "Location": "Delhi"}
Warehouse_Details = eval(input("Enter Warehouse Details (as dictionary): "))


total_price = Price - ((Discount / 100) * Price)



# 1. Comma Separation (sep=', ')
print("Order_ID", Order_ID, "Product_Name", Product_Name, "Price", Price, sep=', ')

# 2. Percentage Formatting
print("Discount Applied: %.2f%%" % Discount)

# 3. Using f-strings

print(f"Product: {Product_Name}")
print(f"Price: ₹{Price}")
print(f"Discount: {Discount}%")
print(f"Order Status: {Order_Status}")
print(f"Total Price after Discount: ₹{total_price:.2f}")


# 4. Using .format() method
print("Warehouse Details: Name - {}, Contact - {}, Location - {}".format(
    Warehouse_Details["Name"], Warehouse_Details["Contact"], Warehouse_Details["Location"]
))
