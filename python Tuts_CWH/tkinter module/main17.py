# import datetime
# from tkinter import *
# import mysql.connector as sql
# import tkinter.messagebox
# import datetime


# def insertdata():
#     conn = sql.connect(host="localhost", user="Root", password="Admin", db="gbgdb")
#     cursor = conn.cursor()
#     a = e1.get()
#     b = e2.get()
#     c = datetime.datetime.now()
#     cursor.execute("insert into notes (Title, Description, TimeStamp) values(%s, %s, %s)", (a, b, c))
#     conn.commit()
#     tkinter.messagebox.showinfo("Traveler Info", "Data Inserted successfully...!!!")
#     conn.close()

# def deletedata():
#     conn = sql.connect(host="localhost", user="Root", password="Admin", db="gbgdb")
#     cursor = conn.cursor()
#     n = e1.get()
#     cursor.execute("delete from notes where Title like %s", (n,))
#     conn.commit()
#     tkinter.messagebox.showinfo("Traveler Info", "Data Deleted successfully...!!!")
#     conn.close()


# # def updatedata():
# #     conn = sql.connect(host="localhost", user="Root", password="Admin", db="gbgdb")
# #     cursor = conn.cursor()
# #

# root = Tk()
# root.geometry('500x500')
# root.title("Add Notes")

# Label(root, text="Add Notes...", font="comicsansms 15 bold").place(x=250, y=60)
# l1 = Label(root, text="Title")
# l2 = Label(root, text="Description")
# l1.place(x=100, y=100)
# l2.place(x=100, y=130)

# e1 = Entry(root, width=40)
# e2 = Entry(root, width=40)
# e1.place(x=200, y=100)
# e2.place(x=200, y=130)

# b1 = Button(root, text="Add Note", bg="green", command=insertdata)
# b2 = Button(root, text="Delete Note", bg="red", command=deletedata)
# b3 = Button(root, text="Update Note", bg="blue")
# b1.place(x=200, y=160)
# b2.place(x=278, y=160)
# b3.place(x=365, y=160)



# root.mainloop()
