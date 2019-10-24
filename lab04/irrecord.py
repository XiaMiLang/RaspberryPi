import RPi.GPIO as GPIO
import time
import sys
import json

def initEnv(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(pin, GPIO.IN)

def endEnv():
    GPIO.cleanup()

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
def main():
    PIN = int(sys.argv[1])
    OUT_FILE = sys.argv[2]
    initEnv(PIN)
    keys = {}
    while True:
        key_name = input('Please input key name(exit for terminating this program):')
        if key_name == 'exit':
            break

        keys[key_name] = getSignal(PIN)

        for pulse in keys[key_name]:
            if pulse > 30 and pulse < 50: # frame space/stop(30~50ms) 
                print('>', end='')
                break
            elif pulse > 2 and pulse < 10: # leading pulse burst (4.5ms) 
                print('<', end='')
            elif pulse > 1.0 and pulse < 2: # 1 (1.7ms)
                print('-', end='')
            elif pulse > 0.1 and pulse < 1: # 0 (0.56ms)
                print('|', end='')
            else:
                print('.', end='') # other
        print('')

    endEnv()

    src = open(OUT_FILE, 'w')
    src.write(json.dumps(keys))
    src.close()

if __name__ == "__main__":
    main()
