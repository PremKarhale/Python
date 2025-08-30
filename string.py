chai ="masala chai "
print(chai)
print(chai[:]) #masala chai
print(chai[0:6]) #masala  slicing
print(chai[:4]) #masa
print(chai[7:]) #chai
quantity = 2
order = "i ordered {} cups of {}"
print(order.format(quantity , chai))


print(chai.upper()) #MASALA CHAI
print(chai) #masala chai    this is because string are immutavble

chai = 'green tea '
print(chai) #green tea
print(chai.strip()) # remove the wide spaces 
print(chai.replace("green","lemon"))

chai =' green tea , lemon tea , masala chai '
print(chai.split(",")) #[' green tea ', ' lemon tea ', ' masala chai ']

chai_verity =['lemon_chai','ginger_chai','masala_chai']
print(chai_verity)
print(''.join(chai_verity))#lemon chai ginger chai masala chai
print('-'.join(chai_verity))#lemon_chai-ginger_chai-masala_chai

print(len(chai.strip())) #35 strip() removes the blank spaces 

chai =" he said,\"Masala chai is asewome \" "
print(chai)

print("masala\nchai")#masala  
                    #chai
print(r"masala\nchai") #masala\nchai  r here is raw 
print(r"c:\user\pwd") #c:\user\pwd
