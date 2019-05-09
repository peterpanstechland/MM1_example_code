from time import sleep
import math
import board
import pulseio
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogIn
import busio
import microcontroller
from micropython import const

def servo_duty_cycle(pulse_ms, frequency=300):
	period_ms = 1.0 / frequency * 1000.0
	duty_cycle = int(pulse_ms / (period_ms / 65534.0)) + 1
	return duty_cycle
#Left Ain1(Reverse) Ain2(Forward) Right Bin1(Reverse) Bin2(Forward)
#Bin2
servo_3 = pulseio.PWMOut(board.SERVO3)
#Ain2
servo_1 = pulseio.PWMOut(board.SERVO1)
#Ain1
servo_2 = pulseio.PWMOut(board.SERVO2)
#Bin1
servo_4 = pulseio.PWMOut(board.SERVO4)

# D1 = DigitalInOut(board.SERVO1)
# D1.direction = Direction.OUTPUT
# D2 = DigitalInOut(board.SERVO2)
# D2.direction = Direction.OUTPUT
# D3 = DigitalInOut(board.SERVO3)
# D3.direction = Direction.OUTPUT
# D4 = DigitalInOut(board.SERVO4)
# D4.direction = Direction.OUTPUT

lineFollow_left = DigitalInOut(board.SERVO5)
lineFollow_left.direction = Direction.INPUT
lineFollow_left.pull = Pull.UP
lineFollow_right = DigitalInOut(board.SERVO6)
lineFollow_right.direction = Direction.INPUT
lineFollow_right.pull = Pull.UP

Light_left = AnalogIn(board.RCH1)
Light_right = AnalogIn(board.RCH2)


def rightReverse():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(1.5)
	servo_4.duty_cycle = servo_duty_cycle(0)
def rightForward():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(1.5)
def leftReverse():
	servo_1.duty_cycle = servo_duty_cycle(1.5)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(0)
def leftForward():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(1.5)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(0)
def rightTurn():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(1.5)
	servo_3.duty_cycle = servo_duty_cycle(1.5)
	servo_4.duty_cycle = servo_duty_cycle(0)
def leftTurn():
	servo_1.duty_cycle = servo_duty_cycle(1.5)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(1.5)
def stop():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(0)

def reverse():
	servo_1.duty_cycle = servo_duty_cycle(1.5)
	servo_2.duty_cycle = servo_duty_cycle(0)
	servo_3.duty_cycle = servo_duty_cycle(1.5)
	servo_4.duty_cycle = servo_duty_cycle(0)

def forward():
	servo_1.duty_cycle = servo_duty_cycle(0)
	servo_2.duty_cycle = servo_duty_cycle(2)
	servo_3.duty_cycle = servo_duty_cycle(0)
	servo_4.duty_cycle = servo_duty_cycle(2)

def followLine():
	if lineFollow_left.value is True:
		servo_1.duty_cycle = servo_duty_cycle(0)
		servo_2.duty_cycle = servo_duty_cycle(1.5)
		servo_3.duty_cycle = servo_duty_cycle(1.2)
		servo_4.duty_cycle = servo_duty_cycle(0)
		sleep(0.2)
	else:
		forward()
	if lineFollow_right.value is True:
		servo_1.duty_cycle = servo_duty_cycle(1.2)
		servo_2.duty_cycle = servo_duty_cycle(0)
		servo_3.duty_cycle = servo_duty_cycle(0)
		servo_4.duty_cycle = servo_duty_cycle(1.5)
		sleep(0.2)
	else:
		forward()

def followLight():
	if Light_left.value < 200:
		reverse()
	elif  Light_right.value < 200:
		forward()
	else:
		stop()

while True:
	# print(Light_left.value)
	# sleep(1)
	# print(lineFollow_left.value)
	forward()
	# leftTurn()
	# followLight()
	# followLine()
	# circle()
	# break
	print("1")
