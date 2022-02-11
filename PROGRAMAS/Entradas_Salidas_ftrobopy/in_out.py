import ftrobopy
# conexión con el plc
# plc = ftrobopy.ftrobopy("192.168.7.2", 9600)
plc = ftrobopy.ftrobopy("192.168.0.101")
print("Nombre del controlador: ", plc.getDevicename())

# Obtener el estado y el tipo de las entradas y las salidas
O, I = plc.getConfig()
print("configuración de las salidas: ", O)
print("configuración de las entradas: ", I)


