from tkinter import *
import tkinter.ttk as ttk

def imprimir():
    if seleccion.get() == 0:
        openNewWindow()
    if seleccion.get() == 1:
        print("Ventana 2")

def openNewWindow():

        # Toplevel object which will
        # be treated as a new window
        

        # sets the title of the
        # Toplevel widget
        newWindow.title("New Window")

        # sets the geometry of toplevel
        newWindow.geometry("200x200")

        # A Label widget to show in toplevel
        Label(newWindow,
            text ="This is a new window").pack()


# ventana principal
ventana = Tk()
ventana.geometry("260x150")
ventana.resizable(0,0)
ventana.title("Ventana de Inicio")

# configurar el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

# Label del mensaje de inicio
msj_inicio = Label(
    ventana,
    text="Opciones de Selección"
)
msj_inicio.grid(row=0, column=0, columnspan=2, pady=10)

# Variable de selección por default
seleccion = IntVar(None,0)

rbtn_Automatico = Radiobutton(
    text="Automático",
    value=0,
    variable=seleccion
).grid(row=1, column=0, columnspan= 2, pady= 3)

rbtn_Manual = Radiobutton(
    text="Manual",
    value=1,
    variable=seleccion,
    #indicator=0
).grid(row=2, column=0, columnspan= 2)

btn_Inicio = Button(
    text="Inicio",
    width=10,
    command=imprimir
).grid(row=3, column=0, columnspan= 3, pady=10)

print(seleccion)
ventana.mainloop()
