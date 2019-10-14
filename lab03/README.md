![](https://github.com/XiaMiLang/RespberryPi/blob/master/lab03/lab03_DHT.JPG)

reference: http://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/

To install the Adafruit DHT11 library:

1. Enter this at the command prompt to download the library:

   ​	git clone https://github.com/adafruit/Adafruit_Python_DHT.git

2. Change directories with:

   ​	cd Adafruit_Python_DHT
   
3. sudo apt-get update

4. Now enter this:

   ​	sudo apt-get install build-essential python-dev

5. Then install the library with:

   ​	sudo python3 setup.py install
   
   ------
   
   

Condition: lab03_DHT.py [bcm_pin] [condition] [monit_time]

* use Adafruit_DHT module
* read bcm_pin from command line as the 1st input argument
* when [condition] triggered, execute something
  * trigger when t >1
  * trigger when t>11 and h>0.43
  * trigger when t*100>h