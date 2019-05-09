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

def data_map(x, in_min, in_max, out_min, out_max):
	return (x - in_min)*(out_max - out_min) / (in_max - in_min) + out_min

# Create a function to simplify setting PWM duty cycle for the servo:
def servo_duty_cycle(pulse_ms, frequency=50):
	period_ms = 1.0 / frequency * 1000.0
	duty_cycle = int(pulse_ms / (period_ms / 65534.0)) + 1
	return duty_cycle

def Servo_init():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(0)
	servo_5.duty_cycle = servo_duty_cycle(0)
	servo_6.duty_cycle = servo_duty_cycle(0)
def Servo_sweep():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(0)
	servo_5.duty_cycle = servo_duty_cycle(0)
	servo_6.duty_cycle = servo_duty_cycle(0)
	sleep(1)
	servo_1.duty_cycle = servo_duty_cycle(0.5)
	servo_2.duty_cycle = servo_duty_cycle(0.5)
	servo_3.duty_cycle = servo_duty_cycle(0.5)
	servo_4.duty_cycle = servo_duty_cycle(0.5)
	servo_5.duty_cycle = servo_duty_cycle(0.5)
	servo_6.duty_cycle = servo_duty_cycle(0.5)
	sleep(1)
	servo_1.duty_cycle = servo_duty_cycle(1)
	servo_2.duty_cycle = servo_duty_cycle(1)
	servo_3.duty_cycle = servo_duty_cycle(1)
	servo_4.duty_cycle = servo_duty_cycle(1)
	servo_5.duty_cycle = servo_duty_cycle(1)
	servo_6.duty_cycle = servo_duty_cycle(1)
	sleep(1)
	servo_1.duty_cycle = servo_duty_cycle(1.5)
	servo_2.duty_cycle = servo_duty_cycle(1.5)
	servo_3.duty_cycle = servo_duty_cycle(1.5)
	servo_4.duty_cycle = servo_duty_cycle(1.5)
	servo_5.duty_cycle = servo_duty_cycle(1.5)
	servo_6.duty_cycle = servo_duty_cycle(1.5)
	sleep(1)
	servo_1.duty_cycle = servo_duty_cycle(2)
	servo_2.duty_cycle = servo_duty_cycle(2)
	servo_3.duty_cycle = servo_duty_cycle(2)
	servo_4.duty_cycle = servo_duty_cycle(2)
	servo_5.duty_cycle = servo_duty_cycle(2)
	servo_6.duty_cycle = servo_duty_cycle(2)

def sqrt_root(sq_num_x, sq_num_y):
	return math.sqrt(sq_num_x*sq_num_x+sq_num_y*sq_num_y)
# Initialise PWM output for the servo (on pin D5):
servo_3 = pulseio.PWMOut(board.SERVO3, frequency=50)
servo_1 = pulseio.PWMOut(board.SERVO1, frequency=50)
servo_2 = pulseio.PWMOut(board.SERVO2, frequency=50)
# servo_3 = pulseio.PWMOut(board.SERVO3, frequency=50)
servo_4 = pulseio.PWMOut(board.SERVO4, frequency=50)
servo_5 = pulseio.PWMOut(board.SERVO5, frequency=50)
servo_6 = pulseio.PWMOut(board.SERVO6, frequency=50)

pitch_pwm = 1.5
roll_pwm = 1.5
roll_pwm_3 = 1.5
multi = 180/math.pi

while True:

	# if start == 0:
	# 	if (not button_a.value):
	# 		#enable 5V Power Rail with Main Switch
	# 		PowerRail.pull = digitalio.Pull.UP
	# 		start = 1
	# 		Servo_init()
	# else:
	# 	# Servo_sweep()
	accel_x, accel_y, accel_z = sensor.acceleration
	pitch_data = sqrt_root(accel_y, accel_z)
	pitch = math.atan2(accel_x, pitch_data)*multi
	roll = math.atan2(-accel_y, accel_z)*multi
	#
	pitch_pwm = data_map(pitch, -90, 90, 0, 2)
	roll_pwm = data_map(roll, -90, 90, 2, 0)
	roll_pwm_3 = data_map(roll, -90, 90, 0, 2)
	pitch_pwm = (pitch_pwm + pitch_pwm) / 2
	roll_pwm = (roll_pwm + roll_pwm) / 2
	roll_pwm_3 = (roll_pwm_3 + roll_pwm_3) / 2
	sleep(0.2)
	#
	# print('roll_pwm = ', roll_pwm)
	print('pitch = ', pitch_pwm)
	# servo_1.duty_cycle = servo_duty_cycle(roll_pwm)
	# 	servo_2.duty_cycle = servo_duty_cycle(roll_pwm)
	# 	servo_3.duty_cycle = servo_duty_cycle(roll_pwm_3)
	# 	servo_4.duty_cycle = servo_duty_cycle(pitch_pwm)
