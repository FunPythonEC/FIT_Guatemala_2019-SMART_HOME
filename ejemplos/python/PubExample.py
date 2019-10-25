
#para mas informacion sobre ubidots y mqtt:
#https://help.ubidots.com/developer-guides/ubidots-mqtt-broker

import network
from umqtt.robust import MQTTClient #no esta incluida en el firmware para el esp32, deben ser agregados los scripts de mqtt
import time

#conexion wifi
sta_if = network.WLAN(network.STA_IF); sta_if.active(True)
sta_if.connect("SSID", "PASS")
time.sleep(5)

#se debe especificar el token de acuerdo a la cuenta de ubidots y el clientid con el que se subscribira el esp
ubidotsToken = "TOKEN"
clientID = "espprueba"
topic=b"/v1.6/devices/espflisol" #el topic define a que device en especifico es que se va a subir datos
								 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
								 #define entre los devices creados al cual se quiere subir el dato

client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

#ejemplo de uso del metodo de publicacion
msg='10|30'
temp, humid = msg.split('|')
msg = b'{"temp":%s, "humid":%s}' % (int(temp), int(humid))
print(msg)
while True:
    client.publish(topic, msg)
    time.sleep(1)
