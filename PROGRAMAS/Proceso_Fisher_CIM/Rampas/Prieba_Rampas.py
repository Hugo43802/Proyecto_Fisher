from ast import If
from time import sleep
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.0.101")

def run():
    B3 = plc.input(4)
    B4 = plc.input(5)
    B5 = plc.input(6)
    B6 = plc.input(7)
    B7 = plc.input(8)
    
    MA2 = plc.output(6)
    
    while True:
        estado_B3 = B3.state()
        estado_B4 = B4.state()
        estado_B5 = B5.state()
        estado_B6 = B6.state()
        estado_B7 = B7.state()
        
        if estado_B4 == 1:
            MA2.setLevel(0)
            print("Lleno 4")
        else: 
            if estado_B3 == 1:
                MA2.setLevel(512)
               
                
            
                      
        if  estado_B5 == 1:
            print("Lleno 5")
        
        if  estado_B6 == 1:
            print("Lleno 6")
            MA2.setLevel(512)
            
        if  estado_B7 == 1:
            print("Lleno 7")
        

if __name__ == "__main__":
    run()