'''
    Este programa genera una lectura del sensor reed
     para activar el motor (MA5)
'''
from time import sleep
import ftrobopy

# función para conectar el plc

plc = ftrobopy.ftrobopy("192.168.0.101")

def run():
    # se crea el objeto sensor reed
    reed = plc.input(2)
    estado = reed.state()
    
    # creación de objeto motor
    motor = plc.motor(2)
  
    
    print("El estado actual del sensor es: ", estado)
    
    while True:
        nuevo_estado = reed.state()
        
        if nuevo_estado != 0:
            sleep(2)
            motor.setSpeed(150)
            
            print("Estado nuevo: ", nuevo_estado)
            estado = nuevo_estado
            
        plc.updateWait()
        
              

if __name__ == "__main__":
    run()