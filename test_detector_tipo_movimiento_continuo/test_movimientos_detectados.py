"""
    Captura las lecturas transmitidas por el test_detector_tipo_movimiento_continuo que corre en el
    arduino, y guarda los resultados en un archivo csv llamado movimientos_detectados
"""

#!/usr/bin/python3
import csv
from time import time

import serial

serialPort = serial.Serial(port = "/dev/ttyACM0", baudrate=115200)

f = open("movimientos_detectados.csv", "a+")
writer = csv.writer(f,delimiter=',', escapechar=',', quoting=csv.QUOTE_NONE)

while (1):
        datos = serialPort.readline().decode('ascii', errors='ignore')
        datosEnviar = datos.split()
        cantidadDatos = len(datosEnviar)
        print(datosEnviar)

        ##if cantidadDatos==4:
        rows = [x for x in datosEnviar]
        print(rows)
        writer.writerow(rows)
        f.flush()
