import requests

def random_jokes_generator():
    url = "https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%252Cid%252Ccontent&page=1"
    response=requests.get(url)
    data=response.json()
    if data['success'] and 'data' in data:
        userdata=data['data']['data'][0]
        msg = data['message']
        id=userdata['id']
        first_joke=userdata['content']
        second_userdata=data['data']['data'][1]
        second_joke=second_userdata['content']
        return first_joke ,second_joke ,msg
    else:
        raise Exception("Failed to fetched the user data !!")
    
def  main():
    try:
        first_joke , second_joke ,msg=random_jokes_generator()
        print(f"\n {msg} \n first joke | {first_joke} \n \n second joke | {second_joke}")
    except Exception as e :
        print(str(e))
    

if __name__=="__main__":
    main()


