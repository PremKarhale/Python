import pymongo
import urllib.parse
from bson import ObjectId

#not a good practice to add passoword and username in the code files 
password = "Prem@1234"
encoded_password = urllib.parse.quote_plus(password)  # "Prem%401234"
client = pymongo.MongoClient(f"mongodb+srv://premkarhale:{encoded_password}@cluster0.7apzc5r.mongodb.net/")
db=client["ytmanager"]

video_collection =db["videos"]
print(video_collection) # give me the collections of all the stored videos 

def list_videos():
       collections= list(video_collection.find()) #now it give me the list of videos in the collections
       if collections :
             print("\n" + "="*50)
             print("YOUR YOUTUBE VIDEOS:")
             print("="*50)
             for video in collections:
                print(f"ID : {video['_id']} , NAME : {video['name']} ,TIME : {video['time']}")
             print("="*50)
       else:
             print("\n no videos found in your library !!!")         

def add_videos(name , time ):
        video_collection.insert_one({"name":name , "time":time})
        print(f"\n your video '{name}' is added sucessfully ".upper())

def update_videos(video_id , new_name , new_time ):
       video_collection.update_one({"_id":video_id},{"$set":{"name":new_name , "time":new_time}})
       print(f"\n video name '{new_name}' is updated sucessfully ".upper())

def delete_video(video_id):
       video_collection.delete_one({"_id":ObjectId(video_id)})
def delete_all_videos():
       video_collection.delete_many({})

def main():
    while True:
            print("\n YOUTUBE MANAGER | CHOOSE ANY OPTION BELOW")
            print("\n")
            print("1. List all youtube videos")
            print("2. Add a youtube videos")
            print("3. Update a youtube video details")
            print("4. Delete youtube video")
            print("5. Delete all the videos")
            print("6. Exit the App")
            choice =input ("Enter your choice ")
            if choice =="1":
                   list_videos()
            elif choice =="2":
                   name =input("Enter the name of the video :")
                   time = input("Enter the time of the video :")
                   add_videos(name , time)
            elif choice =="3":
                    video_id=input("Enter the video id to update :")
                    obj_id = ObjectId(video_id)
                    name =input("Enter the name of the video :")
                    time = input("Enter the time of the video :") 
                    update_videos(obj_id , name , time)      
            elif choice =="4":
                   video_id=input("Enter the video id to delete :")                  
                   delete_video(video_id)
            elif choice =="5":
                   delete_all_videos()
            elif choice =="6":
                   print("GOOD BYE !!")
                   return
            else:
                   print("Enter the valid choice !!")



if __name__=="__main__":
    main()
