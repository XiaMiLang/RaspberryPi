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

shining = True

def end_handler(signal, frame):
    global shining
    print("end of shining")
    shining = False


def initEnv():
    GPIO.setmode(GPIO.BOARD)


def initPin(pins,f):
    pwms = []
    for index in range(len(pins)):
        GPIO.setup(pins[index], GPIO.OUT)
        t_pwm = GPIO.PWM(pins[index], f[index])
        t_pwm.start(100)
        
        pwms.append(t_pwm)

    return pwms
        

def setPin(pwms, duties):
    for i in range(len(pwms)):
        pwms[i].ChangeDutyCycle(duties[i])


def endShining(pwms):
    for pwm in pwms:
        pwm.stop()


def main():
    
    PINS = sys.argv

    print(len(PINS))
    allpin = []
    allstate =[]
    allfreq=[]
    
    for i in range(int(len(PINS))):
        if i!=0:
            allpin.append(int(str(PINS[i]).split(':')[0]))
            allstate.append(int(str(PINS[i]).split(':')[1]))
            allfreq.append(int(str(PINS[i]).split(':')[2]))

	#value = [int(s) for s in sys.argv[2]]

    print("Init Env")
    print(allstate)
    print(allfreq)
    initEnv()
    
    pwms = initPin(allpin,allfreq)
    print(pwms)
    setPin(pwms,allstate)
    


if __name__ == '__main__':
    main()
