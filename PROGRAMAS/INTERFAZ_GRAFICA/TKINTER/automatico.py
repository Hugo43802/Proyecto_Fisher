from cProfile import label
from cgitb import text
from distutils.command.config import config
from sre_parse import State
from textwrap import fill
from tkinter import *

class Automatico:
    def __init__(self, ventana_auto):
        # self.ventana_auto = Tk()
        ventana_auto.geometry("500x400")
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
            text="Sumatoria de Tiempos:"
        ).grid(row=2, column=0, padx= 10)

        self.msj_Sumatxt = Text(
            ventana_auto,
            width=8,
            height=1,
            state="disabled"
        ).grid(row=2, column=0, pady=5, padx=4)

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
        ).grid(row=5, column=0, pady=5)

        self.msj_Eje = Label(
            ventana_auto,
            text="Eje Lineal",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=6, column=0, columnspan= 2, pady=5)

        # VINIPELADO

        self.msj_Vinipeladolbl = Label(
            ventana_auto,
            text="Tiempo de Vinipelado:"
        ).grid(row=6, column=0)

        self.msj_Banda = Text(
            ventana_auto,
            width=8,
            height=1,
            state="disabled"
        ).grid(row=6, column=1, pady=5)
        # No permite que se hagan acciones en otras ventanas 
        ventana_auto.grab_set()




        

