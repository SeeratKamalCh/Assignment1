# File System App

import os
import re


"""
Semantics

On Run:
Menu is displayed
User is asked to select an operation
on selection, the program asks for a filename separately for each operation because it is a  multiple file system

Exception:
    if user asks to create an already existing file then program asks it to overwrite it or not.

"""

#Play app function keeps running till Exit is not pressed.


def PlayApp():
    choice=''
    while(choice!="E"):
        print("\nEnter Choice",end="")
        choice=input()
        state=1
        if choice=="C" or choice=="c":
            state=0
            GetFileInput(state)
            CreateFile()
        
        elif choice=="R" or choice=="r":
            GetFileInput(state)
            RemoveFile()
            
        
        elif choice=="U" or choice=="u":
            GetFileInput(state)
            UpdateFile()
            
        
        elif choice=="S" or choice=="s":
            GetFileInput(state)
            SearchFile()
            
        
        elif choice=="W" or choice=="w":
            GetFileInput(state)
            ReplaceWord()
            
        elif choice=="D" or choice=="d":
            GetFileInput(state)
            ShowFileData()
            
        elif choice=="E" or choice=="e":    
            break
            
        else:
            print("Incorrect instruction enter again")
    return
            
           
# Menu to display options
def Menu():
    print("Select C: Create a file")
    print("Select R: Remove a file")
    print("Select U: Update a file")
    print("Select D: Show Content")
    print("Select S: Search String")
    print("Select W: Replace word")
    print("Select E: Exit program")
        
#Get file input from user on which operation is to be performed
def GetFileInput(state):
    global filename
    print("Enter filename",end='')
    filename=''
    filename=input()
    while(filename==''):
        print("Please enter valid filename")
        filename=input()
    return


# Check if file is already existing or not
def CheckExisting():
    if os.path.exists(dir_path+"/"+filename):
        print("File Already Existing Overwrite it? Y or N",end='')
        choice=input()
        if choice=="Y":
            return 3
        if choice=="N":
            return 2
    else:
        return 1
        
    

    
#Create a new file
def CreateFile():
    global filename
    choice=CheckExisting()
    if choice==1 or choice==3:  #Overwrite or create new file
        file=open(filename,'w+')
        print("Write Content",end="")
        content=input()
        file.write(content)
        file.close()
        print("File Created and Saved")
     
    return

# Remove file
def RemoveFile():
    global filename
    try:
        os.remove(filename)
        print("File Removed")
    except:
        print("File does not exist")
    return



# Update (Overwrite or append)
def UpdateFile():
    global filename
    try:
        file=open(filename,'r+')
        print("Select O to overwrite")
        print("Select A to append",end="")
        choice=input()
        if choice=="O" or choice=="o":
            print("Enter data",end='')
            data=input()
            file.write(data)
        elif choice=="A" or choice=="a":
            print("Enter data",end='')
            data=input()
            prevData=file.read()
            NewData=prevData+data
            file.write(NewData)
        file.close()    
        print("File Updated")
    except:
        print("File does not exist")
    return


#Search string in file
def SearchFile():
    global filename
    try:
        file=open(filename,"r")
        data=file.read().strip().split()
        print("Enter string",end="")
        string=input()
        SearchResult=[i for i, item in enumerate(data) if item.lowercase()==word1.lowercase()]
        print(SearchResult)
        print(data)
        print(str(len(SearchResult))+" instances found")    
    except:
        print("File does not exist")
    return


# Replace word in file
#Assumption with replace word . Replace a word whole not substring in word.
def ReplaceWord():
    global filename
    try:
        print("Replace word",end="")
        oldword=input()
        print("Replaced by",end="")
        newWord=input()
        file=open(filename,"r+")
        data=file.read().strip().split()
        SearchResult=[i for i, item in enumerate(data) if item.lowercase()==word1.lowercase()]
        for i in SearchResult:
            data[i]=newWord
        file=open(filename,"w+")
        print(data)
        data=" ".join(data)
        file.write(data)
        file.close()
        print("Replaced words")
    except:
        print("File does not exist")
    return 



#Get current path
dir_path = os.path.dirname(os.path.realpath(__file__))
filename=''
Menu()
PlayApp()




    