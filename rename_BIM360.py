# get all the imports 
from genericpath import isfile
from operator import contains
import os
import pathlib
import shutil
from pathlib import Path
from tabnanny import check
from tkinter import *
from tkinter import filedialog
import tkinter

#-------------------------------------------------create the main form----------------------------------------------
root = Tk()
root.title("Rename files with text file app")
root.geometry("600x600")
root.columnconfigure(1,weight =1)
root.columnconfigure(2,weight =3) 
root.rowconfigure(1, weight=3)
root.rowconfigure(2, weight=3)
root.rowconfigure(3, weight=1)
root.rowconfigure(4, weight=1)
root.rowconfigure(5, weight=1)
root.rowconfigure(6, weight=1)
#----------------------------------------------------Global parmaters---------------------------------------------
List_Of_Files_To_Rename = []
List_Of_Files_To_Action = []
List_of_files_to_check = []
Dirpath = ""
Text_TO_Replace = tkinter.StringVar()
Text_To_Replace_With = tkinter.StringVar()

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
  

#-----------------------------------------using the run button to action the files------------------------------------------
def run_this():

    for f in List_Of_Files_To_Rename:
        global FileExt            
        fnew = f.split('_RVT')[0] 
        fnew = fnew + "_RVT"     
   

        newname = f"{fnew}"
        renamer(f, newname,FileExt)
        

def renamer(oldname, newname,FileExt): 
    global Dirpath   
    src = f"{Dirpath}/{oldname}{FileExt}"
    dst = f"{Dirpath}/{newname}{FileExt}"

    os.rename(src, dst)     

 #---------------------------------------clear to start again------------------------------------------------


def Clear_this():
    List_Of_Files_To_Rename.clear()
    List_of_files_to_check.Clear()
    List_Of_Files_To_Action.clear()

 #--------------------------------------get the replace text -------------------------------------------------
  
def replacetext():
    Text_TO_Replace.get() 
    Text_To_Replace_With.get() 

     

# -------------------------------------what widgits are needed ----------------------------------------------
textFileButton = Button(root, text="choose Files to rename", command=Files_To_Rename)
btn_run = Button(root, text="Run", command= run_this)
textinfo = Listbox(root)
#file_info = Listbox(root, height= 10)
#runfilemovecheck = Button(root,text= "RUN CHECK", command= file_move_check,)
Cancelprocess = Button(root, text = "CANCEL", command = root.destroy)
Clear = Button(root, text="Clear ALL", command= Clear_this)
#replacethistextlabel = Label(root, text= "find text")
#replacewithtextlabel = Label(root, text= "replace")
#replace_thisText = Entry(root, textvariable = Text_TO_Replace )
#replace_thatText = Entry(root, textvariable = Text_To_Replace_With)

#-------------------------------------where the widgits are placed--------------------------------------------
textFileButton.grid(row=1, column=1, sticky = "ne", padx=10, pady=10)
btn_run.grid(row=4, column=3, sticky = "ne",padx=10, pady=10)
textinfo.grid(row=1, column=2, sticky="nsew", padx=10)
#file_info.grid(row=2, column= 2, sticky="nsew",padx=10, pady=10)
#runfilemovecheck.grid(row=2, column = 1,sticky = "ne",padx=10, pady=10)
Cancelprocess.grid(row = 3,column =2,sticky = "ne",padx=10, pady=10)
Clear.grid(row = 6,column =2,sticky = "ne",padx=10, pady=10)
#replacethistextlabel.grid(row = 3,column =1,sticky = "ne",padx=10, pady=10)
#replacewithtextlabel.grid(row = 3,column =2,sticky = "nw",padx=10, pady=10)
#replace_thisText.grid(row = 4,column =1,sticky = "ne",padx=10, pady=10)
#replace_thatText.grid(row = 4,column =2,sticky = "nw",padx=10, pady=10)

#-------------------------------------renaming files-------------------------------------------------------


root.mainloop()