#!/usr/bin/python
import RPi.GPIO as GPIO
import time
from gpiozero import PWMOutputDevice
import board
from adafruit_ina219 import INA219
 
GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER1 = 22
GPIO_TRIGGER2 = 18
#GPIO_TRIGGER3 = 5
#GPIO_TRIGGER4 = 5
GPIO_ECHO1 = 26
GPIO_ECHO2 = 17
GPIO_ECHO3 = 19
GPIO_ECHO4 = 25
GPIO_ECHO5 = 5
GPIO_ECHO6 = 6
#GPIO_ECHO7 = 6
#GPIO_ECHO8 = 6
#GPIO_ECHO9 = 6
#GPIO_ECHO10 = 6
#GPIO_ECHO11 = 6
#GPIO_ECHO12 = 6
 
GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
#GPIO.setup(GPIO_TRIGGER3, GPIO.OUT)
#GPIO.setup(GPIO_TRIGGER4, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_ECHO2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_ECHO3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_ECHO4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_ECHO5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GPIO_ECHO6, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_ECHO7, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_ECHO8, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_ECHO9, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_ECHO10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_ECHO11, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#GPIO.setup(GPIO_ECHO12, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

GPIO.add_event_detect(GPIO_ECHO1, GPIO.FALLING)
GPIO.add_event_detect(GPIO_ECHO2, GPIO.FALLING)
GPIO.add_event_detect(GPIO_ECHO3, GPIO.FALLING)
GPIO.add_event_detect(GPIO_ECHO4, GPIO.FALLING)
GPIO.add_event_detect(GPIO_ECHO5, GPIO.FALLING)
GPIO.add_event_detect(GPIO_ECHO6, GPIO.FALLING)
#GPIO.add_event_detect(GPIO_ECHO7, GPIO.FALLING)
#GPIO.add_event_detect(GPIO_ECHO8, GPIO.FALLING)
#GPIO.add_event_detect(GPIO_ECHO9, GPIO.FALLING)
#GPIO.add_event_detect(GPIO_ECHO10, GPIO.FALLING)
#GPIO.add_event_detect(GPIO_ECHO11, GPIO.FALLING)
#GPIO.add_event_detect(GPIO_ECHO12, GPIO.FALLING)

TIMEOUT=.02

ELAPSED = time.time()

a = PWMOutputDevice(16, frequency = 20000)
b = PWMOutputDevice(23, frequency = 20000)

DIR1 = 12
DIR2 = 24

GPIO.setup(DIR1,GPIO.OUT)
GPIO.setup(DIR2,GPIO.OUT)

Direction = "Left"

DistanceArray=[]

PWR = .2

DriveTimeOut = 10000

DistanceOut = 40

def distance():
    
    DistanceArray=[]
    
    i1=0
    i2=0
    i3=0
    i4=0
    i5=0
    i6=0
#    i7=0
#    i8=0
#    i9=0
#    i10=0
#    i11=0
#    i12=0
    
    GPIO.event_detected(GPIO_ECHO1)
    GPIO.event_detected(GPIO_ECHO2)
    GPIO.event_detected(GPIO_ECHO3)
    GPIO.event_detected(GPIO_ECHO4)
    GPIO.event_detected(GPIO_ECHO5)
    GPIO.event_detected(GPIO_ECHO6)
#    GPIO.event_detected(GPIO_ECHO7)
#    GPIO.event_detected(GPIO_ECHO8)
#    GPIO.event_detected(GPIO_ECHO9)
#    GPIO.event_detected(GPIO_ECHO10)
#    GPIO.event_detected(GPIO_ECHO11)
#    GPIO.event_detected(GPIO_ECHO12)
    
    GPIO.output(GPIO_TRIGGER1, GPIO.HIGH)
    GPIO.output(GPIO_TRIGGER2, GPIO.HIGH)
