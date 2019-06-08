#!/usr/bin/python

from gpiozero import PWMOutputDevice
import RPi.GPIO as GPIO
import time
import board
from adafruit_ina219 import INA219

a = PWMOutputDevice(13, frequency = 500)

GPIO.setmode(GPIO.BCM)

ENBL = 20
DIR = 21

GPIO.setup(ENBL,GPIO.OUT)

GPIO.setup(DIR,GPIO.OUT)

i2c_bus = board.I2C()

ina219 = INA219(i2c_bus)

Direction = "Open"

def run():

    current = -ina219.current/1000
    bus_voltage = ina219.bus_voltage

    print("Current: {:9.6f} A".format(current))
    #print("Load Voltage:   {:6.3f} V".format(bus_voltage))

    return current


if __name__ == '__main__':
    try:
        
        if Direction == "Close":
            GPIO.output(ENBL,True)

            GPIO.output(DIR,False)

            time.sleep(.1)

            print("Starting Motor...")

            a.value = .9

            cur = -ina219.current/1000
            
            while cur <1.5:
                cur = run()
                #dist = distance()
                #print ("Measured Distance = %.1f cm" % dist)
                time.sleep(.1)
 
        if Direction == "Open":
            GPIO.output(ENBL,True)

            GPIO.output(DIR,True)

            time.sleep(.1)

            print("Starting Motor...")

            a.value = .9

            cur = -ina219.current/1000
            
            while cur <1.0:
                cur = run()
                #dist = distance()
                #print ("Measured Distance = %.1f cm" % dist)
                time.sleep(.1)
                
                
        a.value = 0.0
        
        a.close
        
        GPIO.cleanup()
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Movement stopped by User")
        a.value = 0.0
        
        a.close
        
        GPIO.cleanup()