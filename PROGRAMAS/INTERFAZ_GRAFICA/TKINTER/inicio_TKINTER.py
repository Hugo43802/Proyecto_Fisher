from tkinter import *
# from tkinter.ttk import *


# Instacia window de la clase TK
ventana = Tk()

# Realizar un hola mundo
saludo = Label(
    text= "Colocar el Nombre: ",
    foreground= "black",
    background="grey",
    width= 25,
    height= 3
    # Las medidas de alto y ancho, son tomadas por las unides de texto
    )
saludo.place(x=0,y=0)
saludo.pack()

# Entrada de texto

entrada = Entry(
    width=50
)

entrada.pack()

# generar boton
button = Button(
    text="Dar clic",
    width=25,
    height=5,
    bg="grey",
    fg="yellow"
)

button.pack()









# mainloop es un métodos que llama eventos y bloquea cualquier
# evento que venta después
ventana.mainloop()
