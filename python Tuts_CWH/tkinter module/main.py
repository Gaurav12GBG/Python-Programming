from tkinter import *
import tkinter.font as font

root = Tk(className=' Best Gym in Chandwad')
root.geometry('500x500')
# root.attributes("-alpha", 0.8)      We can make the window transperent

# define font
myFontx = font.Font(family='Helvetica', size=12, weight='bold')
myFonty = font.Font(family='Helvetica', size=10, weight='bold')
myFontb1 = font.Font(family='Helvetica', size=8, weight='bold')

# Add widgets in GUI
x = Label(root, text="Welcome to best Gym in Chandwad", fg="darkblue")
x.pack()
x['font'] = myFontx

y = Label(root, text="To join this gym kindly click on below button to register for same..", fg="Red")
y.pack()
y['font'] = myFonty

b1 = Button(root, text="Click Me/Register", bg="Darkblue", fg="white")
b1.pack(padx=0, pady=10)
b1['font'] = myFontb1

b2 = Button(root, text="Login", bg="red", fg="white")
b2.pack(padx=20, pady=0)    # set the margin to the button
b2['font'] = myFontb1


root.mainloop()


