# Radiobutton Tutorial:
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('455x233')
root.title('Radiobutton tutorial')

def order():
    tmsg.showinfo("Order Received!", f"We have recorded your order of {var.get()}. Thanks for ordering")

# var = IntVar()
var = StringVar()
var.set("Radio")

Label(root, text="What would you like to have sir?", font="lucida 19 bold", justify=LEFT, padx=14).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor="w")
radio = Radiobutton(root, text="Edly", padx=14, variable=var, value="Edly").pack(anchor="w")
radio = Radiobutton(root, text="Paratha", padx=14, variable=var, value="Paratha").pack(anchor="w")
radio = Radiobutton(root, text="Samosa", padx=14, variable=var, value="Samosa").pack(anchor="w")

Button(root, text="Order Now", command=order).pack()

root.mainloop()