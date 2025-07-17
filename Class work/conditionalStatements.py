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
                
        
        
data = {
    1 : {"name":"kalyan","exam_status": True, "python":90, "sql":80,"html":96},
    2:{"name":"Abhinay","exam_status": False, "python": None, "sql":None,"html":None},
    3:{"name":"Hari","exam_status": True, "python":45, "sql":80,"html":96},
    4: {"name":"Suresh","exam_status": True, "python": 25, "sql":65,"html":60},
    5: {"name":"Ramesh","exam_status": True, "python": 20, "sql": 45,"html": 50},
    6: {"name":"Ravi","exam_status": True, "python": 100, "sql": 90,"html": 96},
    
}                

stud_id = int(input("ENter student id:"))
if stud_id in data:
    if data[stud_id]["exam_status"]:
        total_marks = (data[stud_id]["python"] + data[stud_id]["sql"] + data[stud_id]["html"])/3
        if total_marks >=90:
            print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is A")
        elif total_marks>80:
            print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is B")
        elif total_marks>60:
            print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is C")     
        elif total_marks>40:
            print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is D")
        else:
            print(f"{data[stud_id]["name"] } has scored {total_marks} exam grade is F")
    else:
        print(f"{data[stud_id]['name']} has not taken the exam")               
else:
    print("INvalid student id") 
    
    
                   
                