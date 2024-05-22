# Built based on https://github.com/wemos/LOLIN_I2C_MOTOR_Library/blob/master/src/LOLIN_I2C_MOTOR.cpp

MOTOR_CH_A = 0x00
MOTOR_CH_B = 0x01
MOTOR_CH_BOTH = 0x02

MOTOR_STATUS_STOP = 0x00
MOTOR_STATUS_CCW = 0x01
MOTOR_STATUS_CW = 0x02

'''
  motor.changeFreq(MOTOR_CH_BOTH, 1000); //Change A & B 's Frequency to 1000Hz.

  motor.changeStatus(MOTOR_CH_A, MOTOR_STATUS_CCW);
  motor.changeStatus(MOTOR_CH_B, MOTOR_STATUS_CW);
  motor.changeDuty(MOTOR_CH_A, 80);
  motor.changeDuty(MOTOR_CH_B, 80);
  delay(1000);
  
  motor.changeStatus(MOTOR_CH_BOTH, MOTOR_STATUS_STOP);
  delay(500);
'''

'''I2C_Motor is a class for interacting with LOLIN HR8833 motor shild over I2C'''
class Lolin_I2C_Motor:
    def __init__(self, i2c, address=0x48):
        self._address = address
        self._i2c = i2c
    
    def change_freq(self, channel, freq):
        data = bytearray([0x05, channel])
        data.extend(freq.to_bytes(3, 'little'))
        self._i2c.writeto(self._address, data)
        time.sleep_ms(50)
    
    def change_duty(self, channel, duty):
        data = bytearray([0x06, channel])
        duty_int = int(duty * 100)
        data.extend(duty_int.to_bytes(2, 'little'))
        self._i2c.writeto(self._address, data)
        time.sleep_ms(50)
    
    def change_status(self, channel, status):
        data = bytearray([0x04, channel, status])
        self._i2c.writeto(self._address, data)
        time.sleep_ms(50)
    
    def get_status(self):
        data = bytearray([0x01])
        self._i2c.writeto(self._address, data)
        time.sleep_ms(50)
        data = self._i2c.readfrom(self._address, 2)
        product_id = data[0]
        version = data[1]
        return (product_id, version)

    def reset(self):
        data = bytearray([0x02])
        self._i2c.writeto(self._address, data)
        time.sleep_ms(50)


    def change_address(self, address):
        data = bytearray([0x03, address])
        self._i2c.writeto(self._address, data)
        time.sleep_ms(50)
        
    def __str__(self):
        return "{'i2c':"+str(self._address)+"}"