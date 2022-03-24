import ftrobopy

#Conexión con plc
plc= ftrobopy.ftrobopy("192.168.0.100")

print("Conectado a ", plc.getDevicename(), plc.getFirmwareVersion())