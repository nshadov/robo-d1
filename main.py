import time
from machine import Pin
from machine import I2C

led = Pin(2, Pin.OUT)
sclPin = Pin(5, Pin.OUT)
sdaPin = Pin(4, Pin.OUT)

class Main:
    def __init__(self):
        self.init_i2c()
    
    def init_i2c(self):
        print("[+] Initializing I2C ...")
        self.i2c = I2C(freq=9600, scl=sclPin, sda=sdaPin)
        devices = self.i2c.scan()
        print(f"[+] I2C devices: {devices}") 
    
    def run(self):
        print("[+] Initialization complete.")
        while True:
            if led.value():
                led.off()
            else:
                led.on()
            time.sleep_ms(250)