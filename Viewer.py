from cProfile import label
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Images App")
#root.iconbitmap('/home/naya/Documentos/programacion/Tkinter con gringo/ico.ico')

#Cargamos las imagenes en las variables my_imgx
my_img1 = ImageTk.PhotoImage(Image.open("images/1.jpg")) 
my_img2 = ImageTk.PhotoImage(Image.open("images/2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("images/3.jpg"))

#Creamos una lista de dichas variables
image_list = [my_img1, my_img2, my_img3]

#Creamos una etiqueta en donde se visualizarán las imágenes.
#Las imágenes deben ser montadas sobre un widget o no se verán.
my_label= Label(image=my_img1, width=1080, height=500) #Estamos en la imagen 1 al iniciar.
my_label.grid(row=0, column=0, columnspan = 3) #Posicionamos la etiqueta

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget() #Oculta la capa en donde está la imagen por ende, oculta la imagen.
    my_label = Label(image= image_list[image_number-1], width=1080, height=500) #Esta será la nueva imagen.
    button_forward = Button(root, text= ">>", command= lambda: forward(image_number+1))
    button_back = Button(root, text= "<<", command= lambda: back(image_number-1))
    #Se crean los botones con sus funciones

    if image_number == 3:
        button_forward = Button(root, text= ">>", state= DISABLED)
        #Se desabilita el botón >> si ya estamos en la última imagen

    my_label.grid(row=0, column=0, columnspan = 3) #Se posicionan y muestran los elementos
    button_back.grid(row= 1, column=0)
    button_forward.grid(row=1, column=2)

def back(image_number):
     global my_label
     global button_forward
     global button_back

     my_label.grid_forget()
     my_label = Label(image= image_list[image_number-1], width=1080, height=500)
     button_forward = Button(root, text= ">>", command= lambda: forward(image_number+1))
     button_back = Button(root, text= "<<", command= lambda: back(image_number-1))

     if image_number == 1:
        button_back = Button(root, text= "<<", state= DISABLED)
        #Se desabilita el botón << si estamos en la primera imagen

     my_label.grid(row=0, column=0, columnspan = 3)
     button_back.grid(row= 1, column=0)
     button_forward.grid(row=1, column=2)
     #Posicionar y mostrar elementos


#Crear elementos
button_back = Button(root, text= "<<", command= back, state= DISABLED)
#Este botón estará desabilitado al comienzo, ya que se empieza por la primera imagen 
#y no hay a donde retroceder.
button_exit = Button(root, text= "EXIT PROGRAM", command = root.quit)
button_forward = Button(root, text= ">>", command= lambda: forward(2))

#Posicionar elementos y mostrar en pantalla.
button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_forward.grid(row=1, column=2)

root.mainloop()

#Problema sin resolver: colocar favicon de imagen ico.ico en la ventana root.