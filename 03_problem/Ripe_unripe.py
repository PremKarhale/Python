#Ripe unripe problem solution

n= input("Enter the no of times you want to run the program :")
for i in range(int(n)) :
    banana= input("enter the color of your banana:").lower()
    if banana == "green" or banana=="Green" :
        print("unripe")
    elif banana == "yellow" or banana=="Yellow" :
        print("Ripe")
    elif banana == "brown" or banana=="Brown" :
        print("overripe")
    else:
        print("Plz Enter the color from \"green\",\" brown\",\" yellow\" only ")




