# products = {
#     1: {'Apple': 30},
#     2: {'Banana': 10},
#     3: {'orange': 20},
#     4: {'Milk': 50},
#     5: {'Bread': 25},
#     6: {'Eggs': 60},
#     7: {'Rice': 40},
#     8: {'Tea': 35},
#     9: {'Sugar': 30},
#     10: {'Salt': 15},
# }

# for key, value in products.items():
#     for name, price in value.items():
#         print(f"{key}. {name} - ₹{price}")

    
products = {
    'Apple': 30,
    'Banana': 10,
    'orange': 20,
    'Milk': 50,
    'Bread': 25,
    'Eggs': 60,
    'Rice': 40,
    'Tea': 35,
    'Sugar': 30,
    'Salt': 15,
}    
AddtoCart = {}
while True:
    print("Available Products : ")
    for i,key in enumerate(products):
        print(f"{i+1}. {key.ljust(10," ")} : ${products [key]}")
    product = input("Enter the productt name(Done-Exit)").title()
    if product == 'Done'    :
        
        if AddtoCart :
            totalbill = 0
            for i in AddtoCart:
                print(f'{i.ljust(10," ")} : {AddtoCart[i]} * {products[i]}')
                totalbill = totalbill+AddtoCart[i]*products[i]
            print(f"Total Bill : {totalbill}")
        else:
            print("Thanks")   
        break
    #Adding products to cart
    if product in products:
        qua = int(input("enter Quantity : "))
        print(f'{product} is added to cart')         
        AddtoCart[product] = qua
    else:
        print(f"{product} is not found")