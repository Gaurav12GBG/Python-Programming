from tkinter import*
root=Tk()
root.title("Login form")
root.geometry("700x500")

root.attributes('-alpha',0.6)
root.configure(bg="cyan")

l1=Label(root,text="Enter your username",bd=5).place(x=120,y=30)
l2=Label(root,text="Enter your password",bd=5).place(x=120,y=70)
l3=Label(root,text="Enter your email",bd=5).place(x=120,y=110)

e1=Entry(root).place(x=270,y=110)
e2=Entry(root).place(x=270,y=70)
e3=Entry(root,show='*').place(x=270,y=110)

b1=Button(root,text="Login",bg="green",foreground="black",bd=5).place(x=180,y=150)
b2=Button(root,text="Clear",bg="red",foreground="black",bd=5).place(x=240,y=150)

c1=Checkbutton(root,text="do you want to save the password").place(x=150,y=190)

root.mainloop()
