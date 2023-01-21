# import datetime
# from tkinter import *
# import tkinter.messagebox
# import mysql.connector
# import datetime

# def insertdata():
#     conn = mysql.connector.connect(host="localhost", user="Root", password="Admin", db="gbgdb")
#     cursor = conn.cursor()
#     a = e1.get()
#     b = e2.get()
#     c = e3.get()
#     d = e4.get()
#     e = e5.get()
#     f = e6.get()
#     g = datetime.datetime.now()
#     cursor.execute("insert into traveler_info1 (Name, Phone_Number, Gender, Emergency_Contact, Payment_Mode, Payment_History, TimeStamp) values(%s, %s, %s, %s, %s, %s, %s)", (a, b, c, d, e, f, g))
#     conn.commit()
#     tkinter.messagebox.showinfo("Traveler Info", "Data inserted successfully...!!!")
#     conn.close()

# def deletedata():
#     pass

# root = Tk()
# root.title("Databse connection")
# root.geometry('655x355')

# frame = Frame(root, borderwidth=1, relief=SUNKEN, width=500, height=300, bg="lightgrey")
# frame.place(anchor=CENTER, x=325, y=180)

# l = Label(frame, text="Welcome in GBG Travels", font="comisansms 15 bold", bg="lightgrey")
# l.place(x=130, y=20)

# l1 = Label(frame, text="Name", font="comisansms 10 bold", bg="lightgrey")
# l1.place(x=90, y=70)

# l2 = Label(frame, text="Phone", font="comisansms 10 bold", bg="lightgrey")
# l2.place(x=90, y=100)

# l3 = Label(frame, text="Gender", font="comisansms 10 bold", bg="lightgrey")
# l3.place(x=90, y=130)

# l4 = Label(frame, text="Emergency Contact", font="comisansms 10 bold", bg="lightgrey")
# l4.place(x=90, y=160)

# l5 = Label(frame, text="Payment Mode", font="comisansms 10 bold", bg="lightgrey")
# l5.place(x=90, y=190)

# l6 = Label(frame, text="Payment Paided", font="comisansms 10 bold", bg="lightgrey")
# l6.place(x=90, y=220)


# e1 = Entry(frame, borderwidth=1, font="comicsansms 10 bold", relief=SUNKEN, width=25)
# e2 = Entry(frame, borderwidth=1, font="comicsansms 10 bold", relief=SUNKEN, width=25)
# e3 = Entry(frame, borderwidth=1, font="comicsansms 10 bold", relief=SUNKEN, width=25)
# e4 = Entry(frame, borderwidth=1, font="comicsansms 10 bold", relief=SUNKEN, width=25)
# e5 = Entry(frame, borderwidth=1, font="comicsansms 10 bold", relief=SUNKEN, width=25)
# e6 = Entry(frame, borderwidth=1, font="comicsansms 10 bold", relief=SUNKEN, width=25)

# e1.place(x=230, y=70)
# e2.place(x=230, y=100)
# e3.place(x=230, y=130)
# e4.place(x=230, y=160)
# e5.place(x=230, y=190)
# e6.place(x=230, y=220)

# btn1 = Button(frame, text="Insert Data", bg="green", font="comicsansms 8 bold", width=10, command=insertdata)
# btn2 = Button(frame, text="Delete Data", bg="red", font="comicsansms 8 bold", width=10, command=deletedata)

# btn1.place(x=230, y=250)
# btn2.place(x=330, y=250)

# root.mainloop()
