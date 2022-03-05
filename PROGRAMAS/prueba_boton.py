
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.1.208")

def run():
    
    boton = plc.input(2)
    
    sensores = [plc.input(1), plc.input(3), plc.input(4), plc.input(5)]

    motor_banda_lineal = plc.output(6)
    estado_sensores=[]
    for x in sensores:
        estado_sensores.append(x.state())
        

    while True:
        estado_boton = boton.state()
        for x in range(0,4):
            estado_sensores[x]=sensores[x].state()
        
       
        
        
        
        while estado_boton != 1:
            
            motor_banda_lineal.setLevel(512)
            estado_boton = boton.state()
            print(estado_boton)
        motor_banda_lineal.setLevel(0)
        print("estado del sensor es: ", estado_sensores)
        plc.updateWait()

if __name__ == "__main__":
    run()
