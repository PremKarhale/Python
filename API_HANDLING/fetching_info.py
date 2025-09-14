import requests


# THE METHOD TO FETCHED THE RANDOM USER DATA
def fetch_random_user_api():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response=requests.get(url)
    data =response.json()

    if data['success'] and 'data' in data :
        datamsg=data['message'] #Random users fetched successfully
        userdata = data['data']['data'][0]
        userimage=userdata['picture']['large']
        username=userdata['login']['username']
        userpassword =userdata['login']['password']
        userlocation=userdata['location']['city']
        return datamsg , username , userpassword , userlocation ,userimage
    else:
        raise Exception("Failed to fetched the user data !!")

def main():
    try:
        datamsg , username , userpassword ,userlocation ,userimage=fetch_random_user_api()
        print(f"\n {userimage}")
        print(f"\n {datamsg} \n | Name : {username} \n | UserPassword : {userpassword} \n | Location : {userlocation}")
    except Exception as e :
        print(str(e))

if __name__=="__main__":
    main()

