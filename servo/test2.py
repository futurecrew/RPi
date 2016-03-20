import RPi.GPIO as GPIO
import time

#CHANNEL = 18
CHANNEL = 23

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.setup(CHANNEL,GPIO.OUT)
p = GPIO.PWM(CHANNEL,50)
p.start(7.5)

#dsfjsf

try:               
    while True:    
        print('4.5')
        p.ChangeDutyCycle(4.5)
        time.sleep(1)       
        print('15')
        p.ChangeDutyCycle(15) 
        time.sleep(1)         
        print('7.5')
        p.ChangeDutyCycle(100) 
        time.sleep(1)        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()