""" 
En este ejercicio se verifica el cambio del estado del botón

"""
import ftrobopy


# función para conectar el plc
plc = ftrobopy.ftrobopy("192.168.1.208")
   
# función para verificar el estado del botón
def run():
    # Se crea el objeto entrada(I1) y se verifica el estado(1 o 0)
    I1 = plc.input(1)
    estado = I1.state()
    print("El estado actual del botón es: ", estado)

    while True: 
        nuevo_estado = I1.state()
        if nuevo_estado != estado:
            print("estado, getCurrentInput(): ", nuevo_estado, plc.getCurrentInput(0))
            estado = nuevo_estado
        plc.updateWait()

#if que verifica el inicio
if __name__ == "__main__":
    # conexion()
    run()
    

