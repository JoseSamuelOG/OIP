import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    if GPIO.input(25):
        GPIO.output(26, 1)
    else:
        GPIO.output(26, 1)
        time.sleep(0.1)
        GPIO.output(26, 0)
        time.sleep(0.1)
