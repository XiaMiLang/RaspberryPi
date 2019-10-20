lab05 - 20191028 - RFID

sudo apt-get install python-spidev python3-spidev
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
git checkout 8cce26b9ee6e69eb041e9d5665944b88688fca68
sudo python setup.py install  #sudo python setup.py install  ?
cd ..
git clone https://github.com/mxgxw/MFRC522-python.git
sudo reboot
cd MFRC522-python
python Read.py
