import sys
import Adafruit_DHT as DHT
import time
#import os    # myCmd = 'ls > out.txt'  #os.system(myCmd)

def main():
    BCM_PIN = int(sys.argv[1])
    condition = sys.argv[2]
    print(condition)
#    TOTAL_TIME = float(sys.argv[2])    #totay time measuring
    monit_time = int(sys.argv[3])      #delay interval
    iter_num = int(monit_time)
    print("BCM_PIN", BCM_PIN)
#    print("TOTAL_TIME", TOTAL_TIME)
    print("monit_time", monit_time)
#    print("iter_num", iter_num)
#    while True:
    for i in range(monit_time):
        h, t = DHT.read_retry(11, BCM_PIN)    #h, t=DHT.read_retry(DHT_version, BCM_PIN)
        condition = condition.replace("t", str(t)).replace("h", str(h))

        if (eval(condition)):
            print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
#        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(t, h))
        time.sleep(1)
    
if __name__=="__main__":
    main()