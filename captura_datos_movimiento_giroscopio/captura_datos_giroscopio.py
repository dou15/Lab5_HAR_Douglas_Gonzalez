"""
    Código empleado en la captura de los datos a traves puerto serial
    que transmite las lecturas del giroscopio.
    Las lecturas son almacenadas en un archivo csv.
"""

#!/usr/bin/python3
import csv
from time import time

import serial

count = 0

serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=115200)

f = open("captura_datos_giroscopio.csv", "a+")
writer = csv.writer(f,delimiter=',', escapechar=',', quoting=csv.QUOTE_NONE)

encabezado = ['timestamp','gyrX','gyrY','gyrZ']
writer.writerow(encabezado)


while count < 10001:
    #if(serialPort.in_waiting > 0):
        datos = serialPort.readline().decode('ascii', errors='ignore')
        datosEnviar = datos.split()
        cantidadDatos = len(datosEnviar)
        print(datosEnviar)

        if cantidadDatos==4:
            rows = [x for x in datosEnviar]
            print(rows)
            writer.writerow(rows)
            f.flush()

        count += 1

exit()
