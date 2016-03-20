import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
gpio.setup(27, gpio.OUT)
val = 1
inc = 0.1
try :
  while True :
    gpio.output(27, False)
    time.sleep(val / 1000.0)
    gpio.output(27, True)
    time.sleep((20 - val) / 1000.0)
    val += inc
    time.sleep(0.05)
    if val > 2 or val < 0.6 :
      inc *= -1
except KeyboardInterrupt :
  gpio.cleanup()