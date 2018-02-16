import struct
import serial

from settings import CAR_SERIAL_PORT


car = serial.Serial()
car.port = CAR_SERIAL_PORT
car.baudrate = 9600
car.open()

Stop = 0
Steer = 0
Accelerator = 0
Gear = 0
Brakes = 0

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
    Steer = round(float(angle), 2)


def acceleration(power=0):
    global Accelerator
    Accelerator = float(power)


def gear(gear=1):  # p:1,r:2,d:3   ###MAYBE ADD DICTIONARY
    global Gear
    Gear = gear


def brakes(power=0):
    global Brakes
    Brakes = float(power)
