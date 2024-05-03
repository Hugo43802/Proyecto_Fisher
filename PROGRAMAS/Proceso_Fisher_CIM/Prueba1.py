import ftrobopy

plc = ftrobopy.ftrobopy("192.168.0.129")

#PF1
pf1 = plc.output(1)
#B1
B1 = plc.input(1)


def inicio():
    state = B1.state() 
    pf1.setLevel(0)
    while 1:
        
        print("Luz encendida")
        ns = B1.state()
        if ns != state:
            print("state(), getCurrentInput():", ns, plc.getCurrentInput(0))
            pf1.setLevel(0)
        plc.updateWait()

if __name__ == "__main__":
    inicio()
