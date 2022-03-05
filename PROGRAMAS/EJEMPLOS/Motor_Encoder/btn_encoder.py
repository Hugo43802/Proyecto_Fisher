import ftrobopy

'''
Controlar motor con encoder (rojo) mediante la pulsación de un botón

'''

plc = ftrobopy.ftrobopy("192.168.1.208")

def run():
    btn = plc.input(1)
    motor = plc.motor(1)

    estado_boton = btn.state() 
    print("EL botón está en: ", estado_boton)
    
    while True:
        ns = btn.state()
        motor.setSpeed(0)
        
        if ns != 0:
            motor.setSpeed(256)
            estado_boton = ns
            print("Nuevo Estado: ", ns)
        plc.updateWait()

if __name__ == "__main__":
    run()