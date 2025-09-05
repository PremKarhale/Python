#self is a reference to the current instance of the class. It's how Python knows which specific object you're working with.

class car ():
    totalcars =0
    def __init__(self ,brand ,model):
        self.__brand=brand   # it became private now ! need to create getter to get the brand
        self.model=model
        car.totalcars +=1
    def no_of_seates(self):
        return 4
    def fuel_type(self):
        return 'petrol'+' diesel'
    
  
        

class ElectiricCar(car):
    def __init__(self , brand , model , BatteryBackup):
        super().__init__(brand , model)
        self.BatteryBackup =BatteryBackup
    def fuel_type(self):
        return 'electric charge '
    
tesla=ElectiricCar("Tesla","Model S","80kwh")
safari =car("TATA" ,"safari")
Tata =car("Tata" , "nexon")

print(car.totalcars)#3
print(safari.fuel_type())
print(tesla.fuel_type())