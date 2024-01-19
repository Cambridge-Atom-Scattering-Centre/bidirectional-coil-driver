from machine import UART, Pin, Timer, SPI
from set_current import set_current
import time, math

uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

a = 3.8158054e-6
b = -125074.42e-6
# the current and the number N sent to the DAC follow I = a*N-b

while True:
    time.sleep(0.001)
    if uart.any():

        data = uart.read()
        msg = data.decode()
        current = float(msg[2:])
        N = math.ceil((current-b)/a)
        
        # set the current if the N is within the allowed range
        if N>=0 and N<2**16:
            
            set_current(N)
            
            # see if there is a fault on the PSU
            FAULT = Pin(16, Pin.IN)
            if FAULT.value() == 0:
                uart.write('fault\r')
            else:
                uart.write('success\r')
            
        else:
            uart.write('out of range\r')
