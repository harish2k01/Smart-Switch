import serial
import keyboard
import csv
import time
from datetime import datetime
#string=["hello,world,beast,brock,lesnar","hello,world"]
##def write_data():
##    data = arduino.readline()
##    return data  

arduino = serial.Serial(port='COM3',baudrate=9600,timeout=1)
##print(arduino.isOpen())
if(arduino.isOpen() == False):
    arduino.open()
##date=datetime.now()

f = open('RealTimeSampleData.csv', 'w+',newline='')
w = csv.writer(f, delimiter = ',')
time.sleep(2)
writer = csv.DictWriter(f, fieldnames=["Datetime", "Watts"])
writer.writeheader()
while True:
##    date=datetime.now()
    value = round(float(arduino.readline().decode('utf-8').rstrip()))
    ##print(serial)
    value=datetime.now().strftime('%d-%m-%Y - %H:%M:%S.%f')[:-3]+","+str(value)
    w.writerow(value.split(','))
    print(value)
    if(keyboard.is_pressed('q')):
        time.sleep(1)
        f.close()
        break

        
f.close()
