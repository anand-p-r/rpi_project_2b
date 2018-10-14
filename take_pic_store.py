import subprocess
import os
import time
import RPi.GPIO as GPIO

default_webcam_usb_loc = "/dev/video0"
default_image_dir      = "/media/pi/RPI/rpi_project_2b/pics/"
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

        output_file_name = "".join([default_image_dir,
                                    output_file_prefix,
                                    str(time.time()).replace(".", "_"),
                                    output_file_suffix])
        output_file_name

        ## Take the pic
        cmd = cmd_to_pic + output_file_name
        if (os.system(cmd) == 0):
            print("Success!")

        time.sleep(20)

    time.sleep(0.1)
