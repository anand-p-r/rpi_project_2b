import time
import RPi.GPIO as GPIO

sel_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sel_pin, GPIO.IN)

print ("Sensor settling......")
time.sleep(60)

print ("Detecting motion....")

count = 0
while (1):
    if GPIO.input(sel_pin):
        print("Something has moved....", count)
        time.sleep(10)
        count += 1
    time.sleep(0.1)


    
