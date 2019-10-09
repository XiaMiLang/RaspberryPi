# read pin and tunes from command line
# python lab2_buzzer_1.py [pin] [freq:freq:freq]
# python lab2_buzzer_1.py 12 523:589:659:698:784:880:988:1047

import time
import RPi.GPIO as GPIO
import sys

def play_tunes(p, f, delay):
    p.ChangeFrequency(f)
    time.sleep(delay)

def getFreqs(freq_num):
    cand_freqs = [
        261, # Do
        277, # Do#
        293, # Re#
        311, # Re#
        329, # Mi
        349, # Fa
        369, # Fa#
        392, # Sol
        415, # Sol#
        440, # La
        466, # La#
        493, # Si
        523  # Do
    ]



GPIO.setmode(GPIO.BOARD)	

pin = int(sys.argv[1])		#read pin and tune from command line
GPIO.setup(pin,GPIO.OUT)

p = GPIO.PWM(pin, 50)		#p = GPIO.PWM(channel, frequency)
p.start(50)    #0 ~ 100
delay = 0.2

freq = []
freqs = getFreqs(Freq_num)

for fr in freqs:
    freq.append(int(fr))

for f in freq:
    play_tunes(p, f, delay)

p.stop()
GPIO.cleanup()
