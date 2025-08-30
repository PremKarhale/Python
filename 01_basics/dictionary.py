info = {"name":"prem","age":20,"learning":"python" }
print(info)
print(info["name"])#prem
print(info.get("name"))#prem
#for loop in dictionary 
for char in info :
    print(char)
    #name
    #age
    #learning
for char in info:
    print(char , info[char]) 
 #name prem
 #age 20
 #learning python

for key , value in info.items():
    print(key,value)

#conditionals
if "name" in info:
    print("yes present ")

print(info)
info['age']=21
print(info)
print(info.popitem()) #('learning', 'python') pop's out last item from the dictionary
print(info)#{'name': 'prem', 'age': 21}
info["branch"]="IT"
print(info)#{'name': 'prem', 'age': 21, 'branch': 'IT'}

#Dict creation 
key =["masala","ginger","lemon"]
default_value ="delicious"
new_dict = dict.fromkeys(key ,default_value)
print(new_dict)#'masala': 'delicious', 'ginger': 'delicious', 'lemon': 'delicious'}




    