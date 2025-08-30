chai_verities =['black','green','oolang','white']
print(chai_verities)
chai_verities[1:2]="lemon"
print(chai_verities) #['black', 'l', 'e', 'm', 'o', 'n', 'oolang', 'white']

chai_verities =['black','green','oolang','white'] #overwite
chai_verities[1:2]=["lemon"]
print(chai_verities)#['black', 'lemon', 'oolang', 'white']

chai_verities_copy = chai_verities.copy() #created the new obj chai_verities_copy
print(chai_verities_copy)
chai_verities_copy.append("green tea")
print(chai_verities_copy)

squre_num =[x**2 for x in range(10)] # loop in the list 
print(squre_num)
cube_num =[x**3 for x in range(5)]
print(cube_num)