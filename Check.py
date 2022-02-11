from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkboxes")
root.geometry("400x400") #Tamaño del root

def show():
    myLabel = Label(root, text = var.get()).pack()

var = StringVar() #variable var entero

c = Checkbutton(root, text= "Check this box, I dare you", variable= var, onvalue = "On", offvalue= "Off")
c.deselect()
c.pack()
#La variable es la misma var = IntVar()

myButton = Button(root, text = "Show Selection", command = show).pack()

root.mainloop()