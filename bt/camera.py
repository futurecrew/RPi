import bluetooth 
import RPi.GPIO as GPIO
import time

def rotate(ps, direction):  
    print 'rotate direction : %s' % direction
    if direction == 'UP':
        ps[0].ChangeDutyCycle(4.5)
    elif direction == 'DOWN':
        ps[0].ChangeDutyCycle(10)
    elif direction == 'LEFT':
        ps[1].ChangeDutyCycle(4.5)
    elif direction == 'RIGHT':
        ps[1].ChangeDutyCycle(20)
    elif direction == 'STOP':
        ps[0].ChangeDutyCycle(100)
        ps[1].ChangeDutyCycle(100)

hostMACAddress = 'B8:27:EB:65:60:44' # The MAC address of a Bluetooth adapter on the server. The server might have multiple Bluetooth adapters. 

print 'starting BT server : %s' % hostMACAddress

CHANNEL = [18, 23]
ps = []

GPIO.setmode(GPIO.BCM)

for i, c in enumerate(CHANNEL):
    GPIO.setup(c,GPIO.OUT)
    ps.append(GPIO.PWM(c,50))  
    ps[i].start(100)

port = 3 
backlog = 1
size = 1024
s = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
s.bind((hostMACAddress, port))
s.listen(backlog)
try:
    client, clientInfo = s.accept()
    while 1:
        data = client.recv(size)
        if data:
            print(data)
            client.send(data) # Echo back to client
            rotate(ps, data)
except:	
    print("Closing socket")
    client.close()
    s.close()




