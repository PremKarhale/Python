#self is a reference to the current instance of the class. It's how Python knows which specific object you're working with.

class car ():
    def __init__(self ,brand ,model):
        self.__brand=brand   # it became private now !
        self.model=model
    def no_of_seates(self):
        return 4
    def get_brand(self):
        return self.__brand +"!"
        

class ElectiricCar(car):
    def __init__(self , brand , model , BatteryBackup):
        super().__init__(brand , model)
        self.BatteryBackup =BatteryBackup

tesla=ElectiricCar("Tesla","Model S","80kwh")
print(tesla.no_of_seates())
print(tesla.BatteryBackup)
print(tesla.model)
print(tesla.get_brand())#Tesla! this is the way to access the private attribute using getattribute method.(encapsulation)
        