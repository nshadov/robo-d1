import time
from machine import Pin

led = Pin(2, Pin.OUT)

class Main:
    def __init__(self):
        pass
    
    def run(self):
        while True:
            if led.value():
                led.off()
            else:
                led.on()
            time.sleep_ms(250)