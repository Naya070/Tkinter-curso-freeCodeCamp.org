from logging import root
from pydoc import text
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open files dialog box")


def open():
    global my_image
    root.filename = filedialog.askopenfilename(initialdir= "/home/naya/Documentos/programacion/Tkinter con gringo/images", title="Select A File", filetypes=(("jpg files", "*.jpg"),("all files", "*.*")))
    my_label = Label(root, text = root.filename).pack()
    my_image = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image = my_image, width= 900, height= 450).pack()

my_btn = Button(root, text= "Open File", command = open).pack()

root.mainloop()