from time import sleep
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.1.208")
arrRampa={0,220,445,665}


def banda1(rampa):
    # Este es el movimiento de la banda lineal
    MA1 = plc.output(6)
    print(f"soy la rampa {rampa+1}")
    
    motor(MA1,512,3,0)
    
def motor(M,nivel, tiempo, cambio):
    M.setLevel(nivel)
    sleep(tiempo)
    M.setLevel(cambio)




def run():

    sensoresRampa=[]
    for x in range(1,9):
            sensoresRampa.append(plc.input(x))
    
    estado_sensores=[]
    for x in sensoresRampa:
        estado_sensores.append(x.state())
        
    while True:


        for x in range(0,len(estado_sensores)):
            estado_sensores[x]=sensoresRampa[x].state()

                
        plc.updateWait()


if __name__ == "__main__":
    run()
