import RPi.GPIO as GPIO
import time
import random

CHANNEL = [18, 23]
ps = []

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)

for i, c in enumerate(CHANNEL):
    GPIO.setup(c,GPIO.OUT)
    ps.append(GPIO.PWM(c,50))  
    ps[i].start(7.5)
  
try:               
    while True:    
        i = random.randint(0, 1)
        ps[i].ChangeDutyCycle(4.5)
        time.sleep(3)       
        i = random.randint(0, 1)
        ps[i].ChangeDutyCycle(10.5)
        time.sleep(3)        
        i = random.randint(0, 1)
        ps[i].ChangeDutyCycle(7.5) 
        time.sleep(3)        
except KeyboardInterrupt:
    for i, c in enumerate(CHANNEL):
      ps[i].stop()
    GPIO.cleanup()
