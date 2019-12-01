import time

from opcua import Client
url = "opc.tcp://192.168.1.105:48480"

client = Client(url)
client.connect()
print("client connected")
while True:
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Press = client.get_node("ns=2;i=3")
    Pressure = Press.get_value()
    print(Pressure)

    TIME = client.get_node("ns=2;i=4")
    TIME_Value = TIME.get_value()
    print(TIME_Value)

    time.sleep(1)
