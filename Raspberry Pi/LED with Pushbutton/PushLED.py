import RPi.GPIO as GPIO          # import Raspberry Pi GPIO Library 
import time                      # import Time Module

GPIO.setmode(GPIO.BCM)           #set pin mode to BCM

GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # set GPIO Pin 23 as an input connected to Push Button
GPIO.setup(24, GPIO.OUT)                          # set GPIO Pin 24 as an output connected to LED

try:
    while True:                                   # Run Forever
         button_state = GPIO.input(23)            # read button state either 1 or 0
         if button_state == False:                # if button state is 0 turn LED On
             GPIO.output(24, True)
             print('Button Pressed...')
             time.sleep(0.2)
         else:                                   # else button state is 1 so turn LED Off
             GPIO.output(24, False)
except:
    GPIO.cleanup()                               # clean up all the ports used
