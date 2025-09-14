import sqlite3
conn= sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()
cursor.execute(''' 
CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL , 
               time TEXT NOT NULL
               )
''')
def list_videos():
       cursor.execute("select * from videos")
       videos =cursor.fetchall()
       if videos:
            print("\n" + "="*50)
            print("YOUR YOUTUBE VIDEOS:")
            print("="*50)
            for row in videos:
                print(f"ID: {row[0]} | Name: {row[1]} | Duration: {row[2]}")
            print("="*50)
       else:
             print("\nNo videos found in your library!")

def add_videos(name , time):
       cursor.execute("insert into videos (name , time) values(? , ?)",(name , time))
       conn.commit()# to connect with the database 
       print(f"\n Video '{name}' added successfully!")

def update_videos(video_id , new_name , new_time):
       cursor.execute("update videos SET name =? , time=? , video_id ",(new_name , new_time ,video_id))
       conn.commit()
def delete_video(video_id):
       cursor.execute("delete from videos where id = ?",(video_id,))
       conn.commit()
       print(f"\n video no {video_id} is deleted SUCESSFULLY !! ")

def  delete_all_videos():
       cursor.execute("select count(*) from videos ") # get the count of the rows in the table 
       count =cursor.fetchone()[0]
       if count ==0:
             print("\n❌ No videos to delete! Your library is already empty.")
             return
       print(f"\n⚠️  Warning: This will delete all {count} videos from your library!")
       confirmation = input("Are you sure? Type 'YES' to confirm: ").strip()
       if confirmation.upper() == 'YES':
            cursor.execute("DELETE FROM videos")
            conn.commit()
            print(f"\n✅ All {count} videos have been deleted successfully!")
    
    

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
                   name =input("Enter the name of the video :")
                   time = input("Enter the time of the video :") 
                   update_videos(video_id , name , time)        
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
    conn.close() # database close for memory optimisation                

if __name__=="__main__":
        main()