
# coding: utf-8

# In[68]:

import subprocess
import os
import time


# In[69]:

default_webcam_usb_loc = "/dev/video0"
default_image_dir      = "/home/pi/project_2b_pics/"
output_file_prefix     = "image_"
output_file_suffix     = ".jpg"
resolution             = "640x480" 
cmd_to_pic = "fswebcam -d " + default_webcam_usb_loc + " -r " + resolution + " "


# In[70]:

if (os.path.exists(default_webcam_usb_loc)):
    print ("USB Webcam found!")
else:
    print ("Webcam not connected")


# In[71]:

output_file_name = "".join([default_image_dir,
                            output_file_prefix,
                            str(time.time()).replace(".", "_"),
                            output_file_suffix])
output_file_name


# In[72]:

## Take the pic
cmd = cmd_to_pic + output_file_name
if (os.system(cmd) == 0):
    print("Success!")


# In[ ]:



