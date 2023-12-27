import serial
import time

s = serial.Serial('COM5', 9600, timeout=1)

while 1:
    s.readline().decode("utf-8")
    volt = s.readline().decode("utf-8")
    print(volt)
    svolt = volt.split(sep=';')
    
    print("PSV " + svolt[0])
    print("PDV " + svolt[1])

    time.sleep(1)