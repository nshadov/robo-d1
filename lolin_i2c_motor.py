# Built based on https://github.com/wemos/LOLIN_I2C_MOTOR_Library/blob/master/src/LOLIN_I2C_MOTOR.cpp

GET_SLAVE_STATUS = b'1'

MOTOR_CH_A = b'0'
MOTOR_CH_B = b'1'
MOTOR_CH_BOTH = b'2'

MOTOR_STATUS_STOP = b'0'
MOTOR_STATUS_CCW = b'1'
MOTOR_STATUS_CW = b'2'

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
    def __init__(self, i2c_id):
        self.id = i2c_id
    
    def change_freq(self, channel, freq):
        pass
    
    def change_duty(self, channel, duty):
        pass
    
    def change_status(self, channel, status):
        pass
    
    def get_status(self, i2c):
        i2c.writeto(self.id, GET_SLAVE_STATUS)
        result = i2c.readfrom(self.id, 2)
        return result
        
    def __str__(self):
        return "{'i2c':"+str(self.id)+"}"