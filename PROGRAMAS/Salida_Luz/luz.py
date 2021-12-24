'''
En este ejercicio se verifica la salida de luz por parte de una 
bombilla
'''

import ftrobopy

plc = ftrobopy.ftrobopy("192.168.1.208")

def run():
    luz = plc.output(1)
    luz.setLevel(100)
    plc.updateWait(2)
    luz.setLevel(512)
    plc.updateWait(2)
    plc.stopAll()
    plc.updateWait()
    print("¡El proceso terminado!")

#if que verifica el inicio
if __name__ == "__main__":
    # conexion()
    run()