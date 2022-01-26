'''
    Controlar la luz a partir del pulsador
'''

import ftrobopy

# Conectar el plc por medio de WLAN
plc = ftrobopy.ftrobopy("192.168.0.101")

def run():
    # crear objeto entrada(I1) en la entrada 1
    I1 = plc.input(1)
    estado_entrada = I1.state()
    print(f"El estado actual del botón es {estado_entrada}.")

    # se crea el objeto luz de salida
    luz = plc.output(1)

    # Se identifica el nuevo estado del botón que por defecto es (0, sin pulsar), la luz se deja con intensidad (0, Apagada).
    # Seguido, se realiza la comparación si el nuevo estado es diferente de 0, lo cual enciende la luz. Después el nuevo estado
    # se iguala al anterior ns = 0, finalmente se espera una actualización con updateWait() 
    while True:
        ns = I1.state()
        luz.setLevel(0)
        if ns != 0:
            luz.setLevel(512)
            estado_entrada = ns
            print("Nuevo Estado: ", ns)
        plc.updateWait()

if __name__ == "__main__":
    # conexion()
    run()
