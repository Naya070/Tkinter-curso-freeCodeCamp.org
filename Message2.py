from cProfile import label
from pydoc import text
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

root = Tk()
root.title("message")

#Diferentes ventanas:
# showinfo(Ok = "ok"),
#  showwarning(Ok = "ok"),
#  showerror(Ok = "ok"), 
# askquestion(Yes = "yes", No = "no"),
#  askokcancel (ok =1, cancel =0),
#  askyesno (yes =1, no =0)

def popup():
  response =  messagebox.askyesno("This is my pop-up!", "Hello world!")
  Label(root, text = response).pack()
  if response == 1:
      Label(root, text = "You click Yes!").pack()
  else:
      Label(root, text = "You click No!").pack()

Button(root, text = "Pop-up", command=popup).pack()

mainloop()