# Travel form using checkbuttons, Entry widget with database connection(insert, delete) :

from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Combobox
import mysql.connector

# Fuctionality for our form :
def insertdata():
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="gbg_travels")
    cursor = conn.cursor()
    a = nameentry.get()
    b = phoneentry.get()
    c = gendercombo.get()
    d = emergencyentry.get()
    e = paymentmodecombo.get()
    f = paymentpaidedentry.get()
    # g = foodservice.get()
    cursor.execute("insert into Traveler_Info (Name,Phone Number,Gender,Emergency Contact,Payment Mode,Payment History) Values(%s%s%s%s%s%s)",(a, b, c, d, e, f))
    conn.commit()
    tkinter.messagebox.showinfo("Traveler Info", "Data inserted successfully...!!!")

root = Tk()
root.geometry('644x344')
root.title('Travelling Form')

frame = Frame(root, borderwidth=1, relief=SUNKEN, pady=20, bg='lightgrey')
frame.pack(anchor=CENTER, fill=Y, pady=40)

# Heading :
Label(frame, text="Welcome to GBG`s Travels", font="comicsansms 13 bold", pady=5, bg='lightgrey').grid(row=0, column=3)

# Text for our form :
name = Label(frame, text='Name', bg='lightgrey', font='comicsansms 9 bold')
phone = Label(frame, text='Phone', bg='lightgrey', font='comicsansms 9 bold')
gender = Label(frame, text='Gender', bg='lightgrey', font='comicsansms 9 bold')
emergency = Label(frame, text='Emergency Contact', bg='lightgrey', font='comicsansms 9 bold')
paymentmode = Label(frame, text='Payment Mode', bg='lightgrey', font='comicsansms 9 bold')
paymentpaided = Label(frame, text='Payment Paided', bg='lightgrey', font='comicsansms 9 bold')

# Pack text for our form using Grid() :
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmode.grid(row=5, column=2)
paymentpaided.grid(row=6, column=2)


# Tkinter variable for storing entries :
namevalue = StringVar()
phonevalue = StringVar()
gendervalue = StringVar()
emergencyvalue = StringVar()
paymentmodevalue = StringVar()
paymentpaidedvalue = StringVar()
foodservicevalue = StringVar()

# Entries for our form :
nameentry = Entry(frame, textvariable=namevalue, font='comicsansms 9 bold', width=21)
phoneentry = Entry(frame,  textvariable=phonevalue, font='comicsansms 9 bold', width=21)
gendercombo = Combobox(frame, values=['Select', 'male', 'Female'], textvariable=gendervalue, font='comicsansms 9 bold', width=18)
emergencyentry = Entry(frame,  textvariable=emergencyvalue, font='comicsansms 9 bold', width=21)
paymentmodecombo = Combobox(frame, values=['Select Mode', 'Debit Card', 'Paytm', 'Phone Pay', 'Google Pay', 'Cash', 'Checks', 'NetBanking'], textvariable=paymentmodevalue,font='comicsansms 9 bold', width=18)
paymentpaidedentry = Entry(frame,  textvariable=paymentpaidedvalue, font='comicsansms 9 bold', width=21)

# Packing the entries for our form using grid() :
nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
gendercombo.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmodecombo.grid(row=5, column=3)
paymentpaidedentry.grid(row=6, column=3)

# CheckBox and packing it :
foodservice = Checkbutton(frame, text="Want to prebook your meals?", variable=foodservicevalue, bg='lightgrey', font='comicsansms 9 bold')
foodservice.grid(row=7, column=3)

# Button and packing it and assigning it a command :
Button(frame, text="Submit to GBG`s Travel", command=insertdata, bg='lightgrey', font='comicsansms 9 bold').grid(row=8, column=3)

# Button(frame, text="Submit to GBG`s Travel", command=insertdata, bg='lightgrey', font='comicsansms 9 bold').grid(row=8, column=4)

root.mainloop()