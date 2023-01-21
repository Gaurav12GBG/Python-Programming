"""
Entry widget :- Entry widget are the basic widget of tkinter which is used to get input, i.e text strings, from the
                user of an application. This widget allows the user to enter a single line of text.

Grid() Layout :- The Grid() manager is the most flexible of the geometry managers in tkinter.
               - The Grid() geometry manager puts the widgets in a 2D table.
               - The master widget is split into a number of rows and columns , and each "cell" in the resulting table
                 can hold a widget.
"""
from tkinter import *

root = Tk()
root.geometry('655x333')
root.title('Entry widget and Grid layout')

def getvals():
   n1 = uservalue.get()
   n2 = passvalue.get()
   result_label.config(text=f'username = {n1}')
   result_label2.config(text=f'Password = {n2}')
   return

user = Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid()

# Variable classes in tkinter :
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
passentry = Entry(root, textvariable=passvalue)
userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

Button(text="Submit", command=getvals, fg='red', relief=SUNKEN).grid(row=2, column=1)

result_label = Label(root, text='Your username and password comes here:', fg='darkblue')
result_label.grid(row=3, column=1)

result_label2 = Label(root, fg='darkblue')
result_label2.grid(row=4, column=1)

root.mainloop()