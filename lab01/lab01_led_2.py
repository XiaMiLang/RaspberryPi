import sys
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
PINS = sys.argv[1:]
allpin = []
allvalue = []    # dutycycle from 0~100
allfreq = []     #any positive int
for i in range(len(PINS)):
    allpin.append(PINS[i].split(":")[0])
    allvalue.append(PINS[i].split(":")[1])
    allfreq.append(PINS[i].split(":")[2])
    
for i in range(len(allpin)):
    GPIO.setup(int(allpin[i]), GPIO.OUT)
    allpin[i] = GPIO.PWM(int(allpin[i]), int(allfreq[i]))
    allpin[i].start(100)
    allpin[i].ChangeDutyCycle(int(allvalue[i]))

print(allpin)
print(allvalue)
print(allfreq)

GPIO.cleanup()