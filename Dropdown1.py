from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
root.geometry("400x400") #Tamaño del root

#Drop Down Boxes

def show():
    myLabel = Label(root, text= clicked.get()).pack()

clicked = StringVar()
clicked.set("Monday")

drop = OptionMenu(root, clicked, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
drop.pack()

myButton = Button(root, text= "show selection", command= show).pack()

root.mainloop()