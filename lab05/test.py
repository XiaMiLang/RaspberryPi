import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
RED_LED_PIN = 36
GREEN_LED_PIN = 38
BLUE_LED_PIN = 40
PWM_FREQ = 200

GPIO.setup(RED_LED_PIN, GPIO.OUT)
GPIO.setup(GREEN_LED_PIN, GPIO.OUT)
GPIO.setup(BLUE_LED_PIN, GPIO.OUT)

red_pwm = GPIO.PWM(RED_LED_PIN, PWM_FREQ)
red_pwm.start(0)
blue_pwm = GPIO.PWM(BLUE_LED_PIN, PWM_FREQ)
blue_pwm.start(0)
green_pwm = GPIO.PWM(GREEN_LED_PIN, PWM_FREQ)
green_pwm.start(0)
 
def setColor(r=0, g=0, b=0):
    red_pwm.ChangeDutyCycle(r)
    blue_pwm.ChangeDutyCycle(g)
    green_pwm.ChangeDutyCycle(b)

try:
    while True:
        setColor(100,0,0)

finally:
    red_pwm.stop()
    green_pwm.stop()
    blue_pwm.stop()
    GPIO.cleanup()