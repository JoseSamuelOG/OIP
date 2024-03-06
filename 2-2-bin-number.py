import RPi.GPIO as time
import time as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 1, 0, 0, 0, 0, 0, 0]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
voltage = []

time.setmode(time.BCM)
time.setup(dac, time.OUT)

time.output(dac, number)

GPIO.sleep(15)

time.output(dac, 0)
time.cleanup()