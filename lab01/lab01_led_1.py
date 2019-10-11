import sys
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
PINS = sys.argv[1:]
allpin = []
allstate = []
for i in range(len(PINS)):
    allpin.append(PINS[i].split(":")[0])
    allstate.append(PINS[i].split(":")[1])
for i in range(len(allpin)):
    print(i)
    GPIO.setup(int(allpin[i]), GPIO.OUT)
    if allstate[i] == "True":
        GPIO.output(int(allpin[i]), True)
    else:
        GPIO.output(int(allpin[i]), False)