from machine import Pin, SPI

def set_current(a):

    cs = Pin(5, Pin.OUT)

    spi = SPI(0,baudrate=115200,polarity=0,phase=0,bits=8,firstbit=SPI.MSB,
                      sck=Pin(18),mosi=Pin(19),miso=Pin(16))

    cs.value(1)
    outputdata = a.to_bytes(2,'big')
    cs.value(0)
    spi.write(outputdata)
    cs.value(1)
