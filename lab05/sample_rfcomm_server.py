#!/usr/bin/env python3
"""
This program is a simple rfcomm server based on bluetooth connection,
please check your BlueTooth connection before you start your testing.
@author: FATESAIKOU
@argv[1]: server name
"""
import signal
import sys
from bluetooth import *
import time
import RPi.GPIO as GPIO

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

# Service ending handler
def end_service(signal, frame):
    global service_on
    print('[INFO] Ctrl+C captured, shutdown service.')
    service_on = False
    sys.exit(0)

# Client request handler
def handler(sock, info):
    global service_on
    print("[INFO] Accepted connection from", info)
    try:
        while service_on:
            data = str(sock.recv(1024), encoding = "utf-8")
            if len(data) == 0:
                break
            request = data.split()
            print(request)
            print("[RECV] %s" % data)
            if request[0] == "set":
                print(request[1]+":"+request[2]+":"+request[3])
                # duties = [int(request[1]), int(request[2]), int(request[3])]
                # print(duties)
                values = [int(request[1]), int(request[2]), int(request[3])]
                setColor(int(request[1]), int(request[2]), int(request[3]))
                time.sleep(0.5)
                sock.send('led changed')
            elif request[0]=="get" and request[1]=="values":
                msg = "[send] >> " + str(values[1]) + ":" + str(values[2]) + ":"+ str(values[3])
                sock.send(msg)
                print("[send]" + msg)
            else :
                sock.send('invalid input')
            # sock.send('foo ' + data.decode('ascii'))
            # print("[SEND] >> foo " + data.decode('ascii'))
    except IOError:
        pass
# Env init
UUID = '94f39d29-7d6d-437d-973b-fba39e49d4ee'
#UUID = '00001112-0000-1000-8000-00805f9b34fb'
SERVER_NAME = sys.argv[1]
service_on = True

# Add terminator
signal.signal(signal.SIGINT, end_service)

# Create service socket
server_sock = BluetoothSocket(RFCOMM)
server_sock.bind( ('', PORT_ANY) )
server_sock.listen(1)
port = server_sock.getsockname()[1]

# Advertise your service
advertise_service(
    server_sock,
    SERVER_NAME,
    service_id=UUID,
    service_classes = [UUID, SERIAL_PORT_CLASS],
    profiles=[SERIAL_PORT_PROFILE]
)

# Start service
print('[INFO] Service listening at port %d' % port)

while service_on:
    c_sock, c_info = server_sock.accept()
    print('[INFO] Start of connection')
    handler(c_sock, c_info)
    print('[INFO] End of connection')
    c_sock.close()
    
server_sock.close()
print('[INFO] Service shutdown')