#    GPIO.output(GPIO_TRIGGER3, GPIO.HIGH)
#    GPIO.output(GPIO_TRIGGER4, GPIO.HIGH)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER1, GPIO.LOW)
    GPIO.output(GPIO_TRIGGER2, GPIO.LOW)
#    GPIO.output(GPIO_TRIGGER3, GPIO.LOW)
#    GPIO.output(GPIO_TRIGGER4, GPIO.LOW)
 
    StartTime = time.time()+.00046
    StopTime1 = 0
    StopTime2 = 0
    StopTime3 = 0
    StopTime4 = 0
    StopTime5 = 0
    StopTime6 = 0
#    StopTime7 = 0
#    StopTime8 = 0
#    StopTime9 = 0
#    StopTime10 = 0
#    StopTime11 = 0
#    StopTime12 = 0
 
 
    LoopTime = time.time()
    i=0
    while i<1:
 
    # save time of arrival
        if GPIO.event_detected(GPIO_ECHO1):
            StopTime1 = time.time()
            #print("fall detected")
            i1=1
            
        if GPIO.event_detected(GPIO_ECHO2):
            StopTime2 = time.time()
            #print("fall detected")
            i2=1
            
        if GPIO.event_detected(GPIO_ECHO3):
            StopTime3 = time.time()
            #print("fall detected")
            i3=1
            
        if GPIO.event_detected(GPIO_ECHO4):
            StopTime4 = time.time()
            #print("fall detected")
            i4=1
            
        if GPIO.event_detected(GPIO_ECHO5):
            StopTime5 = time.time()
            #print("fall detected")
            i5=1
            
        if GPIO.event_detected(GPIO_ECHO6):
            StopTime6 = time.time()
            #print("fall detected")
            i6=1

#        if GPIO.event_detected(GPIO_ECHO7):
#            StopTime7 = time.time()
#            #print("fall detected")
#            i7=1
#            
#        if GPIO.event_detected(GPIO_ECHO8):
#            StopTime8 = time.time()
#            #print("fall detected")
#            i8=1
#            
#        if GPIO.event_detected(GPIO_ECHO9):
#            StopTime9 = time.time()
#            #print("fall detected")
#            i9=1
#            
#        if GPIO.event_detected(GPIO_ECHO10):
#            StopTime10 = time.time()
#            #print("fall detected")
#            i10=1
#            
#        if GPIO.event_detected(GPIO_ECHO11):
#            StopTime11 = time.time()
#            #print("fall detected")
#            i11=1
#            
#        if GPIO.event_detected(GPIO_ECHO12):
#            StopTime12 = time.time()
#            #print("fall detected")
#            i12=1

        if time.time()-LoopTime > TIMEOUT:
            i=1
            print("timeout")
 
        if i1==1 and i2==1 and i3==1 and i4==1 and i5==1 and i6==1:
        #if i1==1 and i2==1 and i3==1 and i4==1 and i5==1 and i6==1 and i7==1 and i8==1 and i9==1 and i10==1 and i11==1 and i12==1:
            i=1
            #print("exit loop successful")
 
    # time difference between start and arrival
    #TimeElapsed1 = StopTime1 - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    #distance = (TimeElapsed1 * 34300) / 2

    Distance1 = (((StopTime1 - StartTime) * 34300) / 2)
    Distance2 = (((StopTime2 - StartTime) * 34300) / 2)
    Distance3 = (((StopTime3 - StartTime) * 34300) / 2)
    Distance4 = (((StopTime4 - StartTime) * 34300) / 2)
    Distance5 = (((StopTime5 - StartTime) * 34300) / 2)
    Distance6 = (((StopTime6 - StartTime) * 34300) / 2)

    if Distance1 > 0:
        DistanceArray.append(Distance1)
    else:
        DistanceArray.append(6969)
        
    if Distance2 > 0:
        DistanceArray.append(Distance2)
    else:
        DistanceArray.append(6969)
        
    if Distance3 > 0:
        DistanceArray.append(Distance3)
    else:
        DistanceArray.append(6969)
        
    if Distance4 > 0:
        DistanceArray.append(Distance4)
    else:
        DistanceArray.append(6969)
        
    if Distance5 > 0:
        DistanceArray.append(Distance5)
    else:
        DistanceArray.append(6969)
        
    if Distance6 > 0:
        DistanceArray.append(Distance6)
    else:
        DistanceArray.append(6969)
        

    print ("Measured Distance1 = %.1f cm" % (((StopTime1 - StartTime) * 34300) / 2))
    print ("Measured Distance2 = %.1f cm" % (((StopTime2 - StartTime) * 34300) / 2))
    print ("Measured Distance3 = %.1f cm" % (((StopTime3 - StartTime) * 34300) / 2))
    print ("Measured Distance4 = %.1f cm" % (((StopTime4 - StartTime) * 34300) / 2))
    print ("Measured Distance5 = %.1f cm" % (((StopTime5 - StartTime) * 34300) / 2))
    print ("Measured Distance6 = %.1f cm" % (((StopTime6 - StartTime) * 34300) / 2))
