# Accepting the values from the Travel form and store it into the file  :

from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox
import datetime


def gettime():
    return datetime.datetime.now()

root = Tk()
root.geometry('644x344')
root.title('Travelling Form')


# Fuctionality for our form :
def getvals():
    with open("Traveler.txt", "a") as f:
        f.write(
            str([str(gettime())]) +
            f'''{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get()
        ,paymentmodevalue.get()}\n''')
        tkinter.messagebox.showinfo("Traveler Info", "Successfully added")


# Frame for our form :
frame = Frame(root,
              borderwidth=1,
              relief=SUNKEN,
              pady=20,
              padx=20,
              bg='lightgrey')
frame.pack(anchor=CENTER, fill=Y, pady=50)

# Heading :
Label(frame,
      text="Welcome to VBG`s Travels",
      font="comicsansms 13 bold",
      pady=5,
      bg='lightgrey').grid(row=0, column=3)

# Text for our form :
name = Label(frame, text='Name', bg='lightgrey', font='comicsansms 9 bold')
phone = Label(frame, text='Phone', bg='lightgrey', font='comicsansms 9 bold')
gender = Label(frame, text='Gender', bg='lightgray', font='comicsansms 9 bold')
emergency = Label(frame,
                  text='Emergency Contact',
                  bg='lightgrey',
                  font='comicsansms 9 bold')
paymentmode = Label(frame,
                    text='Payment Mode',
                    bg='lightgrey',
                    font='comicsansms 9 bold')

# Pack text for our form using Grid() :
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)

# Tkinter variable for storing entries :
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
foodservicevalue = IntVar()

# Entries for our form :
nameentry = Entry(frame,
                  textvariable=namevalue,
                  font='comicsansms 9 bold',
                  width=21)
phoneentry = Entry(frame,
                   textvariable=phonevalue,
                   font='comicsansms 9 bold',
                   width=21)
gendercombo = Combobox(frame,
                       values=['Select', 'male', 'Female'],
                       textvariable=gendervalue,
                       font='comicsansms 9 bold',
                       width=18)
emergencyentry = Entry(frame,
                       textvariable=emergencyvalue,
                       font='comicsansms 9 bold',
                       width=21)
paymentmodecombo = Combobox(frame,
                            values=[
                                'Select Mode', 'Debit Card', 'Paytm',
                                'Phone Pay', 'Google Pay', 'Cash', 'Checks',
                                'NetBanking'
                            ],
                            textvariable=paymentmodevalue,
                            font='comicsansms 9 bold',
                            width=18)

# Packing the entries for our form using grid() :
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
gendercombo.grid(row=3, column=3)
gendercombo.current(0)
emergencyentry.grid(row=4, column=3)
paymentmodecombo.grid(row=5, column=3)
paymentmodecombo.current(0)

# CheckBox and packing it :
foodservice = Checkbutton(frame,
                          text="Want to prebook your meals?",
                          variable=foodservicevalue,
                          bg='lightgrey',
                          font='comicsansms 9 bold')
foodservice.grid(row=6, column=3)

# Button and packing it and assigning it a command :
Button(frame,
       text="Submit to VBG`s Travel",
       command=getvals,
       bg='lightgrey',
       font='comicsansms 9 bold').grid(row=7, column=3)

root.mainloop()