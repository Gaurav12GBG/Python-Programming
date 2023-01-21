from tkinter import *
import tkinter.font as font

root = Tk()
root.title("myCalculator")
root.geometry('700x300')
# root.configure(background='black')
# root.attributes('-alpha', 0.9)    # u can make it as a transparent

myFont = font.Font(family='Helvetica', size=12, weight='bold')

# Functionality use when button click
def call_result():
    n1 = e1.get()
    n2 = e2.get()
    res = int(n1) + int(n2)
    result_label.config(text="The Addition is = %d" % res)

l = Label(root, text="Welcome in our calculator for addtion operation :", fg="darkblue")
l.place(x=50, y=20)
l['font'] = myFont

l1 = Label(root, text="Enter the number 1:", fg="darkred")
l1.place(x=50, y=50)
l1['font'] = myFont

l2 = Label(root, text="Enter the number 2:", fg="darkred")
l2.place(x=50, y=70)
l2['font'] = myFont

e1 = Entry(root, width=15, fg="darkgreen")
e1.place(x=205, y=50)
# e1.configure(background="white", border='2')
e1['font'] = myFont

e2 = Entry(root, width=15, fg="darkgreen" )
e2.place(x=205, y=70)
# e2.configure(background="white",border=2)
e2['font'] = myFont

b1 = Button(root, text="ADD", bg="Red", fg="white", command=call_result)
b1.place(x=205, y=100)
b1['font'] = myFont

result_label = Label(root, fg='purple')
result_label.place(x=205, y=150)
result_label['font'] = myFont

Error_label = Label(root, fg='red')
Error_label.place(x=205, y=150)
Error_label['font'] = myFont


root.mainloop()