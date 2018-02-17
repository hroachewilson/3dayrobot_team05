import struct
import serial

from settings import CAR_SERIAL_PORT


car = serial.Serial()
car.port = CAR_SERIAL_PORT
car.baudrate = 9600
car.open()

Stop=0# 0:false 1:true
Steer=0
Acceleration=0
Gear=0
Brakes=0
def send():
    global Stop,Steer,Acceleration,Gear,Brakes 
    car.write(':'.join([str(i) for i in [Stop,Steer,Acceleration,Gear,Brakes]]))
    if Stop:
        Stop=0
    pass

def stop():
    global Stop
    Stop=1
    


def steer(angle=0):
    global Steer
    Steer=angle
def acceleration(power=0):#0-100
    global Acceleration
    Acceleration=power
def gear(gearV=1):  # p:1,r:2,d:3   ###MAYBE ADD DICTIONARY
    global Gear
    Gear=gearV
def brakes(power=0):#0-100
    global Brakes
    Brakes=power
if __name__=="__main__":
    for i in range(1000):
        brakes(98)
        steer(100)
        send()
