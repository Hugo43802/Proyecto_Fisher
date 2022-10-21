import random
from automatico import *
from tkinter import *

# Crear el diccionario con los colores
colores = {
    "Azul": 4,
    "Rojo": 7,
    "Blanco": 10,
}

# Se crean los arreglos vacíos
salida_Tiempos = []
salida_Claves = []

def aleatorio(msj_Fichas):
    '''
        Esta función elige entre diferentes combinaciones de colores
        para dar las familias de producto que serán procesadas 
        por el despacho
    '''
    for elem in range(4):
        ## Elección de valores al azar
        alea = random.choice(list(colores.values()))

        ## pos = Guarda los elementos mutables en lista (valores)
        pos = list(colores.values())
        ## llaves = Guarda las claves mutables en lista (claves)
        llaves = list(colores.keys())

        ## llave obtiene los valores y reconoce las claves
        llave = pos.index(alea)

        # Agregar a la lista salida tiempos, los valores
        salida_Tiempos.append(alea)
        # Agregar para visualizar los colores seleccionados.
        salida_Claves.append(llaves[llave])

        #Sunar los valores del arreglo tiempos
        suma = sum(salida_Tiempos)

        msj_Fichas.delete(0, END)
        msj_Fichas.insert(END, "Hola Mundo")

    print(salida_Tiempos)
    print(salida_Claves)
    print("La suma de los tiempos es: ", suma)

# aleatorio()