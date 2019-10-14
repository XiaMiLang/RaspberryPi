import sys
import Adafruit_DHT as DHT
import time
import os    # myCmd = 'ls > out.txt'  #os.system(myCmd)


def main():

    BCM_PIN = int(sys.argv[1])
    TOTAL_TIME = float(sys.argv[2])    #totay time measuring
    DELAY = float(sys.argv[3])      #delay interval
    iter_num = int(TOTAL_TIME / DELAY)
    condition = int(sys.argv[2])
    print("BCM_PIN", BCM_PIN)
    print("TOTAL_TIME", TOTAL_TIME)
    print("DELAY", DELAY)
    print("iter_num", iter_num)
    
    
    
#    while True: 
    for i in range(iter_num):
        h, t = DHT.read_retry(11, BCM_PIN)    #h, t=DHT.read_retry(DHT_version, BCM_PIN)
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
        if (condition == 1) and (t>1):
            print("t>1")
        if (condition == 2) and (t>11) and (h>43):
            print("t>11 & h>0.43")
            
        time.sleep(DELAY)
    
if __name__=="__main__":
    main()