from tkinter import *

root = Tk() #root será la ventana o base 
#en donde irán los otros elementos o widgets

#Crear etiqueta
myLabel = Label(root, text = "Hello World")
#Mostrar etiqueta
myLabel.pack()

#Loop principal para que funcione la ventana
root.mainloop()