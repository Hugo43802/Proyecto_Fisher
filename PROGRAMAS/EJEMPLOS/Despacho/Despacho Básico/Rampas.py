from time import sleep
import ftrobopy


plc = ftrobopy.ftrobopy("192.168.0.101")

def motor_MA4():
    MA4 = plc.output(5)
    MA4.setLevel(512)
    sleep(2)
    MA4.setLevel(0)
    
def banda1():
    # Permiso me sirve para verificar que la función motor_MA4 solo se ejecute una vez
    permiso = 1
    # se crea el objeto sensor reed
    b1 = plc.input(2)
    b2 = plc.input(3)
    b3 = plc.input(4)
    
    ''' creación de objeto salida
        En este caso los motores se manejan como salidas 
        en ese caso las salidas van de 0 a 512
    '''
    MA5 = plc.output(3)
    MA3 = plc.output(4)
    MA4 = plc.output(5)
    MA2 = plc.output(6)
      
    '''
    El cambio de While funciona para que el while salga al ser falso y se ejecute una sola vez
    '''
    cambio_while = True
    
    while cambio_while:
        cambio = 1
        ns_b1 = b1.state()
        ns_b2 = b2.state()
        ns_b3 = b3.state()
        
        if cambio == 1 and ns_b1 != 0:
            MA5.setLevel(512)
            MA3.setLevel(500)
        
        if ns_b2 != 0 and permiso == 1:
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
            
            MA3.setLevel(500)
            MA2.setLevel(512)
                       
        if ns_b3 != 0:
            MA3.setLevel(0)
            MA2.setLevel(0)
            
        cambio_while = False
        break
    
def run():
    B4 = plc.input(5)
    B5 = plc.input(6)
    B6 = plc.input(7)
    B7 = plc.input(8)
    
    MA2 = plc.output(6)
    
    while True:
        #Variable para verificar el cambio
        rampa = 0
        
        estado_B4 = B4.state()
        estado_B5 = B5.state()
        estado_B6 = B6.state()
        estado_B7 = B7.state()
        
        if estado_B4 != 1 and rampa == 0:
            rampa = 1
            print("El producto va a la rampa # 1")
            banda1()
        elif estado_B5 != 1:
            rampa = 1
            print("El producto va a la rampa # 2")
            banda1()
        elif estado_B6 != 1:
            print("El producto va a la rampa # 3")
            banda1()
        elif estado_B7 != 1:
            print("El producto va a la rampa # 4")
            banda1()
        else:
            print("Todas las rampas llenas")
        
        plc.updateWait()


if __name__ == "__main__":
    run()