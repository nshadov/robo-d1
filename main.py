import time

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