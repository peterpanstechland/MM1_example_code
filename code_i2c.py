# CircuitPython Test for Robotics Masters MM1
#
# Notes:
#   This is to be run using CircuitPython 3.1
#
import board
import digitalio
import time
import busio

servo_pins = [board.SERVO1, board.SERVO2, board.SERVO3,
              board.SERVO4, board.SERVO5, board.SERVO6,
              board.SERVO7, board.SERVO8]

rc_pins = [board.RCH1, board.RCH2, board.RCH3, board.RCH4]

# setup I2C
i2c = busio.I2C(board.SCL, board.SDA)
i2c_2 = busio.I2C(board.GPS_SCL, board.GPS_SDA)

while True:
    while not i2c_2.try_lock():
        pass

    [print(hex(x)) for x in i2c_2.scan()]

    i2c_2.unlock()

    time.sleep(3)
