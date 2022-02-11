from cProfile import label
from tkinter import *

def myClick():
    MyLabel = Label(root, text= "Look, I clicked a bottom")
    MyLabel.pack()

root = Tk() #root será la ventana o base 
#en donde irán los otros elementos o widgets

myButton1 = Button(root, text= "Don't click me!", state= DISABLED
)
myButton2 = Button(root, text= "Click me!", command= myClick, fg = "white", bg = "blue")

myButton1.pack()
myButton2.pack()
#Loop principal para que funcione la ventana
root.mainloop()