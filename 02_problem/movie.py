# movie ticket pricing solution
import random 
age = int(input("Enter your age to get the ticket Price :"))
arr =["mon","Tue","wed","thu","sat","sun"]
today = random.choice(arr)
print(today)
if age <18 :
    if today == "wed" : 
        print("price of the ticket is : ","$6")
    else:
        print("price of the ticket is:$8")
else:
    if today == "wed" : 
        print("price of the ticket is : ","$6")
    else:
        print("price of the ticket is:$8")
        

     

           
