""" 
En este ejercicio se prueba la funcionalidad del sensor de color

"""
from typing import Tuple
import ftrobopy


# función para conectar el plc
plc = ftrobopy.ftrobopy("192.168.1.208")


def run():
    scolor = plc.colorsensor(3)
    print("El color es: ", scolor.value())
    print("El color es: ", scolor.color())

    while True:
        plc.updateWait()
        colval = scolor.value()
        colname = scolor.color()
        # https://www.programiz.com/python-programming/methods/string/format
        s = "Color: {:5d} {:>6s} ".format(colval, colname)
        print(s, end='\r')

#if que verifica el inicio
if __name__ == "__main__":
    run()
    