#    print ("Measured Distance7 = %.1f cm" % (((StopTime1 - StartTime) * 34300) / 2))
#    print ("Measured Distance8 = %.1f cm" % (((StopTime2 - StartTime) * 34300) / 2))
#    print ("Measured Distance9 = %.1f cm" % (((StopTime3 - StartTime) * 34300) / 2))
#    print ("Measured Distance10 = %.1f cm" % (((StopTime4 - StartTime) * 34300) / 2))
#    print ("Measured Distance11 = %.1f cm" % (((StopTime5 - StartTime) * 34300) / 2))
#    print ("Measured Distance12 = %.1f cm" % (((StopTime6 - StartTime) * 34300) / 2))


    return DistanceArray


if __name__ == '__main__':
    try:
        
        if Direction == "Reverse":
            GPIO.output(DIR1,True)
            GPIO.output(DIR2,False)

            print("Starting Motor...")


            DistanceArray = distance()
            
            a.value = PWR
            b.value = PWR
            
            timeoutdrive = 0
            
            while min(DistanceArray) > DistanceOut:
                
                DistanceArray = distance()
                
                time.sleep(.1)
 
                timeoutdrive = timeoutdrive + .1
 
        if Direction == "Forward":
            GPIO.output(DIR1,False)
            GPIO.output(DIR2,True)

            print("Starting Motor...")

            DistanceArray = distance()

            a.value = PWR
            b.value = PWR
            

            timeoutdrive = 0
            
            while min(DistanceArray) > DistanceOut:
                
                DistanceArray = distance()
                
                time.sleep(.1)
 
                timeoutdrive = timeoutdrive + .1
 
 
        if Direction == "Left":
            GPIO.output(DIR1,False)
            GPIO.output(DIR2,False)

            print("Starting Motor...")

            DistanceArray = distance()

            a.value = PWR
            b.value = PWR
        
            timeoutdrive = 0
            
            while min(DistanceArray) > DistanceOut:
                
                DistanceArray = distance()
                
                time.sleep(.15)
 
                timeoutdrive = timeoutdrive + .1
 

        if Direction == "Right":
            GPIO.output(DIR1,True)
            GPIO.output(DIR2,True)

            print("Starting Motor...")

            DistanceArray = distance()

            a.value = PWR
            b.value = PWR
            
            timeoutdrive = 0
            
            while min(DistanceArray) > DistanceOut:
                
                DistanceArray = distance()
                
                time.sleep(.1)
 
                timeoutdrive = timeoutdrive + .1
                   
                
        a.value = 0.0
        b.value = 0.0
        
        a.close
        b.close
        
        GPIO.cleanup()
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Movement stopped by User")
        
        a.value = 0.0
        b.value = 0.0
        
        a.close
        b.close
        
        GPIO.cleanup()

