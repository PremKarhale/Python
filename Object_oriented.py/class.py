class car ():
    def __init__(self , brand , model ):
        self.brand =brand
        self.model = model 
    def fullname(self):
        return f"{self.brand} {self.model}"
    
my_car = car("Toyota","safari") #created obj my_car 
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())

new_obj=car("porshe" ,"911 Carerra")
print(new_obj.brand)
print(new_obj.model)


