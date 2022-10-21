from tkinter import *
import Despacho as d

class Automatico:
    def __init__(self):
        self.ventana_auto = Tk()
        self.ventana_auto.geometry("400x640")
        self.ventana_auto.resizable(0,0)
        self.ventana_auto.title("Automático")
        self.ventana_auto.eval('tk::PlaceWindow . center')

        # configurar el grid
        self.ventana_auto.columnconfigure(0, weight=1)
        self.ventana_auto.columnconfigure(1, weight=1)
        self.ventana_auto.columnconfigure(2, weight=1)
        self.ventana_auto.columnconfigure(3, weight=1)
        self.ventana_auto.columnconfigure(4, weight=1)

        self.msj_opciones = Label(
            text="Combinación de Productos",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=0, column=0, columnspan=5)
    
    # ALEATORIO    
        fichas = StringVar()
        self.msj_Fichas = Label(
            width=30,
            height=5,
            textvariable=fichas,
            relief="groove",
            borderwidth=4,
            bg="white"
        )
        self.msj_Fichas.grid(row=1, column=0, columnspan=5)
        # tx.set("Hola Mundo")


        self.msj_Sumalbl = Label(
            text="Sumatoria de Tiempos:",
            width=20
        ).grid(row=2, column=1, pady=10)

        sum_Fichas = StringVar()
        self.msj_Sumatxt = Label(
            width=8,
            height=1,
            relief="groove",
            borderwidth=4,
            textvariable=sum_Fichas,
            bg="white"
        ).grid(row=2, column=2)
        
       

# PROCESO

        self.msj_Proceso = Label(
            text="Proceso de Despacho",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=3, column=0, pady=5, columnspan=5)

        self.msj_Despacho_ini = Label(
            width=30,
            height=5,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=4, column=0, columnspan=5)

        self.msj_Banda = Label(
            width=30,
            height=1,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=5, column=0, columnspan=5, pady=10)

# VINIPELADO

        self.msj_Vinipelado = Label(
            text="Tiempo de Vinipelado:",
            width=20
        ).grid(row=6, column=1, pady=5)

        self.msj_VinipeladoTxt = Label(
            width=8,
            height=1,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=6, column=2)

# EJE LINEAL
        self.msj_Eje = Label(
            text="Eje Lineal",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=7, column=0, columnspan= 5, pady=10)

        self.ms_Eje_Estado = Label(
            width=30,
            height=1,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=8, column=0, columnspan=5)

        self.msj_Eje_Espera = Label(
            text="Tiempo de Espera:",
            width=20
        ).grid(row=9, column=1, pady=5)

        self.msj_EjeTxt = Label(
            width=8,
            height=1,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=9, column=2)

# ENTREGA
        self.msj_Entrega = Label(
            text="Entrega",
            font= ('Helvetica', 10, 'bold')
        ).grid(row=10, column=0, columnspan= 5, pady=10)

        self.msj_Entrega_Banda = Label(
            width=30,
            height=1,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=11, column=0, columnspan= 5, pady=5)

        self.msj_NextTarea = Label(
            width=30,
            height=5,
            relief="groove",
            borderwidth=4,
            bg="white"
        ).grid(row=12, column=0, columnspan=5)
        
        #Botón de inicio
        def btn_Inicio():
            d.aleatorio(fichas, sum_Fichas)
            
            d.rampas(fichas, sum_Fichas)   
            
        self.Inicio = Button(
            text= "Inicio",
            width=10,
            height=1,
            relief="solid",
            command= btn_Inicio
        ).grid(row=13, column=0, columnspan=5, pady=5)
        
        

        self.ventana_auto.mainloop()
        # No permite que se hagan acciones en otras ventanas 
                
if __name__ == "__main__":
        app = Automatico()


