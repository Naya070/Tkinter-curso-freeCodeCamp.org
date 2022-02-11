from sqlite3 import Row
from tkinter import *

root = Tk() #root será la ventana o base 
#en donde irán los otros elementos o widgets

#Crear etiqueta
myLabel1 = Label(root, text = "Hello World")
myLabel2 = Label(root, text = "Me llamo Naya :D")
myLabel3 = Label(root, text = "                    ")

#Mostrar etiqueta
myLabel1.grid(row = 0, column = 1)
myLabel2.grid(row = 2, column =0)
myLabel3.grid(row=1, column=0)

#La etiqueta también se puede poner así:
#myLabel1 = Label(root, text = "Hello World").myLabel1.grid(row = 0, column = 1)

#Loop principal para que funcione la ventana
root.mainloop()