import math
def default(radius):
    area = radius * radius
    circumference = round(2*math.pi*radius ,2) #upto two decimal nos 
    return area ,circumference

a ,c =default(3)
print("Area :",a,"circumference :",c)

