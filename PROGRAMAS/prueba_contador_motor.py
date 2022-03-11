from time import sleep
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.0.101")

MA1_2 = plc.output(2)
MA1 = plc.output(1)
BG1 = plc.input(1)
    
def reset():
    '''
    Proceso reset para colocar el eje lineal en posición de referencia.
    Se enciende MA1. Se compara el estado del botón, así se apaga el motor
    
    "Por dentro del PLC la comparación del botón, entonces están invertidos los valores de 1 = apagado, 0 = encendido"
    '''
    print("Entramos a reset!")
    MA1.setLevel(512)
    
    if BG1.state() != 0:
         MA1.setLevel(0)
    

    '''
    La variable cambio While a true para que inicie al secuencia. además se da inicio a la función reset.
    se espera un tiempo de 5 segundos.
    '''
def run():
    cambio_while = True
    reset()
    sleep(5)
    
    '''
    get.CurrentCounterValue lee el contador existente en la conexión.
    C2 = Obtiene la posición inicial de la banda
    '''
    C2 = plc.getCurrentCounterValue(0)
    print("eL VALOR DE c2 es: ", C2)
    
    '''
    Meta = Variable a la que se quiere llegar (objetivo), es la posición de la banda para llegar a las rampas
    (Revisar archivo Rampas.txt)
    '''
    meta = C2 + 20
    
    '''
    Verificar siempre que es necesario apagar el último motor en uso
    
    Se enciende MA1_2.setlevel() y toma el valor actual de C1 (contador en ejecución)
    
    en el momento que el contador C1 sea mayor o igual a la meta, detiene el motor MA1_2 y sale del ciclo
    '''  
    while cambio_while:
        MA1.setLevel(0)
        MA1_2.setLevel(512)
        C1 = plc.getCurrentCounterValue(0)
        print(C1)
        
        if plc.getCurrentCounterValue(0) >= meta:
            MA1_2.setLevel(0)
            print("Motor detenido")
            cambio_while = False
        
        plc.updateWait()

if __name__ == "__main__":
    run()