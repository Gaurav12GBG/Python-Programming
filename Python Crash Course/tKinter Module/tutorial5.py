#Write a program to check username and password.username password is correct then create a new window.
from pydoc import classname
from tkinter import*

from tkinter import*
gui1=Tk(className="First window")
def func1():
    var1=username.get()
    var2=password.get()
    
    if var1=="Snjb" and var2=="coe":
        print("You have enter correct username and password")
        gui1.configure(bg="cyan")
        gui2 = Tk(className="second window")
        gui2.configure(bg="pink")
        gui2.geometry("500x300")
        
        l3=Label(gui2,text="Welcome to Snjbcoe",font=("Helvetika",20)).place(x=100,y=200)
        
    else:
        print("Incorrect username and password")
        gui1.configure(bg="green")
        
        
gui1.geometry("700x500")
gui1.configure(bg="orange")

l1=Label(gui1,text="Enter your username :").place(x=100,y=200)
username=Entry(gui1)
username.place(x=250,y=200)

l2=Label(gui1,text="Enter your password :").place(x=100,y=250)
password=Entry(gui1)
password.place(x=250,y=250)

b1=Button(gui1,text="Login",activebackground="green",activeforeground="yellow",bd=10,command=func1).place(x=250,y=300)
b2=Button(gui1,text="clear",activebackground="red",activeforeground="yellow",bd=10,command=func1).place(x=320,y=300)
gui1.mainloop()