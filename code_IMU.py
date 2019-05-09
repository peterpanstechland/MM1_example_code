from time import sleep
import math
import board
import pulseio
import digitalio
import busio
import microcontroller
from micropython import const
# from adafruit_mpu9250 import adafruit_mpu9250 as ss

import adafruit_mpu9250

# Initialise IMU communication
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_mpu9250.MPU9250_I2C(i2c)

while True:

	print('Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.acceleration))
	print('Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.magnetic))
	print('Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})'.format(*sensor.gyro))
	print('Temperature: {0:0.3f}C'.format(sensor.temperature))
