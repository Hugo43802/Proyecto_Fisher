'''
En este ejercicio se verifica la salida de luz por parte de una 
bombilla con un ciclo
'''

import ftrobopy

plc = ftrobopy.ftrobopy("192.168.1.208")

def run():
    luz = plc.output(1)

# El ciclo for que repite el ciclo de 1 a 4. en donde enciende y apaga
    for i in range(1, 4):
        luz.setLevel(512)
        plc.updateWait(2)
        luz.setLevel(0)
        plc.updateWait(2)
        plc.stopAll()
        plc.updateWait()
    print("¡El proceso terminado!")

#if que verifica el inicio
if __name__ == "__main__":
    # conexion()
    run()