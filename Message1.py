from cProfile import label
from pydoc import text
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("message")

#Diferentes ventanas:
# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    messagebox.showinfo("This is my pop-up!", "Hello world!")
    

Button(root, text = "Pop-up", command=popup).pack()

mainloop()