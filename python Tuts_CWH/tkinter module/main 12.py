# Message box :
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('544x244')
root.title("Menus and submenues")


def myFunc():
    print("Its work")


def help():
    print("I will help you")
    tmsg.showinfo('Help', 'GBG will help you with this GUI')


def Rate():
    print("Rate Us")
    value = tmsg.askquestion("Was your experience Good?",
                             "You use this GUI....Was your experience Good?")
    if value == 'yes':
        msg = "Great. Rate us on appstore please!!"
    else:
        msg = "Tell us what went wrong. We will call you soon"
    tmsg.showinfo("Experience", msg)


# Use these to create a non dropdown menu :

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myFunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)

# First Menus :
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New Project..", command=myFunc)
m1.add_command(label="New..", command=myFunc)
m1.add_command(label="New Scratch File", command=myFunc)
m1.add_separator()
m1.add_command(label="Save", command=myFunc)
m1.add_command(label="Save As", command=myFunc)
m1.add_separator()
m1.add_command(label="Print", command=myFunc)
m1.add_command(label="Rename File", command=myFunc)
root.config(menu=mainmenu)

mainmenu.add_cascade(label="File", menu=m1)

# Second Menus :
m2 = Menu(mainmenu, tearoff=0)
m2.add_command(label="Cut..", command=myFunc)
m2.add_command(label="Copy..", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
m2.add_command(label="Delete", command=myFunc)

m2.add_separator()
m2.add_command(label="Find", command=myFunc)
m2.add_command(label="Find Usage", command=myFunc)
m2.add_separator()
m2.add_command(label="Select All", command=myFunc)
m2.add_command(label="Replace", command=myFunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Edit", menu=m2)

# Third Menus
m3 = Menu(mainmenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate Us", command=Rate)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="Help", menu=m3)

root.mainloop()
