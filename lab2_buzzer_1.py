import time
import RPi.GPIO as GPIO
import sys
"""
def doReMi():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)
    p = GPIO.PWM(12, 50)
    p.start(50)

    print("Do")
    p.ChangeFrequency(523)
    time.sleep(1)

    print("Re")
    p.ChangeFrequency(587)
    time.sleep(1)
   
    print("Mi")
    p.ChangeFrequency(659)
    time.sleep(1)

    p.stop()
    GPIO.cleanup()

doReMi()
"""


def play_tunes(p, freq, delay):
    p.ChangeFrequency(freq)
    time.sleep(delay)

GPIO.setmode(GPIO.BOARD)

pin = int(sys.argv[1])
GPIO.setup(pin,GPIO.OUT)

p = GPIO.PWM(pin, 50)    #p = GPIO.PWM(channel, frequency)
p.start(50)    #0 ~ 100
delay = 0.2

tunes = sys.argv[2].split(":")
fres = []
for fr in tunes:
    fres.append(int(fr))

for f in fres:
    play_tunes(p, f, delay)

p.stop()
GPIO.cleanup()



