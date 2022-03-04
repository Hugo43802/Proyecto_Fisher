from time import sleep
import ftrobopy


plc = ftrobopy.ftrobopy("192.168.0.101")

def motor_MA4():
    MA4 = plc.output(5)
    MA4.setLevel(512)
    sleep(2)
    MA4.setLevel(0)
    
def banda1(num_rampa):
    # se crea el objeto sensor reed en input
    b1 = plc.input(2)
    b2 = plc.input(3)
    b3 = plc.input(4)
    
    #Botón de la banda lineal BG1
    
    BG1=plc.input(1)
    
    ''' creación de objeto salida
        En este caso los motores se manejan como salidas 
        en ese caso las salidas van de 0 a 512
    '''
    # Objeto motor en output
    ## BANDA LINEAL 
    MA1 = plc.output(1)
    MA1_2 = plc.output(2) # El 2 es la dirección opuesta
    
    ## DESPACHO
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
        ns_BG1=BG1.state()
        
        if cambio == 1 and ns_b1 != 0:
            MA5.setLevel(512)
            MA3.setLevel(500)
        
        if ns_b2 != 0 and ns_BG1==1:
            cambio = 0
            MA3.setLevel(0)
            MA5.setLevel(0)
            
            motor_MA4()         
            '''
                Espera  segundo para encender nuevamente los motores
                MA3 y MA2
            '''
            sleep(1)
            
            MA3.setLevel(500)
            MA2.setLevel(512)
       
        if ns_b2 != 0 and ns_BG1==0:
            MA3.setLevel(0)
            MA5.setLevel(0)
            MA1.setLevel(512)
            cambio =1
            
            
            if cambio ==1:
                MA1.setLevel(0)
            
            if ns_b3 != 0:
                MA3.setLevel(0)
                MA2.setLevel(0)
                
                if num_rampa == 1:
                    if ns_BG1 != 0:
                        MA1_2.setLevel(512)
                        sleep(2)
                        MA1_2.setLevel(0)
                        MA2.setLevel(512)
                        sleep(3)
                        MA2.setLevel(0)
                        MA1.setLevel(512)
                        sleep(3)
                        MA1.setLevel(0)
                    else:
                        MA1.setLevel(512)
                        
                        if ns_BG1 ==1:
                            MA1.setLevel(0)
            
        cambio_while = False
        break
    
def run():
    B4 = plc.input(5)
    B5 = plc.input(6)
    B6 = plc.input(7)
    B7 = plc.input(8)
    
    MA2 = plc.output(6)
    
    while True:
        #Variable para enviar a la banda linea a donde debe moverse
        rampa = 0
        
        estado_B4 = B4.state()
        estado_B5 = B5.state()
        estado_B6 = B6.state()
        estado_B7 = B7.state()
        
        if estado_B4 != 1 and rampa == 0:
            rampa = 1
            print("El producto va a la rampa # 1")
            banda1(rampa)
        elif estado_B5 != 1:
            rampa = 2
            print("El producto va a la rampa # 2")
            banda1(rampa)
        elif estado_B6 != 1:
            rampa = 3
            print("El producto va a la rampa # 3")
            banda1(rampa)
        elif estado_B7 != 1:
            rampa = 42
            print("El producto va a la rampa # 4")
            banda1(rampa)
        else:
            print("Todas las rampas llenas")
        
        plc.updateWait()


if __name__ == "__main__":
    run()