import array
import pulseio
import board

pulse_read = pulseio.PulseIn(board.RCH1)

a_list = [1, 2]
b_list = range(4,9)
a_list += b_list
pulses = array.array('H', [65000, 1000])

for i, x in enumerate(a_list):
	SERVO = 'board.SERVO'+str(x)
	# print(SERVO)
	pwm = pulseio.PWMOut(eval(SERVO), duty_cycle=2 ** 15)
	pulse = pulseio.PulseOut(pwm)
	pulse.send(pulses)
	while len(pulse_read) == 0:
		pass
	print(len(pulse_read))
