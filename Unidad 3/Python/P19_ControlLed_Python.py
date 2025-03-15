import serial as control
arduino = control.Serial("COM7",baudrate=9600,timeout=1)
while True:
    v=input("valor: ")
    arduino.write(v.encode())