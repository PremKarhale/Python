import json
openFile="youtube.txt"

def load_data():
    try:
        with open(openFile,"r") as file:   #all the videos that loads are in teh form of a strings 
            data= json.load(file)
            # print("data type of the loaded data is :",type(data))
            return data
    except FileNotFoundError:
        return []
    
    #json.dump takes two para kya dump karna hai or kisme dump karna hai 
def save_data_helper(videos):
    with open(openFile , "w") as file:
        return json.dump(videos , file)   

def list_all_videos(videos):
    print("\n")
    print("*"*40)
    for index , video in  enumerate(videos , start=1):
        print(f"{index}  {video['name']}- Duration: {video['time']}")
    print("\n")
    print("*"*40)

def add_video(videos):
    name=input("enter the name of the video :")
    time=input("length of the video :")
    videos.append({"name":name , "time":time})#jo jo videos mene add kiya usko append kar do videos me 
    save_data_helper(videos) # it save my added videos in the loader file(youtube.txt)
    print("\n")
    print(f"VIDEO IS SUCESSFULLY ADDED")  


#REMEMBER !! VIDEOS IS THE LIST AND LIST ARE MUATIABLE 
def update_videos(videos):
    list_all_videos(videos)
    userInput =int(input("Enter the video no you want to update :"))
    if 1<= userInput < len(videos):
        name=input("enter the name of the video you want to update")
        time=input("enter the duration of the video you want to update ")
        videos[userInput-1]={"name":name , "time":time}
        save_data_helper(videos)
        print("\n")
        print(f"VIDEO NO {userInput} IS SUCESSFULLY UPDATED")  
    else:
        print("select the valid video no you want to update !!")



def delete_videos(videos):
    list_all_videos(videos)
    userInput =int(input("Enter the video no you want to delete :"))
    if 1<=userInput <len(videos):
        del(videos[userInput-1]) 
        save_data_helper(videos)
        print("\n")
        print(f"VIDEO NO {userInput} IS SUCESSFULLY DELEATED")  
    else:
        print("enter the correct no of the videos ")
 
def main():
    videos =load_data() # all the data into the files is now stored in the videos 

    # print(f"loaded videos :{videos}")

    while True:  # ← Loop is NOW inside main()
            print("\n YOUTUBE MANAGER | CHOOSE ANY OPTION BELOW")
            print("\n")
            print("1. List all youtube videos")
            print("2. Add a youtube videos")
            print("3. Update a youtube video details")
            print("4. Delete youtube video")
            print("5. Exit the App")
            
            choice = input("Enter your choice: ")
            
            match choice:
                case "1":
                    list_all_videos(videos)
                case "2":
                    add_video(videos)
                case "3":
                    update_videos(videos)
                case "4":
                    delete_videos(videos)    
                case "5":
                    print("Goodbye!")
                    break 
                case _:
                    print("Invalid choice")
if __name__=="__main__":
        main()
                
        