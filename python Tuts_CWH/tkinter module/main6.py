"""
Frame :- A frame widget is a rectangular region on the screen which can be used as a foundation class to implement
        complex widgets.
       - This widget is very important for the process of grouping and organizing other widgets in a friendly way.
       - It works like a container , which is responsible for arranging the position of other widgets.
       - We can use bg, relief, borderwidth, bd as the attributes of frame widget.
       - Some important attributes are discussed below :
         1) bg : The normal background color displayed behind the label and indicator.
         2) relief :- The type of border of the frame.
                    - Its default value is FLAT.
                    - We can set it to any other styles i.e FLAT, RAISED, SUNKEN, GROOVE, RIDGE.
         3) borderwidth :- Tkinter label doesnt have any border by default.
                         - We need to assign the borderwidth option to add a border around label widget along with the
                           relief option to be any option rather than flat to make visible.
         4) bd : The size of the border around the indicator. Default is 2 pixels.
"""
from tkinter import *
root = Tk()
root.geometry("655x333")
root.title('Pycharm Editor !!!')

f1 = Frame(root, bg='darkblue', borderwidth=10, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, borderwidth=8, bg='darkblue', relief=SUNKEN)
f2.pack(side=TOP, fill=X)

f3 = Frame(root, bg="skyblue")
f3.pack(pady=0, fill=BOTH)

l = Label(f1, text="Project Tkinter - pycharm", font="Teko 9 bold", borderwidth=8, relief=SUNKEN, bg='skyblue')
l.pack(side=TOP, pady=12, padx=5)

l = Label(f2, text="Welcome to Tkinter project - On Pycharm...", font="Teko 9 bold", borderwidth=5, relief=SOLID,
          bg='skyblue', pady=15)
l.pack(side=TOP, pady=12, padx=5)

l = Text(f3, font="Teko 15 bold", bg='skyblue', width=655, height=333, )
l.pack(fill=BOTH)

root.mainloop()