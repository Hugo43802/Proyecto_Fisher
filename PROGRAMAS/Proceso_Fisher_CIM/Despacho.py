'''
    Este programa genera una lectura del sensor reed
     para activar el motor (MA5)
'''
from time import sleep
import ftrobopy

# función para conectar el plc

plc = ftrobopy.ftrobopy("192.168.0.101")
cambio = 1

def banda1():
    # se crea el objeto sensor reed
    b1 = plc.input(2)
    b1_estado = b1.state()
    
    b2 = plc.input(3)
    b2_estado = b2.state()
    
    
    # creación de objeto motor
    MA5 = plc.motor(2)
    MA3 = plc.motor(1)
  
    print("El estado del sensor B1 es: ", b1_estado)
    print("El estado del sensor B2 es: ", b2_estado)
    
    while True:
        cambio = 1
        print("El estado de B1 es = ", b1_estado)
        print("El estado de B2 es = ", b2_estado)
        ns_b1 = b1.state()
        ns_b2 = b2.state()
        
        if cambio == 1 and ns_b1 != 0:
            #plc.updateWait(0.5)
            MA5.setSpeed(512)
            MA3.setSpeed(512)
            print(" B1 Estado nuevo: ", ns_b1)
            b1_estado = ns_b1
        
        if ns_b2 != 0:
            cambio = 0
            MA3.setSpeed(0)
            MA5.setSpeed(0)
            print(" B2 Estado nuevo: ", ns_b2)
            b2_estado = ns_b2
         
            plc.updateWait()
              
if __name__ == "__main__":
    banda1()