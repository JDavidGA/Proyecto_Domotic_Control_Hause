#------------------------------ [IMPORT]------------------------------------#


import network, time, urequests
from machine import Pin, ADC, PWM
from utelegram import Bot
from dht import DHT11
import utime

TOKEN = '5362701999:AAFqfaSdNKyR9J3Xg6cbFtbyHU7Yb0WEEEo'

#--------------------------- [OBJETOS]---------------------------------------#

bot = Bot(TOKEN)
bombillo  = Pin(6, Pin.OUT)
sensorDHT= DHT11(Pin(15))
ventilador = Pin(4, Pin.OUT)
gas =   ADC(Pin,36)
lluvia = ADC(Pin(34))
magnetico = Pin(5,Pin.OUT)
#Puertas = Pin(18,Pin.OUT)
iluminacion = ADC(Pin,39)
#persiana = Pin(9, Pin.OUT) # UTILIZRA pwm
#bomba_water = Pin(10, Pin.OUT)
#caudalimetro = Pin(11, Pin.OUT)



#----------------------[ CONECTAR WIFI ]---------------------------------------------------------#

def conectaWifi (red, password):
      global miRed
      miRed = network.WLAN(network.STA_IF)     
      if not miRed.isconnected():              #Si no está conectado…
          miRed.active(True)                   #activa la interface
          miRed.connect(red, password)         #Intenta conectar con la red
          print('Conectando a la red', red +"…")
          timeout = time.time ()
          while not miRed.isconnected():           #Mientras no se conecte..
              if (time.ticks_diff (time.time (), timeout) > 10):
                  return False
      return True

    

#------------------------------------[BOT]---------------------------------------------------------------------#

if conectaWifi ("RedMiHugo", "Hupe6493"):

    print ("Conexión exitosa!")
    print('Datos de la red (IP/netmask/gw/DNS):', miRed.ifconfig())
      
    
    
    @bot.add_message_handler('Hola')
    def help(update):
        update.reply('''¡hola querido usuario! espero te encuentres bien,
                     cuentame que quieres hacer, recuerda que para saber la
                     temepratura escribe "calefaccion", para activar el ventilador
                     escribe "ventilacion",para apagar el ventilador escribe "apagar", 
                     para encender una luz escribe "luz",
                     para saber si esta lloviendo "lluvia",
                     para apagar la luz escribe "noche" ,
                     ¿necesitas abrir una puerta? solo escribe "abrir" y en caso de que la 
                     desees cerrar solo escribe "cerrar", 
                     No olvides que estoy para cumplir tus deseos y ordenes B)''')

    @bot.add_message_handler("puerta")
    def estado_puerta(update):
        if magnetico.value():
            update.reply("Puerta abierta")
        else:
            update.reply("Puerta Cerrada")

    @bot.add_message_handler('luz')
    def on(update):
        bombillo.on()
        update.reply("Iluminacion Encendida")

    @bot.add_message_handler('noche')
    def off(update):
        bombillo.off()
        update.reply('Iluminacion Apagada')

    @bot.add_message_handler('calefaccion')
    def sensor_temperatura(update):
        sensorDHT.measure()
        temp = sensorDHT.temperature()
        hum = sensorDHT.humidity()       
        #print("T={:02d}C H={:02d}%".format(temp, hum))
        update.reply('Temp: '+ str(temp) + 'Hum: ' + str(hum))
        
    @bot.add_message_handler('lluvia')
    def sensor_de_lluvia(update):
        
        gas.width(ADC.WIDTH_12BIT)
        gas.atten(ADC.ATTN_11DB)
        
        lectura_lluvia = int(lluvia.read())
        #print(lectura)
        utime.sleep(0.2)
        if lectura_lluvia <= 100:
            print("No hay LLuvia")
        if lectura_lluvia >= 200 and lectura_lluvia <= 2000 :
            print("Hay Lluvia")
        if lectura_lluvia >= 2200:
            print("tormenta")
            
    @bot.add_message_handler('gas')
    def sensor_de_gas(update):
        
        gas.width(ADC.WIDTH_12BIT)
        gas.atten(ADC.ATTN_11DB)
        
        lectura_gas = int(gas.read())
        #print(lectura)
        utime.sleep(0.2)
        if lectura_gas <= 100:
            print("No hay LLuvia")
        if lectura_gas >= 200 and lectura_gas <= 2000 :
            print("Hay Lluvia")
        if lectura_gas >= 2200:
            print("tormenta")
    
    @bot.add_message_handler('luminocidad')
    def sensor_de_luz(update):
        
        iluminacion.width(ADC.WIDTH_12BIT)
        iluminacion.atten(ADC.ATTN_11DB)
        
        lectura_iluminacion = int(gas.read())
        #print(lectura)
        utime.sleep(0.2)
        if lectura_iluminacion <= 100:
            print("hay poca luz")
        if lectura_iluminacion >= 200 and lectura_iluminacion <= 2000 :
            print("esta nublado")
        if lectura_iluminacion >= 2200:
            print("hay es la luz")        
        
        
        

    
            
    
    
    bot.start_loop()
        
        
    
        
        
        
        
        
 
else:
       print ("Imposible conectar")
       miRed.active (False)
       
       
