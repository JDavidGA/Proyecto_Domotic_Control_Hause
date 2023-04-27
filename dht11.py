from dht import DHT11
from machine import Pin
from utime import sleep

sensorDHT = DHT11(Pin(4))

while True:
    
    sleep(1)
    sensorDHT.measure()
    temp = sensorDHT.temperature()
    hum = sensorDHT.humidity()
    print("T={:02}C H={:02}%".format(temp, hum))