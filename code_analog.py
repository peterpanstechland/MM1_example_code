# CircuitPython AnalogIn Demo
import time
import board
from analogio import AnalogIn

analog_in = AnalogIn(board.RCH1)


def get_voltage(pin):
    return (pin.value * 3.3) / 65536


while True:
    print((get_voltage(analog_in),))
    time.sleep(0.1)
