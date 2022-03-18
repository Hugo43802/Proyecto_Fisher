from time import sleep
import ftrobopy


plc = ftrobopy.ftrobopy("192.168.1.240")
#plc = ftrobopy.ftrobopy("192.168.0.101")

#MOTORES

MA5 = plc.output(8)


def run():
    while True:
        MA5.setLevel(512)

if __name__ == "__main__":
    run()