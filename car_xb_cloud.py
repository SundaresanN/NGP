#Libraries
import RPi.GPIO as GPIO
import time
from Adafruit_IO import *
from digi.xbee.devices import *

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
device = XBeeDevice('/dev/ttyS0',9600)
device.open()

#aio key from io.adafruit.com
aio = Client('')

if __name__ == '__main__':
    try:
        while True:
            mess = device.read_data()
            if mess is not None:
                print ("Free Slot available")
                time.sleep(1)
                data = aio.send('ultrasonic',1)
            else:
                print("Car engaged")
                time.sleep(1)
                data = aio.send('ultrasonic',0)
                continue

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
