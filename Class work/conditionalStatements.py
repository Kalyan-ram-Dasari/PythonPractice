# hr , min = list(map(int,input("Enter Railway time in HH:MM format:").split(":")))

# if hr>=0 and hr<24 and min >=0 and min <= 60:
#     if hr>=0 and hr<4:
#         print("Its high time to sleep")
#     if hr>=4 and hr<12:
#         print("Good morning , hava a nice day")
#     if hr>=12 and hr<16:
#         print("Good afternoon , had your lunch?")
#     if hr>= 16 and hr<20:
#         print("Good evening , how was your day?")
#     if hr>= 20 and hr<=24:
#         print("Good night , sleep well")
# else: 
#     print("Invalid time format .Please enter correct time ")
                
        
        
# data = {
#     1 : {"name":"kalyan","exam_status": True, "python":90, "sql":80,"html":96},
#     2:{"name":"Abhinay","exam_status": False, "python": None, "sql":None,"html":None},
#     3:{"name":"Hari","exam_status": True, "python":45, "sql":80,"html":96},
#     4: {"name":"Suresh","exam_status": True, "python": 25, "sql":65,"html":60},
#     5: {"name":"Ramesh","exam_status": True, "python": 20, "sql": 45,"html": 50},
#     6: {"name":"Ravi","exam_status": True, "python": 100, "sql": 90,"html": 96},
    
# }                

# stud_id = int(input("ENter student id:"))
# if stud_id in data:
#     if data[stud_id]["exam_status"]:
#         total_marks = (data[stud_id]["python"] + data[stud_id]["sql"] + data[stud_id]["html"])/3
#         if total_marks >=90:
#             print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is A")
#         elif total_marks>80:
#             print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is B")
#         elif total_marks>60:
#             print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is C")     
#         elif total_marks>40:
#             print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is D")
#         else:
#             print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is F")
#     else:
#         print(f"{data[stud_id]['name']} has not taken the exam")               
# else:
#     print("INvalid student id") 
    
    
    
    
   #TICKET BOOKING SYSTEM 
    
# seate = {
#     "L1": True,
#     "L2": True,
#     "L3":False,
#     "L4": True,
#     "L5": True,
#     "L6": False,
#     "L7": False,
#     }

# seat_no = input("Enter seat number:").upper()
# if seat_no in seate:
#     if seate[seat_no]:
#         print(f"Seat {seat_no} is already booked")
#     else:
#         print(f"Seat {seat_no} is available for booking")
# else:
#     print("Invalid seat number , try to chack between L1 to L7")        
    
    
    
## PRODUCT DISCOUNT SYSTEM


# data = {
#     "watch" : {'discount':60, 'brands': ['Titan', 'Fastrack', 'Casio']},
#     "facewash": {"discount": 30, 'brands': ['Nivea', 'Garnier', 'Pond']},
#     "shirts" : {"discount": 50, 'brands': ['Allen Solly', 'Van Heusen', 'Peter England']},
#     "Jeans": {"discount": 40, 'brands': ['Levis', 'Wrangler', 'Lee']},
# }    
# print("Welcome to the sale")
# print("Available products are:", data.keys(),)
# prod = input("Enter product name:").lower()
# if prod in data:
#     print(f"{data[prod]["discount"] } % discount is going on {prod} of brands {data[prod]["brands"]} ")
# else:
#     print(f"Product is not available , check with otherproducts {data.keys()}")                       
                
                
# MOVIE TICKET BOOKING SYSTEM               
movies = {
    "salaar":{'kids':True},
    "rajarani":{'kids':False},
    "kannapa":{'kids':False},
    "jawan":{'kids':True},
    "arjunreddy":{'kids':False}
    
}                

print(" Welcome to the Hotstar ".center(30,"="))

movie = input("Enter movie name:").lower()

if movie in movies:
    if movies[movie]['kids']:
        print(f"{movie} is a kids movie , you can watch it with your family")
    else:
        print(f"{movie} is not a kids movie , you can watch it with your friends")
else:
    print(f"{movie} is not available in our collection , please check with other movies {movies.keys()}") 
    
    
    
data = {
    'INDIA': ("passport"),
    'NEPAL': ("passport"),
    'USA': ("passport","visa"),
    'CANADA'  : ("passport","visa"),
          
}    

from_place = input("Enter from place:").upper()
to_place = input("Enter to place:").upper()

if to_place in data:
    if len(data[to_place]) ==1:
         print(f"To travel from {from_place} to {to_place} you need {data[to_place]}")
    else:
        print(f"To travel from {from_place} to {to_place} you need {data[to_place]} ")     
else:
    print(f"{to_place} is not available in our collection , please check with other places {data.keys()}")    
       