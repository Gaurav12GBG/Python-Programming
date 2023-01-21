from tkinter import *
from tkinter.ttk import Combobox


root = Tk()
root.title('widgets in tkinter')
root.geometry('700x500')

def myResult():
    # This code for only multiline area.....
    # data = txt.get(1.0, END)
    # result_label.config(text=data)
    # return

    # This code for only listbox.....
    # data = " "
    # for i in lst.curselection():
    #     data = data + lst.get(i)
    #     result_label.config(text=data)
    # return

    # This code for only Combobox....
    data = cmb.get()
    result_label.config(text=data)
    return

l1 = Label(root, text="Multiline Text Area", fg='darkblue', font='Teko')
l1.pack()
txt = Text(root, width=30, height=10)
txt.pack()

l2 = Label(root, text="Listbox",  fg='darkblue', font='Teko')
l2.pack()
lst = Listbox(root, selectmode=MULTIPLE)
lst.insert(1, 'C language')
lst.insert(2, 'C++ language')
lst.insert(3, 'python language')
lst.insert(4, 'php language')
lst.pack()

l3 = Label(root, text="Combobox",  fg='darkblue', font='Teko')
l3.pack()
cmb = Combobox(root, values=['india', 'Pakistan', 'USA', 'Japan'])
cmb.pack()

b1 = Button(root, text="Click Here", fg='white', font='Teko', bg='red', command=myResult)
b1.pack()

result_label = Label(root, text='Your result display here',fg='darkblue', font='Teko' )
result_label.pack()

root.mainloop()