

from tkinter import*
def func1():
    var1=int(e1.get()) #add
    var2=int(e2.get())
    res=var1+var2
    l1.config(text=res)
def func2():
    var1 = int(e1.get())  # substract
    var2 = int(e2.get())
    res = var1 - var2
    l1.config(text=res)
def func3():
    var1 = int(e1.get())  #multi
    var2 = int(e2.get())
    res = var1 * var2
    l1.config(text=res)
def func4():
    var1 = int(e1.get())  # divison
    var2 = int(e2.get())
    res = var1 % var2
    l1.config(text=res)


top=Tk()
top.geometry("800x600")
top.configure(bg="#a7d8de")

#input 1st number
e1=Entry(top)
e1.place(x=50,y=50)

#input 2nd number
e2=Entry(top)
e2.place(x=50,y=100)

#printing res on l1
l1=Label(top,text="result=",bg="yellow")
l1.place(x=200,y=75)

b1=Button(top,text="Addition", activebackground="green",bd=10,bg="red", command=func1).place(x=120,y=150)
b2=Button(top,text="Substraction", activebackground="green",bd=10,bg="green", command=func2).place(x=220,y=150)
b3=Button(top,text="Multiplication", activebackground="green",bd=10,bg="pink", command=func3).place(x=340,y=150)
b4=Button(top,text="Division", activebackground="green",bd=10,bg="blue", command=func4).place(x=460,y=150)

top.mainloop()