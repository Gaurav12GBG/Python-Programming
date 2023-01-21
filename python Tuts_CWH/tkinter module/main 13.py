# Sliders in Tkinter :
from tkinter import *
import tkinter.messagebox as tmsg

root = Tk()
root.geometry('455x233')
root.title('slider tutorial')

def getdollar():
    print(f"We have credited {myslider2.get()} dollars to your bank account")
    tmsg.showinfo("Banking Credit Info", f"We have credited {myslider2.get()} dollars to your bank account")

# myslider = Scale(root, from_=0, to=100)
# myslider.pack()

Label(root, text="How many dollars do you want?").pack()
myslider2 = Scale(root, from_=0, to=100, orient=HORIZONTAL, tickinterval='50')
myslider2.pack()

Button(root, text="Get Dollars!", pady=10, command=getdollar, bg='black', fg='white', borderwidth=6).pack(pady=12)

root.mainloop()