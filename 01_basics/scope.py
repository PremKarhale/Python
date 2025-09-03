username = "chaiOrcode"
def func():
    # username ="prem"
    print(username)

print(username) #chaiOrcode  here username is golbal scoped 
func() #prem jab func ke undar bhi username tha , jab username delte kar dia to usne username globally accessed kar liya !!


# closure 
def chaicoder(num):  
    def actual(x):
        return x **num
    return actual

f= chaicoder(3)# retrun karega kya - actual function jo hai uska memory reference 
g=chaicoder(3)
print(f) # f stores the memory address of the function actual 
print(f(3)) #27
