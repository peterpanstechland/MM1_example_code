import pulseio
import time
import board

list_a = [3, 1, 2]
list_b = range(4, 9)
list_a += list_b
list_c = list_a[:4]
list_c += sorted(list_a[:4])

pulse_read_1 = pulseio.PulseIn(board.RCH1, 1)
pulse_read_2 = pulseio.PulseIn(board.RCH2, 1)
pulse_read_3 = pulseio.PulseIn(board.RCH3, 1)
pulse_read_4 = pulseio.PulseIn(board.RCH4, 1)

# while True:
for i, j in zip(list_a, list_c):
		pwm_pin = "board.SERVO" + str(i)
		pwm = pulseio.PWMOut(eval(pwm_pin))
		pulse_name = "pulse_read_" + str(j)

		pwm.duty_cycle = 65534
		while len(eval(pulse_name)) == 0:
			pass
		eval(pulse_name).pause()
		print(pwm_pin, "at", pulse_name, ":", eval(pulse_name)[0])
		eval(pulse_name).clear()
		time.sleep(1)

		pwm.duty_cycle = 800
		time.sleep(1)
		while len(eval(pulse_name)) == 0:
			pass
		eval(pulse_name).pause()
		print(pwm_pin, "at", pulse_name, ":", eval(pulse_name)[0])

		eval(pulse_name).clear()
