import subprocess
import os
import datetime
import time
import RPi.GPIO as GPIO
import os

default_webcam_usb_loc = "/dev/video0"
default_image_dir      = "../pics/"
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

with open("log_file.txt", "w") as fp:

    count = 0
    while (1):
    
        ## Look for GPIO output from the HC-SR501 sensor
        if GPIO.input(sel_pin):
            time_str = str(datetime.datetime.now())

            ## Day folders for pictures
            day_folder = str(datetime.datetime.now().date())
    
            ## If folder does not exist create one
            if not os.path.exists(default_image_dir + day_folder):
                os.mkdir(default_image_dir + day_folder)
            else:
                pass

            print("Something has moved....", count)
            print("Timestamp - ", time_str)
        
            fp.write("Count-" + str(count) + "\n")
            fp.write("Timestamp - " + time_str + "\n")
        
            count += 1
        
            time_str = time_str.replace("-", "_").replace(":","_").replace(".","_").replace(" ","_")

            for i in range (3):
                output_file_name = "".join([default_image_dir,
                                            day_folder, "/",
                                            output_file_prefix,
                                            time_str,
                                            "_", str(i),
                                            output_file_suffix])
            
                ## Take the picture. Take 3 snaps spaced by 2secs.
                cmd = cmd_to_pic + output_file_name
                if (os.system(cmd) == 0):
                    print("Image captured - ", output_file_name)
            
                time.sleep(2)
            print ("Re-settling sensor......")
            time.sleep(20)
            print ("Ready to detect motion....")
        
        time.sleep(0.1)