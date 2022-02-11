from cProfile import label
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images App")
#root.iconbitmap('/home/naya/Documentos/programacion/Tkinter con gringo/ico.ico')
button_quit = Button(root, text = "Exit Program", command = root.quit)
button_quit.pack()

my_img = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_label= Label(image=my_img)
my_label.pack()

root.mainloop()

#Problema sin resolver: colocar favicon de imagen ico.ico en la ventana root.