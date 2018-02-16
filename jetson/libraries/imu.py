import FaBo9Axis_MPU9250
import math

imu = FaBo9Axis_MPU9250.MPU9250()

direction = imu.readMagnet()
direction = math.atan2(direction['x'], direction['z'])


def getCompass():
    global direction
    mag = imu.readMagnet()
    val = math.atan2(mag['x'], mag['y'])
    if val != 0.0:
        direction = val
    direction = math.degrees(direction)
    direction = (direction + 180) % 360
    return direction
