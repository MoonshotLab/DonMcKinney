import RPi.GPIO as GPIO
import time

PINS = {
    'BUTTON'    : 18,
    'L_EYE'     : 23,
    'R_EYE'     : 24
    }

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PINS['BUTTON'], GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PINS['L_EYE'], GPIO.OUT)
GPIO.setup(PINS['R_EYE'], GPIO.OUT)

def listen(callback):

    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            GPIO.output(23, True)
            GPIO.output(24, True)
            callback()
            GPIO.output(23, False)
            GPIO.output(24, False)
