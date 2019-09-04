#librerias necesarias
import network
from umqtt.robust import MQTTClient #no esta incluida en el firmware para el esp32, deben ser agregados los scripts de mqtt
import time

#funcion de callback
def cb(topic, msg):
	print(msg)

#conexion wifi
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("SSID", "PASS")
time.sleep(5)

#credenciales para la conexion de ubidots
#token, clientid y topic al que se desea subscribirse
ubidotsToken = "TOKEN"
clientID = "CLIENTID"
topic="/v1.6/devices/{devicelabel}/{labelvariable}/lv" #el topic define a que device en especifico es que se va a subir datos
                                 #b"/v1.6/devices/{NOMBRE_DISPOSITIVO}" en el que NOMBRE_DISPOSITIVO es quien
                                 #define entre los devices creados al cual se quiere subir el dato

#construccion de objeto mqtt para la conexion
client = MQTTClient(clientID, "industrial.api.ubidots.com", 1883, user = ubidotsToken, password = ubidotsToken) #creacion de objeto
client.connect() #conexion a ubidots

#setear funcion de callback cb
client.set_callback(cb)
#subscripcion al topic                    
client.subscribe(bytes(topic, 'utf-8'))

while True:
    try:
    	#metodo para escuchar mensajes
        client.wait_msg()        
    except Exception as e:
        print(e)
        client.disconnect()
		sys.exit()
