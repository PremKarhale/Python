# transportation sol

n = input("Enter the iteration you want:")
for i in range(int(n)):
    distance = float(input("Enter the Distance you have to cover:"))
    if distance < 0:
        print("enter the positive distance")
        exit()    
    if distance > 0 and distance < 3:
        print("walk")
    elif distance < 15:
        print("Bike")
    elif distance >= 15:
        print("car")
    else:
        print("Enter the valid distance")
        
  