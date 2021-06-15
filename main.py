import shutil
import os
import time

def move(location,destination):
  shutil.move(location,destination)
 
def movedhistory(filename,pathmoved):
  
  open1 = open("myhistory.txt","a")
  open1.write("moved"+filename+" \n  to  \n "+pathmoved+"\n"+time.ctime())
  open1.close()
 
while True:
        file_list = ["mp4","html","css","pdf","png","jpeg","zip","mkv","jpg","deb","tar","py"]
        opn3 = open("directory.txt","r")
        path= opn3.read()
        opn3.close()
        file1  = os.listdir(path)
        
        for file in file1:
         file2 = file.split(".")
         
         
         if file_list[0] in file2:
                    folder_path = path+"files of format"+file_list[0]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
                
         elif file_list[1] in file2:
                    folder_path = path+"files of format"+file_list[1]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
                
                
         elif file_list[2] in file2:
                    folder_path = path+"files of format"+file_list[2]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
                    
         elif file_list[3] in file2:
                    folder_path = path+"files of format"+file_list[3]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
                    
         elif file_list[4] in file2:
                    folder_path = path+"files of format"+file_list[4]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)

                
         elif file_list[5] in file2:
                    folder_path = path+"files of format"+file_list[5]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
                    
         elif file_list[6] in file2:
                    folder_path = path+"files of format"+file_list[6]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)

         elif file_list[7] in file2:
                    folder_path = path+"files of format"+file_list[7]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
         elif file_list[8] in file2:
                    folder_path = path+"files of format"+file_list[8]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
         elif file_list[9] in file2:
                    folder_path = path+"files of format"+file_list[9]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
         elif file_list[10] in file2:
                    folder_path = path+"files of format"+file_list[10]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
         elif file_list[11] in file2:
                    folder_path = path+"files of format"+file_list[11]
                    try:
                        os.mkdir(folder_path)
                    except:
                        location= path+file
                        destination = folder_path
                        movedhistory(location , destination)
                        move(location,destination)
         else:
                 x= 1
        