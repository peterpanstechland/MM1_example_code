# CircuitPython Test for Robotics Masters MM1
#
# Notes:
#   This is to be run using CircuitPython 3.1
#
from ublox_gps import MicropyGPS

import board
import digitalio
import time
import busio

UPDATE_GPS = const(10)

# setup I2C
i2c = busio.I2C(board.SCL, board.SDA)
i2c_2 = busio.I2C(board.GPS_SCL, board.GPS_SDA)
uart = busio.UART(board.GPS_TX, board.GPS_RX, baudrate=9600)

my_gps = MicropyGPS()
stat = None
updateGPS = time.monotonic()

while True:
    print(time.monotonic() - updateGPS)
    try:
        if(time.monotonic() - updateGPS >= UPDATE_GPS):
            updateGPS = time.monotonic()
            stat = my_gps.updateall(uart.readall())
            print("stat")
        if(stat != None):
            print("1")
    except:
        print(my_gps)
        my_gps.stringclean()
        time.sleep(1)
