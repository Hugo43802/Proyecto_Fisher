import ftrobopy
from time import sleep

'''
Controlar el motor de color negro (motor XS).
Motor básico
'''

plc = ftrobopy.ftrobopy("192.168.1.208")


def run():
    # El motor se encuentra conectado a la salida 1, se instancia a tener una velocidad de 32 y se apaga después de 2 seg. 
    # Finalmente el motor se detiene
    motor = plc.motor(1)
    motor.setSpeed(15) # si se coloca en negativo, gira hacia el lado contrario
    sleep(2)
    motor.stop()

if __name__ == "__main__":
    run()