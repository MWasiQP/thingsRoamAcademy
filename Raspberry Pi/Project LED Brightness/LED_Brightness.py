import RPi.GPIO as GPIO     # import Raspberry Pi GPIO Library
from time import sleep      # import sleep method from the time module

ledpin = 12				          # assign Pin 12 connected to LED to a variable 
GPIO.setwarnings(False)		  # disable warnings
GPIO.setmode(GPIO.BOARD)		# set physical pin numbering system
GPIO.setup(ledpin,GPIO.OUT) # set pin 12 as an output

pi_pwm = GPIO.PWM(ledpin,1000)	# create PWM instance with frequency
pi_pwm.start(0)				          # start PWM of required Duty Cycle 

while True:                          # Infinite Loop
    for duty in range(0,101,1):      # increase duty value from 0-100 with 1 step
        pi_pwm.ChangeDutyCycle(duty) 
        sleep(0.01)                  # 10 miliseconds delay after every new value
    sleep(0.5)                       # half second delay after the completion of loop  
    
    for duty in range(100,-1,-1):    # decrease duty value from 100 to 0 with 1 step
        pi_pwm.ChangeDutyCycle(duty)
        sleep(0.01)                  # 10 miliseconds delay after every new value
    sleep(0.5)                       # half second delay after the completion of loop
