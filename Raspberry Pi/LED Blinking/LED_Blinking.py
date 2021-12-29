import RPi.GPIO as GPIO # Import the GPIO library of Raspberry Pi 
from time import sleep # Import the sleep function from the time module

GPIO.setwarnings(False) # To ignore the warnings
GPIO.setmode(GPIO.BOARD) # GPIO.Board initialize the physical pin numbering 
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set physical pin 8 to be an output pin and set initial value to low (0)

while True: # Run forever
  GPIO.output(8, GPIO.HIGH) # Turn on the led
  sleep(1) # Sleep for 1 second
  GPIO.output(8, GPIO.LOW) # Turn off the led
  sleep(1) # Sleep for 1 second
