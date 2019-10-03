# https://pythonprogramming.net/tkinter-tutorial-python-3-event-handling/
# https://instructobit.com/tutorial/51/Python-Tkinter-event-handling
# https://etutorials.org/Programming/Python+tutorial/Part+III+Python+Library+and+Extension+Modules/Chapter+16.+Tkinter+GUIs/16.9+Tkinter+Events/


#https://stackoverflow.com/questions/40641130/how-to-use-a-comboboxselected-virtual-event-with-tkinter

"""
import tkinter as tk
from tkinter import ttk

tkwindow = tk.Tk()

cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.grid(column=0, row=0)

cbox.bind("<<ComboboxSelected>>", print("Selected!"))

tkwindow.mainloop()
"""

"""
import tkinter as tk
from tkinter import ttk

tkwindow = tk.Tk()

cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.grid(column=0, row=0)


def callback(eventObject):
    print(eventObject)

cbox.bind("<<ComboboxSelected>>", callback)

tkwindow.mainloop()
"""
"""
import tkinter as tk
from tkinter import ttk

tkwindow = tk.Tk()

cbox = ttk.Combobox(tkwindow, values=[1,2,3], state='readonly')
cbox.grid(column=0, row=0)

cbox.bind("<<ComboboxSelected>>", lambda _ : print("Selected!"))

tkwindow.mainloop()
"""
# https://www.c-sharpcorner.com/blogs/using-combobox-widget-in-python-gui-application
#Python Combobox Application  
import tkinter as tk  
from tkinter import ttk  

win = tk.Tk()  
#Application Name  
win.title("Python GUI App")  
#Label Creation  
ttk.Label(win, text="Choose the color:").grid(column=0,row=0)  
#Button Action

def click():  
    action.configure(text="chosen color is : "+ numberChosen.get())  

#button Creation
action = ttk.Button(win, text="Click", command=click)  
action.grid(column=1,row=1)  

#Combobox Creation  
number= tk.StringVar()  
numberChosen= ttk.Combobox(win, width=12, textvariable=number)  
#Adding Values  
numberChosen['values']=("Red","Blue","Green")  
numberChosen.grid(column=0,row=1)  
numberChosen.current()  

#Calling Main()  
win.mainloop()


# https://runestone.academy/runestone/books/published/thinkcspy/GUIandEventDrivenProgramming/06_command_events.html

# Python ttk.Combobox() Examples 
# https://www.programcreek.com/python/example/81908/ttk.Combobox


