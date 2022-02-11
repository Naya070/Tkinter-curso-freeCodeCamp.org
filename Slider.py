
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sliders")
root.geometry("400x400") #Tamaño del root

def slide(var):
    my_label = Label(root, text=horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

horizontal = Scale(root, from_=0, to = 400, orient= HORIZONTAL, command=slide)
horizontal.pack()

my_label = Label(root, text = horizontal.get()).pack()


my_btn = Button(root, text = "Click Me", command= slide).pack()

root.mainloop()