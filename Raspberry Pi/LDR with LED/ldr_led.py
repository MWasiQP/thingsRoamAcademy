import RPi.GPIO as GPIO          # import Raspberry Pi GPIO Library 
import time                      # import Time Module

GPIO.setmode(GPIO.BOARD)         # set physical pin mode

delaytime = .1                   # set 0.1 second deley
value = 0                        # this variable will be used to store the ldr value
ldr = 7                          # ldr is connected to physical pin number 7
led = 11                         # led is connected to physical pin number 11

GPIO.setup(led, GPIO.OUT)        # set pin 11 as output
GPIO.output(led, False)          # turn led off at start

def rc_time (ldr):               # define a function for ldr
    
    count = 0 

    GPIO.setup(ldr, GPIO.OUT)    # clear the ldr pin
    GPIO.output(ldr, False)
    time.sleep(delaytime)

    GPIO.setup(ldr, GPIO.IN)         # change the pin back to input

    while (GPIO.input(ldr) == 0):    # count until the pin goes high 
        count += 1

    return count                     # return the value of count


try:
    while True:                           # Main loop of the program
        print("Ldr Value:")
        value = rc_time(ldr)              # call LDR fuction that is defined above     
        print(value)
        if ( value <= 10000 ):
                print("Lights are ON")
                GPIO.output(led, True)
        if (value > 10000):
                print("Lights are OFF")
                GPIO.output(led, False)
except KeyboardInterrupt:
    pass
  
finally:
    GPIO.cleanup()
