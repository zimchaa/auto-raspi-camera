#!/usr/bin/env python

import pibrella
from picamera import PiCamera
import time

processing = False

def take_picture():
    global processing
       
    if processing == False:
        try: 
            camera = PiCamera()
            camera.resolution = (1024, 1024)
            time_stamp = time.strftime("%Y-%m-%d-%H-%M-%S") 
            processing = True
            print("Start processing")
            camera.start_preview()
            camera.rotation = 270
            pibrella.light.green.fade(0,100,1)
            time.sleep(1)
            pibrella.light.amber.fade(0,100,1)
            time.sleep(1)
            pibrella.light.red.fade(0,100,1)
            time.sleep(1)
            camera.capture('simple_shot_' + time_stamp + '.jpg')
            processing = False
            print("Processing complete")
            pibrella.light.off()
        finally:
            camera.close()
            print("Waiting for new press")
            pibrella.output.h.pulse(1,1,0,0)
    else:
        print("halted processing - currently taking a picture...")
    
def handle_button(button):
    global processing
    if processing == False:
        pibrella.output.h.off()
        take_picture()
        print("Taking a picture!")
    else:
        print("Currently processing... try again later!")

# kick off the picture taking
pibrella.button.released(handle_button)

# indicate that we're ready to start by pulsing the output light
pibrella.output.h.pulse(1,1,0,0)

pibrella.pause()
