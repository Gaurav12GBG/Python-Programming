#Write a program to create window in which output is window.
from tkinter import*
def func1():
    var1=e1.get()
    var2=e2.get()

    if var1=="snjb" and var2=="coe":
        print("username and pass is correct")
        top.configure(bg="Green")
        top2 = Tk()
        top2.geometry("500x300")
        top2.configure(bg="#dcdcdc")
        l4=Label(top2,text="Welcome to the SNJB COE",font=60, fg="red").place(x=250,y=150)

    else:
        print("worng info")
        top.configure(bg="Red")



top=Tk()
top.geometry("800x600")
top.configure(bg="#a7d8de")

l1=Label(top,text="Enter the username",bd=5).place(x=100,y=50)
e1=Entry(top)
e1.place(x=250,y=50)
l2=Label(top,text="Enter the password",bd=5).place(x=100,y=100)
e2=Entry(top)
e2.place(x=250,y=100)
l3=Label(top)

b1=Button(top,text="login", activebackground="green",bd=10,bg="yellow", command=func1).place(x=120,y=150)
b2=Button(top,text="signup", activebackground="red",bd=10,bg="cyan").place(x=250,y=150)
cheknbttn=Checkbutton(top, text="Do you want to save the password", onvalue=1, height=2, width=30, fg="green").place(x=120,y=250)
top.mainloop()