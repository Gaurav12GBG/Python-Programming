# canvas Widget :

from tkinter import *
root = Tk()
canvas_width = 800
canvas_height = 400
root.geometry(f'{canvas_width}x{canvas_height}')

can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# The line goes from the point x1, y1 and x2, y2 :

# can_widget.create_line(200, 0, 50, 200)

# To create a rectangle specify parameter in this order - coors of top left and coors of bottom right :
can_widget.create_rectangle(3, 5, 700, 300, fill='black')

can_widget.create_text(350, 150, text="Hii, I am a GBG", font="comicsansms 45 bold", fill='yellow')
can_widget.create_line(0, 200, 500, 200, fill='yellow')


can_widget.create_oval(500, 100, 200, 80, fill='red')


root.mainloop()