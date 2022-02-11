'''
    Este programa genera el movimiento del proceso de 
    Despacho
'''
from multiprocessing.connection import wait
from time import sleep
import ftrobopy

# función para conectar el plc

plc = ftrobopy.ftrobopy("192.168.0.101")

def motor_MA4():
    MA4 = plc.output(5)
    MA4.setLevel(512)
    sleep(2)
    MA4.setLevel(0)
            
def banda1():
    # se crea el objeto sensor reed
    b1 = plc.input(2)
    b1_estado = b1.state()
    
    b2 = plc.input(3)
    b2_estado = b2.state()
    
    b3 = plc.input(4)
    b3_estado = b3.state()
    
    ''' creación de objeto salida
        En este caso los motores se manejan como salidas 
        en ese caso las salidas van de 0 a 512
    '''
    MA5 = plc.output(3)
    MA3 = plc.output(4)
    MA4 = plc.output(5)
    MA2 = plc.output(6)
  
    #print("El estado del sensor B1 es: ", b1_estado)
    #print("El estado del sensor B2 es: ", b2_estado)
    
    while True:
        cambio = 1
        #print("El estado de B1 es = ", b1_estado)
        #print("El estado de B2 es = ", b2_estado)
        ns_b1 = b1.state()
        ns_b2 = b2.state()
        ns_b3 = b3.state()
        
        if cambio == 1 and ns_b1 != 0:
            MA5.setLevel(512)
            MA3.setLevel(512)
            #print(" B1 Estado nuevo: ", ns_b1)
        
        if ns_b2 != 0:
            cambio = 0
            MA3.setLevel(0)
            MA5.setLevel(0)
            #print(" B2 Estado nuevo: ", ns_b2)
            motor_MA4()         
            
            '''
                Espera  segundo para encender nuevamente los motores
                MA3 y MA2
            '''
            sleep(1)
            
            MA3.setLevel(512)
            MA2.setLevel(512)
            
                       
        if ns_b3 != 0:
            MA3.setLevel(0)
            MA2.setLevel(0)
                             
         
        plc.updateWait()
              
if __name__ == "__main__":
    banda1()