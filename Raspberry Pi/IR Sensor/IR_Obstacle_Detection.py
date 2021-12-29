import RPi.GPIO as IO    # import Raspberry Pi GPIO Library
import time              # import time module

IO.setwarnings(False)    # disable warning
IO.setmode(IO.BCM)       # set pin mode to BCM 

IO.setup(2,IO.OUT)       # set GPIO Pin 2 as output connected to Red LED
IO.setup(3,IO.OUT)       # set GPIO Pin 3 as output connected to Green LED
IO.setup(14,IO.IN)       # set GPIO Pin 14 as input connected to IR Sensor

while 1:                      # Main Loop
    if(IO.input(14)==True):   # if IR Sensor gives 1
        IO.output(2,True)     # Red LED ON
        IO.output(3,False)    # Green LED OFF
    
    if(IO.input(14)==False):  # if IR Sensor gives 0
        IO.output(3,True)     # Green LED ON
        IO.output(2,False)    # Red LED OFF
