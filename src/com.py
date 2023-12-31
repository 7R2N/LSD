import serial
import time

def serial_collector(data_arr):
    s = serial.Serial('COM5', 9600, timeout=1)

    for i in range(2):
        row = []
        s.readline().decode("utf-8")
        volt = s.readline().decode("utf-8")
        svolt = volt.split(sep=';')
            
        psv = float(svolt[0])
        pdv = float(svolt[1])
            
        print("PSV " + str(psv))
        print("PDV " + str(pdv))

        dvolt = [psv, pdv]

        print(dvolt)

        row.append(dvolt)

    data_arr.append(row)

    time.sleep(1)
