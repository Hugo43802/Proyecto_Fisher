""" 
En este ejercicio se verifica el cambio del estado del sensor reed

"""
import ftrobopy


# función para conectar el plc
# plc = ftrobopy.ftrobopy("192.168.1.208")

plc = ftrobopy.ftrobopy("192.168.0.101")

def run():
    #se crea el objeto sensor reed y se verifica el estado
    reed = plc.input(5)
    estado = reed.state()
    print("El estado actual del botón es: ", estado)

    #Se crea le objeto luz por la salida 1 
    luz = plc.output(1)

    while True: 
        nuevo_estado = reed.state()
        luz.setLevel(0)
        if nuevo_estado != 0:
            luz.setLevel(512)
            print("estado, getCurrentInput(): ", nuevo_estado, plc.getCurrentInput(1))
            estado = nuevo_estado
        plc.updateWait()

#if que verifica el inicio
if __name__ == "__main__":
    # conexion()
    run()
    