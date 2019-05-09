import time
import board
from digitalio import DigitalInOut, Direction, Pull

D1 = DigitalInOut(board.SERVO1)
D1.direction = Direction.INPUT
print(D1.value)

D2 = DigitalInOut(board.SERVO2)
D2.direction = Direction.INPUT
print(D2.value)

last_position2 = None
enc_l = 0
enc_r = 0
while True:
	position2 = D2.value
	position1 = D1.value

	if position1 == None or position1 != last_position1:
		enc_r = enc_r + 1
		print(enc_r)
	last_position1 = position1

	if position2 == None or position2 != last_position2:
		enc_l = enc_l + 1
		print(enc_l)
	last_position2 = position2
