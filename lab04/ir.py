#!/usr/bin/env python3
"""
This is a program for simple led control on RasberryPi(R)

@author: FATESAIKOU
@argv[1:]: ALL Pins for using
"""

import RPi.GPIO as GPIO
import sys
import random
import time
import signal
import json  

def setupPin(ledPin):
    GPIO.output(ledPin, True)
        

def setoffPin(ledPin):
    GPIO.output(ledPin, False)
        
        
def compairSignal(s1,s2,rang):
	min_len = min(len(s1),len(s2))
	for i in range(min_len):
		print(str(sc1)+"="+str(sc2))
		if sc1!=sc2:
			return False 
		
	return True
	
def decodeSingal(s,signal_map,rang):
	for name in signal_map.keys():
		print(name)
		if compairSignal(s,signal_map[name],rang):
			return name
	return None
	
def getSignal(pin):
	start, stop = 0, 0

	signals = []
	while True:
		while GPIO.input(pin) == 0:
			None

		start = time.time()

		while GPIO.input(pin) == 1:
			stop = time.time()

			duringUp = (stop - start)*1000 # using ms
			if duringUp > 100  and len(signals) > 0:
				return signals[1:]

		signals.append(duringUp)
		
def initEnv(IR_pin,LED_pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setwarnings(False)
	GPIO.setup(LED_pin, GPIO.OUT)

	GPIO.setup(IR_pin, GPIO.IN)

def endEnv():
	GPIO.cleanup()
	
def changecode(s):
	res =''
	if s > 30 and s < 50: # frame space/stop(30~50ms) 
		res ='>'
	elif s > 2 and s < 10: # leading pulse burst (4.5ms) 
		res ='<'
	elif s > 1.0 and s < 2: # 1 (1.7ms)
		res ='-'
	elif s > 0.1 and s < 1: # 0 (0.56ms)
		res ='|'
	else:
		res ='.'
		
	return res
	
def main():
	IR_PIN = int(sys.argv[1])
	LED_PIN = int(sys.argv[2])
	FILEPATH = sys.argv[3]
	with open(FILEPATH,'r') as f:
		key_map = json.load(f)
	initEnv(IR_PIN,LED_PIN)
	
	while True:
		print("please press key")
		
		s = getSignal(IR_PIN)
		usekey = (decodeSingal(s,key_map,0.05))
		print("Your press %s"%usekey)
		if usekey == "1" :
			setupPin(LED_PIN)
		elif usekey == "0":
			setoffPin(LED_PIN)
	endEnv()


if __name__ == '__main__':
	main()
