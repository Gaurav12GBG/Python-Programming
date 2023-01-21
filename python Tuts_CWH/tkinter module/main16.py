# from tkinter import *
# import mysql.connector
# import tkinter.messagebox

# def insertdata():
#     conn = mysql.connector.connect(host="localhost", user="Root", password="Admin", db="gbgdb")
#     cursor = conn.cursor()
#     n = userName.get()
#     p = password.get()
#     cursor.execute("insert into gbgtb (Username, Password) values(%s, %s)", (n, p))
#     conn.commit()
#     tkinter.messagebox.showinfo("Traveler Info", "Data inserted successfully...!!!")

# root=Tk()
# root.geometry('500x500')
# root.title("Database Demo")

# l1 = Label(root, text="Enter the name")
# l1.place(x=50, y=20)

# userName = Entry(root, width=50)
# userName.place(x=150, y=20)


# l2 = Label(root, text="Enter the pass")
# l2.place(x=50, y=50)

# password = Entry(root, width=50)
# password.place(x=150, y=50)


# mybtn = Button(root, text="insert data", command=insertdata)
# mybtn.place(x=150, y=80)


# root.mainloop()