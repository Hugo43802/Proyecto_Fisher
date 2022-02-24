from time import sleep
import ftrobopy

plc = ftrobopy.ftrobopy("192.168.0.101")

def transporte():
    
    # Inicializar sensores reed
    b3 = plc.input(4)
    
    b4 = plc.input(5)
    
    
    MA2 = plc.output(6)
    
    while True:
        ns_b3 = b3.state()
        ns_b4 = b4.state()
            
        if ns_b3 != 0:
            print("Entra a b3")
            MA2.setLevel(512)
    
        elif ns_b4 != 0:
            MA2.setLevel(0)
        
        plc.updateWait()
            
if __name__ == "__main__":
    transporte()