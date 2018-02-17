import struct
import serial

from settings import CAR_SERIAL_PORT


car = serial.Serial()
car.port = CAR_SERIAL_PORT
car.baudrate = 9600
car.open()

Stop = 0
Steer = 0.01
Accelerator = 0.01
Gear = 0
Brakes = 0.01

def send():
    global Stop, Gear, Steer, Accelerator, Brakes
    car.write(
        ','.join(map(lambda x: str(x), [Stop, Gear, Steer, Accelerator, Brakes]))+'\n')
    if Stop:
        Stop = False


def stop():
    global Stop
    Stop = 1


def steer(angle=0):
    global Steer
    Steer = str(round(float(angle)+0.01, 2))
    Steer=Steer.zfill(6)
    Steer=Steer[-6:]


def acceleration(power=0):
    global Accelerator
    Accelerator = str(round(float(power)+0.01, 2))
    Accelerator=Accelerator.zfill(6)
    Accelerator=Accelerator[-6:]


def gear(gear=1):  # p:1,r:2,d:3   ###MAYBE ADD DICTIONARY
    global Gear
    Gear = gear


def brakes(power=0):
    global Brakes
    
    Brakes = str(round(float(power)+0.01, 2))
    Brakes=Brakes.zfill(6)
    Brakes=Brakes[-6:]

if __name__=="__main__":
    steer(98.00)
    send()
