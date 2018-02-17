import struct
import serial

from settings import CAR_SERIAL_PORT


car = serial.Serial()
car.port = CAR_SERIAL_PORT
car.baudrate = 19200
car.open()


def stop():
    car.write(b's')


def steer(angle=0):
    car.write(b"d")
    car.write(struct.pack('>h',angle))

def acceleration(power=0):#0-100
    car.write(b'a')
    car.write(struct.pack('<B',power))


def gear(gear=1):  # p:1,r:2,d:3   ###MAYBE ADD DICTIONARY
    car.write(b"g")
    car.write(struct.pack('<B',gear))

def brakes(power=0):#0-100
    car.write(b"b")
    car.write(struct.pack('<B',power))
if __name__=="__main__":
    for i in range(1000):
        brakes(98)
        steer(100)
