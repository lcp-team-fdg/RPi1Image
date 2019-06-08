from gpiozero import PWMOutputDevice
import RPi.GPIO as GPIO
import time

a = PWMOutputDevice(16, frequency = 20000)
b = PWMOutputDevice(23, frequency = 20000)
c = PWMOutputDevice(13, frequency = 500)


a.value = 0.0
b.value = 0.0
c.value = 0.0



a.close
b.close
c.close