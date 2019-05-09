from time import sleep
import board
import pulseio

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
	servo_1.duty_cycle = servo_duty_cycle(1)
	servo_2.duty_cycle = servo_duty_cycle(1)
	servo_3.duty_cycle = servo_duty_cycle(1)
	servo_4.duty_cycle = servo_duty_cycle(1)
	servo_5.duty_cycle = servo_duty_cycle(1)
	servo_6.duty_cycle = servo_duty_cycle(1)
	servo_7.duty_cycle = servo_duty_cycle(1)
	servo_8.duty_cycle = servo_duty_cycle(1)
	sleep(2)
	servo_1.duty_cycle = servo_duty_cycle(2)
	servo_2.duty_cycle = servo_duty_cycle(2)
	servo_3.duty_cycle = servo_duty_cycle(2)
	servo_4.duty_cycle = servo_duty_cycle(2)
	servo_5.duty_cycle = servo_duty_cycle(2)
	servo_6.duty_cycle = servo_duty_cycle(2)
	servo_7.duty_cycle = servo_duty_cycle(2)
	servo_8.duty_cycle = servo_duty_cycle(2)
	sleep(2)

# Initialise PWM output for the servo (on pin D5):
servo_3 = pulseio.PWMOut(board.SERVO3, frequency=50)
servo_1 = pulseio.PWMOut(board.SERVO1, frequency=50)
servo_2 = pulseio.PWMOut(board.SERVO2, frequency=50)
servo_4 = pulseio.PWMOut(board.SERVO4, frequency=50)
servo_5 = pulseio.PWMOut(board.SERVO5, frequency=50)
servo_6 = pulseio.PWMOut(board.SERVO6, frequency=50)
servo_7 = pulseio.PWMOut(board.SERVO7, frequency=50)
servo_8 = pulseio.PWMOut(board.SERVO8, frequency=50)

while True:
	duty = servo_duty_cycle(20)
	print(duty)
	servo_1.duty_cycle = duty
	sleep(1)
	duty_2 = servo_duty_cycle(5)
	servo_1.duty_cycle = duty_2
	print(duty_2)
	sleep(1)
