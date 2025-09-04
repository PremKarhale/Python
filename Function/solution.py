def even_generator(limit):
    for i in range(2,limit+1 ,2):
        yield i  # not only returns but also remember the last value 

for num in even_generator(10):
    print(num)