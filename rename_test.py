# get all the imports 
from operator import contains
import os
import pathlib
import shutil
from pathlib import Path
from tkinter import *
from tkinter import filedialog

#-------------------------------------------------create the main form----------------------------------------------
root = Tk()
root.title("Rename files with text file app")
root.geometry("600x400")
root.columnconfigure(1,weight =1)
root.columnconfigure(2,weight =3) 
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=1)
#----------------------------------------------------Global parmaters---------------------------------------------
List_Of_Files_To_Rename = []
List_Of_Files_To_Action = []
List_of_files_to_check = []
Dirpath = ""

#---------------------------------using the button get the files to rename and place them in a list---------------
def Files_To_Rename(): 
    global Dirpath
    global FileExt   
    filenames = filedialog.askopenfilenames(initialdir= r"C:\Users\russh\source\repos\PythonApplication1\rename")
    for filename in filenames:
        Dirpath = os.path.dirname(filename)
        filepath = os.path.basename(filename)
        filename = os.path.splitext(filepath)[0]
        FileExt =  os.path.splitext(filepath)[1]            
        List_Of_Files_To_Rename.append(filename)   
    count = 0
    for item in List_Of_Files_To_Rename:
        textinfo.insert((count), (item))
        count = count + 1
    
    
#--------------------------------using the check button see what files need to be reviewed against----------------------
def file_move_check():
    global Dirpath
    filenames = os.listdir(Dirpath)  
    for filename in filenames:
        filepath = os.path.basename(filename)
        filename = os.path.splitext(filepath)[0]         
        List_of_files_to_check.append(filename)   
    count = 0
    for item in List_of_files_to_check:
        for rename in List_Of_Files_To_Rename:
            if item == rename:
               pass
            else: 
                file_info.insert((count), (item))
                List_Of_Files_To_Action.append(item)
                count = count + 1 

#-----------------------------------------using the run button to action the files------------------------------------------
def run_this():
     for f in List_Of_Files_To_Rename:
        global FileExt            
        fnew = f.split('(')[0]  
        rev_list = []        
        for file in List_Of_Files_To_Action:                               
            if  file.startswith(fnew):
                rev = file.split(f'{fnew}')[1]
                rev = rev.replace("_","")
                rev_list.append(rev)
            else:
                pass
        rev_list.sort(reverse=True)
        new_rev = rev_list[0]
        update_rev = int(new_rev)
        update_rev = update_rev+1
        newname = f"{fnew}_{update_rev}"
        renamer(f, newname,FileExt)
        

def renamer(oldname, newname,FileExt): 
    global Dirpath   
    src = f"{Dirpath}/{oldname}.{FileExt}"
    dst = f"{Dirpath}/{newname}.{FileExt}"

    os.rename(src, dst)            

     

# -------------------------------------what widgits are needed ----------------------------------------------
textFileButton = Button(root, text="choose Files to rename", command=Files_To_Rename)
btn_run = Button(root, text="Run", command= run_this)
textinfo = Listbox(root)
file_info = Listbox(root, height= 10)
runfilemovecheck = Button(root,text= "RUN CHECK", command= file_move_check,)
Cancelprocess = Button(root, text = "CANCEL", command = root.destroy)

#-------------------------------------where the widgits are placed--------------------------------------------
textFileButton.grid(row=1, column=1, sticky = "ne", padx=10, pady=10)
btn_run.grid(row=3, column=1, sticky = "ne",padx=10, pady=10)
textinfo.grid(row=1, column=2, sticky="nsew", padx=10)
file_info.grid(row=2, column= 2, sticky="nsew",padx=10, pady=10)
runfilemovecheck.grid(row=2, column = 1,sticky = "ne",padx=10, pady=10)
Cancelprocess.grid(row = 3,column =2,sticky = "ne",padx=10, pady=10)

#-------------------------------------renaming files-------------------------------------------------------



#----------------------------------remove additional info from original file name-------------------------

def remove_des(oldname):
    return oldname.split('(')[0]

def removeRev(text,n):
    text = [text[i:i+n] for i in range(0,len(text),n)

root.mainloop()