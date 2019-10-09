# read pin and bee.json from command line.
# python lab2_buzzer_2.py [pin] [freq_sequence.json]
# python lab2_buzzer_2.py 12 bee.json

import time
import RPi.GPIO as GPIO
import sys

def play_tunes(p, f, delay):
    p.ChangeFrequency(f)
    time.sleep(delay)

GPIO.setmode(GPIO.BOARD)	

pin = int(sys.argv[1])		#read pin and tune from command line
GPIO.setup(pin,GPIO.OUT)

p = GPIO.PWM(pin, 50)		#p = GPIO.PWM(channel, frequency)
p.start(50)    #0 ~ 100
delay = 0.2

tunes = sys.argv[2].split(":")
freq = []
for t in tunes:
    freq.append(int(t))

for f in freq:
    play_tunes(p, f, delay)

p.stop()
GPIO.cleanup()