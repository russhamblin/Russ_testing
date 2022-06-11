# get all the imports 
from ast import Global
from logging import root
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

 
# directory_from_path = Path(r'C:\Users\russh\source\repos\PythonApplication1\From')

List_of_Text_to_move = []

#using the button get the text file

def get_Text_File():
    TextFileLocation = filedialog.askopenfilename ()
    adjustedPath = fr"{TextFileLocation}"
    tf = open(adjustedPath,'r')    
    text_read = tf.readlines()
    print (text_read)
    
    for t in text_read:
        t = t.strip()
        List_of_Text_to_move.append(t)
    print (List_of_Text_to_move)
    textinfo.insert(END, (TextFileLocation))
    
    

def get_source_dir():
    sourceDirName = filedialog.askdirectory()
    global AdjustedSourceDirName
    AdjustedSourceDirName = fr"{sourceDirName}"
    sourceinfo.insert(END, (sourceDirName))
    

def get_new_dir():
    NewDirName = filedialog.askdirectory()
    global AdjustedNewDirName
    AdjustedNewDirName = fr"{NewDirName}"
    newinfo.insert(END, (NewDirName))
    
List_of_files_to_move = []

def run_this():
    
#get all the files from the source directory
    List_of_files_to_check = os.listdir(AdjustedSourceDirName)

    # check if the files exist in the text file. return a list of files to be moved

    
    for item in List_of_files_to_check:
        if item in List_of_Text_to_move:
            List_of_files_to_move.append(item)

        if not List_of_files_to_move:
            print ("list is empty")

    


# what buttons are needed 
textFileButton = Button(root, text="choose Text file", command=get_Text_File)
dirSourceButton = Button(root, text="Choose Source Directory", command=get_source_dir)
dirNewButton = Button(root,text="Choose new folder Location", command=get_new_dir)
runButton = Button(root, text="Run", command= run_this)
textinfo = Entry(root)
sourceinfo = Entry(root)
newinfo = Entry(root)

#where the buttons are placed
textFileButton.grid(row=1, column=2, padx=10, pady=10)
dirSourceButton.grid(row=2, column=2, padx=10, pady=10)
dirNewButton.grid(row=3, column=2, padx=10, pady=10)
runButton.grid(row=4, column=2, padx=10, pady=10)
textinfo.grid(row=1, column=3,padx=10, pady=10)
sourceinfo.grid(row=2, column=3, padx=10, pady=10)
newinfo.grid(row=3, column=3, padx=10, pady=10)



#get the list of items to move with their full file path

oldFileLocation = []
for item in List_of_files_to_move:
    item = pathlib.PurePath(directory_from_path,item)
    oldFileLocation.append(item)



# create the list of items to move with their NEW file path 

newFileLocation = []
for item in List_of_files_to_move:
    item = pathlib.PurePath(directory_to_path,item)
    newFileLocation.append(item)


# try and move the files that exist

getListCount = len(newFileLocation)
itemCount = 0

while (itemCount<getListCount):
    shutil.move(oldFileLocation[itemCount],newFileLocation[itemCount])
    itemCount = itemCount +1



# provide report of files moved.

root.mainloop()

