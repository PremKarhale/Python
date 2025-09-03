import time

wait_time =0.5
attempt = 0
max_attempt=5

while attempt < max_attempt :
    input_val = input("Enter the input :")
    print("Attempt :",attempt +1 , "waiting Time :",wait_time)
    time.sleep(wait_time)
    print("WRONG INPUT")
    wait_time *= 2
    attempt += 1
print("you have reached to the limit of your attempts \"TRY AGAIN LATER\"")    







