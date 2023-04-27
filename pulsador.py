from machine import Pin
import utime

push = Pin(15, Pin.IN, Pin.PULL_DOWN) # pulsador conectado a 3.3v 


while True:
    
    estado = push.value()
    print(estado)
    utime.sleep_ms(50)from machine import Pin
import utime

push = Pin(15, Pin.IN, Pin.PULL_DOWN) # pulsador conectado a 3.3v 


while True:
    
    estado = push.value()
    print(estado)
    utime.sleep_ms(50)
    

    © 2022 GitHub, Inc.

    Terms
    Privacy

    

    © 2022 GitHub, Inc.

    Terms
    Privacy
