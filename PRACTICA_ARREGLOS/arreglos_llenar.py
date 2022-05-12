import random


arreglo = ["Rojo", "Azul", "Blanco"]

n_Arreglo = []

n_Arreglo.append(arreglo[1])

for i in arreglo:
    selec = random.choice(arreglo)
    print(selec)
print(n_Arreglo)
