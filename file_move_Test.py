# get all the imports 
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
root.geometry("400x400")



# get the source directory for files location
directory_from_path = Path(r'C:\Users\russh\source\repos\PythonApplication1\From')


# get the target directory for files location
directory_to_path = Path(r'C:\Users\russh\source\repos\PythonApplication1\To')

# get the reference or sorting text file location



#get all the files from the source directory
List_of_files_to_check = os.listdir(directory_from_path)


# read the text file and get a list of files
textfile_read = open(r"C:\Users\russh\source\repos\PythonApplication1\Text\Items to move.txt","r")
text_read = textfile_read.readlines()

# remove the hard carrage return from strings in each line

List_of_Text_to_move = []
for t in text_read:
    t = t.strip()
    List_of_Text_to_move.append(t)
print (List_of_Text_to_move)


# check if the files exist in the text file. return a list of files to be moved

List_of_files_to_move = []


for item in List_of_files_to_check:
    if item in List_of_Text_to_move:
        List_of_files_to_move.append(item)

if not List_of_files_to_move:
    print ("list is empty")

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



