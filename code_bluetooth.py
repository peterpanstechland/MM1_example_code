import board
import busio
import digitalio

print("running")

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

uart = busio.UART(board.UART_TX, board.UART_RX, baudrate=115200)
local = busio.UART(board.TX, board.RX, baudrate=9600)

print("also running")
counter = 0

while True:
    data = uart.read(32)  # read up to 32 bytes
    dataSend = local.read(32)
    arr = bytearray(data)
	print(data)  # this is a bytearray type

    if data is not None:
        counter = 0
        led.value = True

        # convert bytearray to string
        data_string = ''.join([chr(b) for b in data])
        print(data_string, end="")

        led.value = False

    if dataSend is not None:
        led.value = True

        # presume that you are using serial terminal emulator
        uart.write(dataSend)

        led.value = False
