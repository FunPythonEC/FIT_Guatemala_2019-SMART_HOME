from machine import Pin
import machine, neopixel
from urandom import getrandbits
import network
import time
from umqtt.robust import MQTTClient
import os
import sys

num_leds=10
pin_salida=15
np = neopixel.NeoPixel(machine.Pin(pin_salida), num_leds)

def rojo():
    for led in range(num_leds):
        np[led]=(255,0,0)
    np.write()        

def verde():
    for led in range(num_leds):
        np[led]=(0,255,0)
    np.write()
      
def azul():
    for led in range(num_leds):
        np[led]=(0,0,255)
    np.write()
     
def amarillo():
    for led in range(num_leds):
        np[led]=(255,255,0)
    np.write()
    
def magenta():
    for led in range(num_leds):
        np[led]=(255,0,255)
    np.write()
    
def cyan():
    for led in range(num_leds):
        np[led]=(0,255,255)
    np.write() 

def encender():
    for led in range(num_leds):
        np[led]=(255,255,255)
    np.write()
    
def apagar():
    for led in range(num_leds):
        np[led]=(0,0,0)    
    np.write()
 


#RECIBIR EL DATO DEL SERVIDOR PARA ENCENDER LOS 
#########################
# la siguiente función es la devolución de llamada que es
# llamada cuando se reciben los datos suscritos
def cb(topic, msg):
    print((msg))    

#########################

    #while True:
        
    if msg == b"rojo":
        rojo()
        time.sleep_ms(5)
        print("rojo")
            
    if msg == b"verde":
        verde()
        time.sleep_ms(5)
        print("verde")
    
    if msg == b"azul":
        azul()
        time.sleep_ms(5)
        print("azul")

    if msg == b"amarillo":
        amarillo()
        time.sleep_ms(5)
        print("amarillo")
    
    if msg == b"magenta":
        magenta()
        time.sleep_ms(5)
        print("magenta")
    
    if msg == b"cyan":
        cyan()
        time.sleep_ms(5)
        print("cyan")

    if msg == b"ON":
        encender()
        time.sleep_ms(5)
        print("encender")

    if msg == b"OFF":
        apagar()
        time.sleep_ms(5)
        print("apagar")        


#CONEXION A LA RED WIFI
######################### ('J-PC', 'jp12345678')
# Informacion de la red WiFi
WIFI_SSID = 'IoT 2.4GHz'
WIFI_PASSWORD = ''

# apagar el punto de acceso WiFi
ap_if = network.WLAN(network.AP_IF)
ap_if.active(False)

# conecta el dispositivo a la red WiFi
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(WIFI_SSID, WIFI_PASSWORD)

# esperar hasta que el dispositivo esté conectado a la red WiFi
MAX_ATTEMPTS = 20
attempt_count = 0

while not wifi.isconnected() and attempt_count < MAX_ATTEMPTS:
    attempt_count += 1
    time.sleep(1)
    print('conectando a la red WiFi...')
    
if attempt_count == MAX_ATTEMPTS:
    print('no se pudo conectar a la red WiFi')
    sys.exit()
    
print('conectado a la red WiFi')
print ("Configuracion de red: ", wifi.ifconfig())

#CONEXION AL SERVIDOR ADAFRUIT-IO
#########################       
# crear un ID de cliente MQTT
mqtt_client_id = bytes('esp_32', 'utf-8')


# conectar con el corredor de Adafruit IO MQTT usando TCP no seguro (puerto 1883)
# 
# Para usar una conexión segura (encriptada) con TLS:
#    establece el parámetro de inicializador MQTTClient a "ssl = True"
#    Advertencia: una conexión segura usa aproximadamente 9k bytes de la pila
#          (aproximadamente 1/4 de la pila de micropython en la plataforma ESP8266)
ADAFRUIT_IO_URL = b'io.adafruit.com' 
ADAFRUIT_USERNAME = b'jhon_p16'
ADAFRUIT_IO_KEY = b'50f55bdf3ee849bbad1c564d1136da97'
ADAFRUIT_IO_FEEDNAME = b'led_strip'

client = MQTTClient(client_id=mqtt_client_id, 
                    server=ADAFRUIT_IO_URL, 
                    user=ADAFRUIT_USERNAME, 
                    password=ADAFRUIT_IO_KEY,
                    ssl=False)
print('conectado al servidor MQTT')

try:      
    client.connect()
except Exception as e:
    print('no se pudo conectar al servidor MQTT {}{}'.format(type(e).__name__, e))
    sys.exit()


mqtt_feedname = bytes('jhon_p16/feeds/led-strip', 'utf-8')
client.set_callback(cb)                    
client.subscribe(mqtt_feedname)  

# Seguir dos líneas es una implementación específica de Adafruit de la función Publicar "retener"
# que permite que una Suscripción reciba inmediatamente el último valor publicado para un feed,
# incluso si ese valor se publicó hace dos horas.
# Descrito en el blog de Adafruit IO, 22 de abril de 2018: https://io.adafruit.com/blog/  
mqtt_feedname_get = bytes('{:s}/get'.format(mqtt_feedname), 'utf-8')    
client.publish(mqtt_feedname_get, '\0')
     

# espere hasta que se hayan publicado los datos en la fuente IO de Adafruit
while True:
    try:
        client.wait_msg()
        
    except KeyboardInterrupt:
        print('Ctrl-C pressed...exiting')
        client.disconnect()
        sys.exit()



