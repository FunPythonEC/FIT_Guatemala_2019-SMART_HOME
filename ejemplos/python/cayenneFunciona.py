from umqtt.simple import MQTTClient
from machine import Pin
import network
import time

#wifi setting
SSID="flisol" #inserta el nombre de la red
PASSWORD="flisol2019" #inserta tu clave wifi

SERVER = "mqtt.mydevices.com"
CLIENT_ID = "inserta tu client ID"
username='inserta tu MQTT '
password=''
TOPIC = ("v1/%s/things/%s/data/1" % (username, CLIENT_ID))

def connectWifi(ssid,passwd):
  global wlan
  wlan=network.WLAN(network.STA_IF)
  wlan.active(True)
  wlan.disconnect()
  wlan.connect(ssid,passwd)
  while(wlan.ifconfig()[0]=='0.0.0.0'):
    time.sleep(1)
    
connectWifi(SSID,PASSWORD)
server=SERVER
c = MQTTClient(CLIENT_ID, server,1883,username,password)
c.connect()

def senddata():
  temp=20
  
  c.publish(TOPIC, str(temp))

  time.sleep(1)
  print("temperatura es: ", temp)
  print("dato enviado")
  
while True:
    try:
        senddata()
    except OSError:
        pass




