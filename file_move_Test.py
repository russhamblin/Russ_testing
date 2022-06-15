# get all the imports 
import os
import pathlib
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog

# create the main form
root = Tk()
root.title("Move files with text file app")
root.geometry("800x400")
root.columnconfigure(3,weight =5)
 
#Global parmaters
List_of_Text_to_move = []
oldFileLocation = []
newFileLocation = []
List_of_files_to_move = []
List_of_files_to_check = []

#using the button get the text file
def get_Text_File():
    global TextFileLocation
    TextFileLocation = filedialog.askopenfilename (initialdir= r"C:\Users\russh\source\repos\PythonApplication1\Text")
    adjustedPath = fr"{TextFileLocation}"
    tf = open(adjustedPath,'r')    
    text_read = tf.readlines()
    print (text_read)
    
    for t in text_read:
        t = t.strip()
        List_of_Text_to_move.append(t)    
    textinfo.insert(END, (TextFileLocation))
    dirSourceButton.config(state= NORMAL)
      
#using the button to get the source directory location
def get_source_dir():
    global AdjustedSourceDirName
    global files_to_check
    sourceDirName = filedialog.askdirectory(initialdir= r"C:\Users\russh\source\repos\PythonApplication1\From")    
    AdjustedSourceDirName = fr"{sourceDirName}"
    sourceinfo.insert(END, (sourceDirName))
    files_to_check = os.listdir(AdjustedSourceDirName)
    #for file in files_to_check:    
    #   List_of_files_to_check.append(files_to_check)
    dirNewButton.config(state=NORMAL)
    return AdjustedSourceDirName
   
#using the button to get the to directory location
def get_new_dir():
    global AdjustedNewDirName
    NewDirName = filedialog.askdirectory(initialdir= r"C:\Users\russh\source\repos\PythonApplication1\To")     
    AdjustedNewDirName = (fr"{NewDirName}")
    newinfo.insert(END, (NewDirName))
    runfilemovecheck.config(state=NORMAL)
    return AdjustedNewDirName
    
#using the check button see what files need to be moved
def file_move_check():
    print ("check")
    for item in List_of_Text_to_move:
        for this in files_to_check:
            if item == this:   
                List_of_files_to_move.append(item)          
        
    file_info.insert(END, (List_of_files_to_move))


def run_this():
     print ("nothing") 

def dummyfunciton():
    print ("nothing")    

# what widgits are needed 
textFileButton = Button(root, text="choose Text file", command=get_Text_File)
dirSourceButton = Button(root, text="Choose Source Directory", command=get_source_dir,state = "disabled")
dirNewButton = Button(root,text="Choose new folder Location", command=get_new_dir,state = "disabled")
btn_run = Button(root, text="Run", command= run_this)
textinfo = Entry(root)
sourceinfo = Entry(root)
newinfo = Entry(root)
file_info = Text(root)
runfilemovecheck = Button(root,text= "CHECK FILES TO MOVE", command= file_move_check,state = "disabled")
Cancelprocess = Button(root, text = "CANCEL", command = root.destroy)

#where the widgits are placed
textFileButton.grid(row=1, column=1, padx=10, pady=10)
dirSourceButton.grid(row=2, column=1, padx=10, pady=10,)
dirNewButton.grid(row=3, column=1, padx=10, pady=10)
btn_run.grid(row=5, column=2, padx=10, pady=10)
textinfo.grid(row=1, column=2, sticky="ew", padx=10)
sourceinfo.grid(row=2, column=2, sticky="ew", padx=10)
newinfo.grid(row=3, column=2, sticky="ew", padx=10)
file_info.grid(row=4, column= 2)
runfilemovecheck.grid(row=4, column = 1)
Cancelprocess.grid(row = 5,column =3)

#get the list of items to move with their full file path

def get_old_file_location():
    for item in List_of_files_to_move:
        item = pathlib.PurePath(directory_from_path,item)
        oldFileLocation.append(item)
    return oldFileLocation

# create the list of items to move with their NEW file path 

def get_new_file_location():
    for item in List_of_files_to_move:
        item = pathlib.PurePath(directory_to_path,item)
        newFileLocation.append(item)
    return newFileLocation

# try and move the files that exist

getListCount = len(newFileLocation)
itemCount = 0

while (itemCount<getListCount):
    shutil.move(oldFileLocation[itemCount],newFileLocation[itemCount])
    itemCount = itemCount +1

# provide report of files moved.

root.mainloop()