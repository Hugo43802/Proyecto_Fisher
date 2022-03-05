#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from TouchStyle import *
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.0.101")

class FtcGuiApplication(TouchApplication):
    def __init__(self, args):
        TouchApplication.__init__(self, args)
        
            
        # crear objeto entrada(I1) en la entrada 1
        I1 = plc.input(1)
        estado_entrada = I1.state()
        print(f"El estado actual del botón es {estado_entrada}.")
        

        # se crea el objeto luz de salida
        luz = plc.output(1)
        luz.setLevel(0)
        n=0

        # Se identifica el nuevo estado del botón que por defecto es (0, sin pulsar), la luz se deja con intensidad (0, Apagada).
        # Seguido, se realiza la comparación si el nuevo estado es diferente de 0, lo cual enciende la luz. Después el nuevo estado
        # se iguala al anterior ns = 0, finalmente se espera una actualización con updateWait() 
        while True:
            ns = I1.state()
            if ns != 0:
                luz.setLevel(n)
                n=n+10
                if n>=512:
                    n=0
                print(n)
            plc.updateWait()    
    
def run():
    # Creates an empty MainWindow
    app = FtcGuiApplication(sys.argv)
    w = TouchWindow("Test")
    w.show()
    app.exec_() 

if __name__ == "__main__":
    run()
    
