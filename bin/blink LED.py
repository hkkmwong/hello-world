import RPi.GPIO as GPIO
import time

LED_PIN = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT)

def Blink(speed):
    GPIO.output(LED_PIN, True)
    time.sleep(speed)
    GPIO.output(LED_PIN, False)
    time.sleep(speed)
    GPIO.cleanup()
    
Blink(1)