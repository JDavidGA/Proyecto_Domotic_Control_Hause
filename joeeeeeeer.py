from machine import Pin, ADC
import utime

sensor = ADC(Pin(34))
sensor.width(ADC.WIDTH_12BIT)
sensor.atten(ADC.ATTN_11DB)
led = Pin(27, Pin.OUT)

while True:
    
    lectura = int(sensor.read())
    print(lectura)
    utime.sleep(0.2)
    if lectura <= 1500:
        print("el nivel es bajo")
    if lectura >= 2000:
        print("el nivel es alto")
        led.value(0)
        utime.sleep(0.5)
    else:
        led.value(1)
        utime.sleep(1)