import time, sys
import RPi.GPIO as GPIO
from Adafruit_IO import *

pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#Add your aio key here
aio = Client('')

def sense(channel):
    #print('Mine gas detected!')
    return

GPIO.add_event_detect(pin, GPIO.RISING)
GPIO.add_event_callback(pin, sense)

try:
    while True:
        time.sleep(0.5)
	print('Condition Normal')
	if GPIO.event_detected(pin):
		print ('Alert! Change in Gas content Detected')
		alert = aio.send('Mine Gas Sensor',1)
	else:
		alert = aio.send('Mine Gas Sensor',0)
except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()
