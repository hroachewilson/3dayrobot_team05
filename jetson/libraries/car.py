import struct
import serial

from settings import CAR_SERIAL_PORT


car = serial.Serial()
car.port = CAR_SERIAL_PORT
car.baudrate = 9600
car.open()


def stop():
    car.write(b's')


def steer(angle=0):
    car.write(b"d")


def acceleration(power=0):#0-100
    car.write(b'a')


def gear(gear=1):  # p:1,r:2,d:3   ###MAYBE ADD DICTIONARY
    car.write(b"g")


def brakes(power=0):#0-100
    car.write(b"b")
    
if __name__=="__main__":
    steer(98.00)
    send()
