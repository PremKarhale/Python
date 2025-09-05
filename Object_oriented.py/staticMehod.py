# Static methods are the methods which only belong to its class not to its instance !!

class car ():
    totalcars =0
    def __init__(self ,brand ,model):
        self.__brand=brand  # it became private now ! need to create getter to get the brand
        self.__model=model
        car.totalcars +=1
    def no_of_seates(self):
        return 4
    def fuel_type(self):
        return 'petrol'+' diesel'
    
    # Static methods are NOT class-only
    #They're just utility functions that don't need instance/class data
    @staticmethod  
    def getCarinfo():   
        return 'cars are the means of transport !!'
    

#also property [decorator] convertes the method into the attribut so we can directly access it without need of using parenthesis. 
#Can create read-only properties (without setter)
    @property  
    def privateVarModel(self):
        return self.__model  # Getter method

      

class ElectiricCar(car):
    def __init__(self , brand , model , BatteryBackup):
        super().__init__(brand , model)
        self.BatteryBackup =BatteryBackup
    def fuel_type(self):
        return 'electric charge '
    
tesla=ElectiricCar("Tesla","Model S","80kwh")
tata=car("fdf","fdfs")
safari =car("TATA" ,"safari")

print(tesla.getCarinfo())#cars are the means of transport !!
print(tata.getCarinfo())#cars are the means of transport !!
print(car.getCarinfo())#cars are the means of transport !!


tesla.model="dfd" #value cannot get overwritten because it required no setter 
print(tesla.privateVarModel)  #No parentheses needed (like an attribute)
