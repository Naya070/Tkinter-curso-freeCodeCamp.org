from pydoc import text
from tkinter import *
from turtle import width
from PIL import ImageTk, Image

root = Tk()
root.title("Create new windows in tkinter")

def open():
    global my_img #Poner la variable como global, si no, no se mostrará en la ventana top.
    top = Toplevel() #la nueva ventana
    top.title("My Second window")

    my_img = ImageTk.PhotoImage(Image.open("images/1.jpg"))
    my_label = Label(top, image= my_img, width=1000, height=500).pack()
    btn2 = Button(top, text = "Close window", command= top.destroy).pack()
    #Los widgets reposan sobre la ventana llamada top.


btn = Button(root, text= "Open Second Window", command = open).pack()

mainloop()