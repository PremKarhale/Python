# default = "kudasai"
def Greet(greet = "kudasai"):  # "para" is also treated as variables !!
    return greet    
while True:
    user_input = input("Enter the greeting:")
    print(Greet(user_input))
    

