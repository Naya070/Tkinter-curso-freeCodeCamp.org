from ssl import Options
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
root.geometry("400x400") #Tamaño del root

#Drop Down Boxes

def show():
    myLabel = Label(root, text= clicked.get()).pack()

options = [
    "Monday", 
    "Tuesday", 
    "Wednesday", 
    "Thursday", 
    "Friday"
]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options )
drop.pack()

myButton = Button(root, text= "show selection", command= show).pack()

root.mainloop()