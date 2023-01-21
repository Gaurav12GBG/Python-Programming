from tkinter import *

top=Tk()
Lb1=Listbox(top,selectmode=MULTIPLE,bg="purple")
Lb1.insert(1, "India")
Lb1.insert(2, "Aus")
Lb1.insert(3, "Jpn")
Lb1.insert(4, "Shrilanka")
Lb1.insert(5, "bankok")


#b1=Button(top, text="Print Selcetion", command=selectmode)
#b1.pack()
Lb1.pack()


top.mainloop()