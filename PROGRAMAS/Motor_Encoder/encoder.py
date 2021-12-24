import ftrobopy

'''
Controlar motor con encoder (rojo)

'''

plc = ftrobopy.ftrobopy("192.168.1.208")
# txt = ftrobopy.ftrobopy('192.168.7.2', 65000)

def run():
    mot1 = 0
    motor = plc.motor(1)
    motor.setSpeed(512)
    motor.setDistance(750)

    while not motor.finished():
        n = plc.getCurrentCounterValue(mot1)
        cd = motor.getCurrentDistance()
        print("La distancia actual del motor es: ", cd, n)
        plc.updateWait()

if __name__ == "__main__":
    run()