import time
from machine import Pin

led = Pin(2, Pin.OUT)

def main():

    while True:
        if led.value():
            led.off()
        else:
            led.on()
        time.sleep_ms(250)