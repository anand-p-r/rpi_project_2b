import subprocess
import os
import datetime
import time
import RPi.GPIO as GPIO

default_webcam_usb_loc = "/dev/video0"
default_image_dir      = "./pics/"
output_file_prefix     = "image_"
output_file_suffix     = ".jpg"
resolution             = "640x480" 
cmd_to_pic = "fswebcam -d " + default_webcam_usb_loc + " -r " + resolution + " "

if (os.path.exists(default_webcam_usb_loc)):
    print ("USB Webcam found!")
else:
    print ("Webcam not connected")

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
        count += 1
        time_str = str(datetime.datetime.now())
        time_str = time_str.replace("-", "_").replace(":","_").replace(".","_").replace(" ","_")

        for i in range (3):
            output_file_name = str(i).join([default_image_dir,
                                            output_file_prefix,
                                            time_str,
                                            output_file_suffix])
            ## Take the pic
            cmd = cmd_to_pic + output_file_name
            if (os.system(cmd) == 0):
                print("Image captured - ", output_file_name)
            
            time.sleep(2)
        print ("Re-settling sensor......")
        time.sleep(20)
        print ("Detecting motion....")
        
    time.sleep(0.1)
