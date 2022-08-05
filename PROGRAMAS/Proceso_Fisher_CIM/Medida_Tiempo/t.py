import time 
import ftrobopy
import random

'''
    VARIABLES
'''  
# Crear diccionario de colores

colores = {
    "Azul": 4,
    "Rojo": 7,
    "Blanco": 10,
}

# Se crean los arreglos vacíos para guardar tiempos y claves
salida_Tiempos = []
salida_Claves = []

'''
    INICIO DE PLC
'''
plc = ftrobopy.ftrobopy("192.168.0.115") # ip de la U


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

def aleatorio():
    '''
        Esta función elige entre diferentes combinaciones de colores
        para dar las familias de producto que serán procesadas 
        por la función vinipelado y eje_lineal.
        
        Esta función retorna la sumatoria de tiempos de los colores
        y lo divide a la mitad.
    '''
    for elem in range(4):
        ## Elección de valores al azar
        alea = random.choice(list(colores.values()))

        ## pos = Guarda los elementos mutables en lista (valores)
        pos = list(colores.values())
        ## llaves = Guarda las claves mutables en lista (claves)
        llaves = list(colores.keys())

        ## llave obtiene los valores y reconoce las claves
        llave = pos.index(alea)

        # Agregar a la lista salida tiempos, los valores
        salida_Tiempos.append(alea)
        # Agregar para visualizar los colores seleccionados.
        salida_Claves.append(llaves[llave])

        #Sunar los valores del arreglo tiempos
        suma = sum(salida_Tiempos)

        return suma
    
    print(salida_Tiempos)
    print(salida_Claves)
    print("La suma de los tiempos es: ", suma)

## Función Reset para verificar que el motor MA1 siempre esté en la posición de 
# origen
def reset():
    start_time = time.time()
    '''
        Función que permite enviar el eje lineal de nuevo a su posición original
    '''
    while BG1.state() != 0:
        MA1.setLevel(0)
        print("Eje en el origen")
        break
    else:
        MA1.setLevel(512)

    tf= time.time()
    #print("Tiempo de eje", tf-start_time) 
   
    
    
def vinipelado():
    start_time = time.time()
    '''
        Función que activa el motor MA4 del prodceso de despacho,
        adicional se obtiene el tiempo de la combinación de colores
        obtenida de la función aleatorio.
    '''
    
    tiempo = aleatorio()/3
    MA4 = plc.output(5) # Para probar en el sistema orginal cambiar a 5
    time.sleep(tiempo)
    MA4.setLevel(512)
    time.sleep(tiempo)
    #print("El tiempo de vinipelado es: ",tiempo)
    MA4.setLevel(0)
    
    tf= time.time()
    print("Tiempo de vinipelado", tf-start_time) 

def eje_lineal(num_Rampa,sensor, pulsos, tiempo):
    start_time = time.time()
    '''
        num_Rampa = Número de la rampa hacia la que se dirigirá el motor MA1_Reverso

        sensor = Objeto sensor que se va a actualizar. Se recibe de la función despacho.
        
        pulsos = Cantidad de pasos que debe ejercer el motor para llegar a la meta
        Esta función genera el movimiento del eje lineal para transportar según la 
        cantidad de pulsos el producto que se encuentra en la banda.
        
        tiempo = Suma de los tiempos obtenidos de la función aleatorio().

        La función eje_lineal genera el movimiento del motor MA1 y MA1_Reverso, para ubicar
        la banda en las diferentes rampas según los pulsos y se detiene al identificar el 
        sensor elegido para cada rampa.
        
    '''

    #get.CurrentCounterValue lee el contador existente en la conexión.
    #pos_inicial_eje = posición inicial del motor frente a la rampa 1

    #meta = Variable a la que se quiere llegar (objetivo), es la posición de la banda para llegar a las rampas
    #(Revisar archivo Rampas.txt)

    # C1 = Variable que guarda los datos del contador desde el PLC

    # Los estados B4, B5, B6 y B7, verifican si el producto pasa por el sensor
    time.sleep(tiempo)
    
    pos_inicial_eje = plc.getCurrentCounterValue(0)
    #print("El valor de C2 es: ", pos_inicial_eje)

    meta = pos_inicial_eje + pulsos

    cambio_while = True

    while cambio_while:
        MA1.setLevel(0)
        
        C1 = plc.getCurrentCounterValue(0) 
        #print(C1)
        
        #print("La meta es: ", meta)
        #print("Los pulsos contados son: ",pulsos)
        
        MA1_Reverso.setLevel(512)
        
        while (plc.getCurrentCounterValue(0) >= meta) and (cambio_while == True): #Para no usar break, simplemente se mantiene el cambio a True
            estado = sensor.state() # el estado será el cambio del objeto dependiendo de la rampa
            MA1_Reverso.setLevel(0)
            #print("Los pulsos contados son: ",pulsos)
            #print("Eje en posición")
            # sleep(2)
            
            MA2.setLevel(512)
            # sleep(2)
            #print("La rampa es: ", num_Rampa)
            
            if estado == 1: 
                MA2.setLevel(0)
                print(f"Rampa #{num_Rampa} lista")
                cambio_while =False
                
    time.sleep(tiempo)
    reset()
    time.sleep(4)
    
    tf= time.time()
    print("Tiempo de eje_lineal", tf-start_time)
    
    rampas()
        
    plc.updateWait()

def despacho(num_Rampa,sensor,pulsos):
    start_time = time.time()
    '''
        num_Rampa: Número de la rampa a la que el producto se dirigirá

        sensor: Número del sensor recibido de la función rampas()

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
            
            #sleep(0.5)

            MA3.setLevel(500)
            MA2.setLevel(512)
        
        if estado_b3 != 0:
            MA3.setLevel(0)
            MA2.setLevel(0)
            
            tiempo = aleatorio()/2
            tf= time.time()
            print("Tiempo de despacho: ", tf-start_time) 
            eje_lineal(num_Rampa, sensor, pulsos, tiempo) #Envia los datos directamente a la función eje lineal con el número del sensor
    
    cambio_while = False
    
    plc.updateWait()

def rampas():
    start_time = time.time()
    
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
            despacho(rampa,B4,0)
        elif estado_B5 != 1:
            rampa = 2
            print("¡El producto se dirige a la rampa #2!")
            despacho(rampa,B5,209)
        elif estado_B6 != 1:
            rampa = 3
            print("¡El producto se dirige a la rampa #3!")
            despacho(rampa,B6 ,435)
        elif estado_B7 != 1:
            rampa = 4
            print("¡El producto se dirige a la rampa #4!")
            despacho(rampa,B7, 651)
        else:
            print("¡Todas las rampas están llenas!")

        tf= time.time()
        
        plc.updateWait()
    print("Tiempo de rampas: ", tf-start_time) 
    
if __name__ == "__main__":
    rampas()