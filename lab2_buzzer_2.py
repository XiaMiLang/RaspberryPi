# read pin and bee.json from command line.
# python lab2_buzzer_2.py [pin] [freq_sequence.json]
# python lab2_buzzer_2.py 12 bee.json
import json
import time
import RPi.GPIO as GPIO
import sys

def play_tunes(p, f, delay):
    p.ChangeFrequency(f)
    time.sleep(delay)

GPIO.setmode(GPIO.BOARD)    

pin = int(sys.argv[1])      #read pin and tune from command line
GPIO.setup(pin, GPIO.OUT)

p = GPIO.PWM(pin, 50)       #p = GPIO.PWM(channel, frequency)
p.start(50)    #0 ~ 100
delay = 0.2


filename = sys.argv[2]

with open(filename, 'r') as f:
    data = json.load(f)

freq = []
delay = []

for d in data:
    freq.append(int(d["freq"]))
    delay.append(float(d["time"]))

for f in range (int(len(freq))):
    if freq[f] > 0:
        play_tunes(p, freq[f], delay[f])

p.stop()
GPIO.cleanup()