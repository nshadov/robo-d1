import time
from machine import Pin
from machine import I2C
from random import getrandbits
import lolin_i2c_motor as lm


led = Pin(2, Pin.OUT)
sclPin = Pin(5, Pin.OUT)
sdaPin = Pin(4, Pin.OUT)
I2C_MOTOR_ID = 48

def random():
    r = int(getrandbits(8)) * 4
    if r > 1000:
        print("R="+str(100))
        return 100
    else:
        print("R="+str(int(r/10)))
        return int(r/10)

class Main:
    def __init__(self):
        self.motor = None
        self.init_i2c()
    
    def init_i2c(self):
        print("[+] Initializing I2C ...")
        self.i2c = I2C(freq=9600, timeout=5000, scl=sclPin, sda=sdaPin)
        devices = self.i2c.scan()
        if I2C_MOTOR_ID in devices:
            self.motor = lm.Lolin_I2C_Motor(self.i2c, I2C_MOTOR_ID)
            print(f"[+] I2C motor found: {self.motor}")
            print("Status:"+str(self.motor.get_status()))
            self.motor.change_freq(lm.MOTOR_CH_BOTH, 1000)
            self.motor.change_status(lm.MOTOR_CH_BOTH, lm.MOTOR_STATUS_CW);
    
    def run(self):
        print("[+] Initialization complete.")
        while True:
            if led.value():
                led.off()
                self.motor.change_duty(lm.MOTOR_CH_A, int(20+random()));
                self.motor.change_duty(lm.MOTOR_CH_B, int(20+random()));
            else:
                led.on()
                self.motor.change_duty(lm.MOTOR_CH_A, int(20+random()));
                self.motor.change_duty(lm.MOTOR_CH_B, int(20+random()));
            time.sleep_ms(250 + int(random()*10))