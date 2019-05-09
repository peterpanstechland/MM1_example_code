import pulseio
import time
import board

pwm = pulseio.PWMOut(board.SERVO2)
pulse_read = pulseio.PulseIn(board.RCH2, 1)

while True:
	pwm.duty_cycle = 65534
	# print(duty)
	while len(pulse_read) == 0:
		pass
	pulse_read.pause()
	print("1:", pulse_read[0])
	pulse_read.clear()
	pulse_read.resume(60)

	pwm.duty_cycle = 900
	# print(2 ** 14)
	while len(pulse_read) == 0:
		pass
	pulse_read.pause()
	print("2:", pulse_read[0])
	time.sleep(2)
	pulse_read.clear()
	pulse_read.resume(60)
