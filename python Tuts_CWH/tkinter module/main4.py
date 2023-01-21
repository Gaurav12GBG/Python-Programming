# Displaying image using labels in tkinter :

from tkinter import *
from PIL import Image, ImageTk         # After installing pillow import this

root = Tk()
root.geometry('1200x675')
root.title('Displaying Image on GUI')

# In tkinter only png image allowed
# photo = PhotoImage(file="python.png")

# for jpg image install pillow module
image = Image.open("python.png")
photo = ImageTk.PhotoImage(image)

mylabel = Label(root, image=photo)
mylabel.pack()

root.mainloop()