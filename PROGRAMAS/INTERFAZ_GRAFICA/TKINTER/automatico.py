from tkinter import *

class Automatico:
    def __init__(self, ventana_auto):
        # self.ventana_auto = Tk()
        ventana_auto.geometry("400x600")
        ventana_auto.resizable(0,0)
        ventana_auto.title("Automático")

        # configurar el grid
        ventana_auto.columnconfigure(0, weight=1)
        ventana_auto.columnconfigure(1, weight=1)

        self.msj_opciones = Label(
            ventana_auto,
            text="Combinación de Productos",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=0, column=0, columnspan= 2)
        
        self.msj_Fichas = Text(
            ventana_auto,
            width=30,
            height=5,
            state="disabled"
        ).grid(row=1, column=0, columnspan=2)

        self.msj_Sumalbl = Label(
            ventana_auto,
            text="Sumatoria de Tiempos:",
            width=20
        ).grid(row=2, column=0, pady=10)

        self.msj_Sumatxt = Text(
            ventana_auto,
            width=8,
            height=1,
            state="disabled"
        ).grid(row=2, column=0, sticky=E)

# PROCESO

        self.msj_Proceso = Label(
            ventana_auto,
            text="Proceso de Despacho",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=3, column=0, columnspan= 2, pady=5)

        self.msj_Despacho_ini = Text(
            ventana_auto,
            width=30,
            height=5,
            state="disabled"
        ).grid(row=4, column=0, columnspan=2)

        self.msj_Banda = Text(
            ventana_auto,
            width=30,
            height=1,
            state="disabled"
        ).grid(row=5, column=0, columnspan=2, pady=10)

# VINIPELADO

        self.msj_Vinipelado = Label(
            ventana_auto,
            text="Tiempo de Vinipelado:",
            width=20
        ).grid(row=6, column=0, pady=5, sticky=W, ipadx=115)

        self.msj_VinipeladoTxt = Text(
            ventana_auto,
            width=8,
            height=1,
            state="disabled"
        ).grid(row=6, column=0, sticky=E)

# EJE LINEAL
        self.msj_Eje = Label(
            ventana_auto,
            text="Eje Lineal",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=7, column=0, columnspan= 2, pady=10)

        self.ms_Eje_Estado = Text(
            ventana_auto,
            width=30,
            height=1
        ).grid(row=8, column=0, columnspan=2)

        self.msj_Eje_Espera = Label(
            ventana_auto,
            text="Tiempo de Espera:",
            width=20
        ).grid(row=9, column=0, pady=5, sticky=W, ipadx=105)

        self.msj_EjeTxt = Text(
            ventana_auto,
            width=8,
            height=1,
            state="disabled"
        ).grid(row=9, column=0, sticky=E)

# ENTREGA
        self.msj_Entrega = Label(
            ventana_auto,
            text="Entrega",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=10, column=0, columnspan= 2, pady=10)

        self.msj_Entrega_Banda = Text(
            ventana_auto,
            width=30,
            height=1,
            state="disabled"
        ).grid(row=11, column=0, columnspan= 2, pady=5)

        self.msj_NextTarea = Text(
            ventana_auto,
            width=30,
            height=5,
            state="disabled"
        ).grid(row=12, column=0, columnspan=2)

        # No permite que se hagan acciones en otras ventanas 
        ventana_auto.grab_set()
