from time import sleep
import ftrobopy

#plc = ftrobopy.ftrobopy("192.168.1.208") # ip de mi hogar
plc = ftrobopy.ftrobopy("192.168.0.101") # ip de la U

# Inicialización de variables y objetos


## SENSORES REED
B1 = plc.input(2)
B2 = plc.input(3)
B3 = plc.input(4)

B4 = plc.input(5) #cambiar a 5, 6, 7 y 8 para probar en original
B5 = plc.input(6)
B6 = plc.input(7)
B7 = plc.input(8)

### MOTORES
#Reset y banda lineal
MA1 = plc.output(1)
MA1_Reverso = plc.output(2)
#Despacho
MA5 = plc.output(3)
MA3 = plc.output(4) #Cambiar a 4 y 6 para probar original1
MA2 = plc.output(6)

#### BOTÓN 
BG1 = plc.input(1)

## Función Reset para verificar que el motor MA1 siempre esté en la posición de 
# origen
def reset():
    '''
        Función que permite enviar el eje lineal de nuevo a su posición original
    '''
    
    # Para probar en el sistema original, debe cambiarse a != 0
    while BG1.state() != 0:
        MA1.setLevel(0)
        print("Eje en el origen")
        break
    else:
        MA1.setLevel(512)

def vinipelado():
    '''
        Función que activa el motor MA4 del prodceso de despacho
    '''
    MA4 = plc.output(5) # Para probar en el sistema orginal cambiar a 5
    MA4.setLevel(512)
    sleep(2)
    MA4.setLevel(0)

def eje_lineal(pulsos):
    '''
        pulsos = Cantidad de pasos que debe ejercer el motor para llegar a la meta

        Esta función genera el movimiento del eje lineal para transportar según la 
        cantidad de pulsos el producto que se encuentra en la banda.

    '''

    #get.CurrentCounterValue lee el contador existente en la conexión.
    #pos_inicial_eje = posición inicial del motor frente a la rampa 1

    #meta = Variable a la que se quiere llegar (objetivo), es la posición de la banda para llegar a las rampas
    #(Revisar archivo Rampas.txt)

    # C1 = Variable que guarda los datos del contador desde el PLC

    # Los estados B4, B5, B6 y B7, verifican si el producto pasa por el sensor

    estado_B4 = B4.state()
    estado_B5 = B5.state()
    estado_B6 = B6.state()
    estado_B7 = B7.state()

    reset()
    sleep(4)

    pos_inicial_eje = plc.getCurrentCounterValue(0)
    print("El valor de C2 es: ", pos_inicial_eje)

    meta = pos_inicial_eje + pulsos

    cambio_while = True
    
    while cambio_while:
        MA1.setLevel(0)

        if pulsos == 0:
            MA1_Reverso.setLevel(0)
            MA2.setLevel(512)

            if estado_B4 != 0:
                print("Detectado B4")
                MA2.setLevel(0)

        else:
            C1 = plc.getCurrentCounterValue(0) 
            print(C1)
            
            print("La meta es: ", meta)
            print(pulsos)
            
            MA1_Reverso.setLevel(512)
            if plc.getCurrentCounterValue(0) >= meta:
                MA1_Reverso.setLevel(0)
                print("Eje en posición")
                sleep(2)
                
                MA2.setLevel(512)
                sleep(2)
                
                if estado_B5 == 1:
                    MA2.setLevel(0)
                    print("Rampa 2 lista")
                
                if estado_B6 == 1:
                    MA2.setLevel(0)

                if estado_B7 == 1:
                    MA2.setLevel(0)
            
                cambio_while =False
    reset()
    plc.updateWait()

def despacho(num_Rampa, pulsos):
    '''
        num_Rampa: Número de la rampa a la que el producto se dirigirá

        pulsos: Es la cantidad de pasos que debe dar el motor para llegar a cada rampa
    '''
    reset()
    
    cambio_while = True

    while cambio_while:
        cambio = 1

        # Se reconoce en qué estado se encuentran los sensores 1 = activado o 0 = desactivado
        estado_b1 = B1.state()
        estado_b2 = B2.state()
        estado_b3 = B3.state()

        if cambio == 1 and estado_b1 != 0:
            MA5.setLevel(512)
            MA3.setLevel(500)
        
        if estado_b2 != 0:
            cambio = 0
            MA3.setLevel(0)
            MA5.setLevel(0)

            vinipelado()
            sleep(0.5)

            MA3.setLevel(500)
            MA2.setLevel(512)
        
        if estado_b3 != 0:
            MA3.setLevel(0)
            MA2.setLevel(0)
            
            #Entrar al movimiento de la banda lineal
            if num_Rampa == 1:
                eje_lineal(pulsos)
            elif num_Rampa == 2:
                eje_lineal(pulsos)
            elif num_Rampa == 3:
                eje_lineal(pulsos)
            elif num_Rampa == 4:
                eje_lineal(pulsos)


    cambio_while = False
    plc.updateWait()

def rampas():
    cambio_while = True
    while cambio_while:

        rampa = 0

        estado_B4 = B4.state()
        estado_B5 = B5.state()
        estado_B6 = B6.state()
        estado_B7 = B7.state()

        if estado_B4 != 1:
            rampa = 1
            print("¡El producto se dirige a la rampa #1!")
            despacho(rampa, 0)
        elif estado_B5 != 1:
            rampa = 2
            print("¡El producto se dirige a la rampa #2!")
            despacho(rampa, 209)
        elif estado_B6 != 1:
            rampa = 3
            print("¡El producto se dirige a la rampa #3!")
            despacho(rampa, 442)
        elif estado_B7 != 1:
            rampa = 4
            print("¡El producto se dirige a la rampa #4!")
            despacho(rampa, 653)
        else:
            print("¡Todas las rampas están llenas!")

        plc.updateWait()   

if __name__ == "__main__":
    rampas()