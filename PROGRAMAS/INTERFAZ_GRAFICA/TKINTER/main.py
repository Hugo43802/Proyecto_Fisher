from tkinter import *
import automatico

class App:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.geometry("260x150")
        self.ventana.resizable(0,0)
        self.ventana.title("Ventana de Inicio")

        # configurar el grid
        self.ventana.columnconfigure(0, weight=1)
        self.ventana.columnconfigure(1, weight=1)
        
        # Label del mensaje de inicio
        self.msj_inicio = Label(
            self.ventana,
            text="Opciones de Selección"
        )
        self.msj_inicio.grid(row=0, column=0, columnspan=2, pady=10)

        # Variable de selección por default
        self.seleccion = IntVar(None,0)

        self.rbtn_Automatico = Radiobutton(
            text="Automático",
            value=0,
            variable= self.seleccion
        )
        self.rbtn_Automatico.grid(row=1, column=0, columnspan= 2, pady= 3)

        self.rbtn_Manual = Radiobutton(
            text="Manual",
            value=1,
            variable= self.seleccion,
            #indicator=0
        )
        self.rbtn_Manual.grid(row=2, column=0, columnspan= 2)

        self.btn_Inicio = Button(
            text="Inicio",
            width=10,
            command= self.imprimir
        )
        self.btn_Inicio.grid(row=3, column=0, columnspan= 3, pady=10)

        self.ventana.mainloop()

    def imprimir(self):
        if self.seleccion.get() == 0:
            ventana_automatico = automatico.Automatico(Toplevel(self.ventana))
        if self.seleccion.get() == 1:
            print("self.Ventana 2")

if __name__ == "__main__":
        app = App()

