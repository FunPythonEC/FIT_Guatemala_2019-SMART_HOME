from umqtt.robust import MQTTClient
import time

MQTT_CLIENT_ID = "basicPubSub"
MQTT_PORT = 1883
MQTT_TOPIC = ""
MQTT_HOST = "fit2019.ejambre.ec"
WIFI_SSID = ""
WIFI_PW = ""

mqtt_client = None
def cb(topic, msg):
	print(msg)
    
def pub_msg(msg):
    global mqtt_client
    try:    
        mqtt_client.publish(MQTT_TOPIC, msg)
        print("Enviado: " + msg)
    except Exception as e:
        print("Excepcion de publicacion: " + str(e))
        raise

def sub_msg():
    global mqtt_client
    try:    
        mqtt_client.set_callback(cb)
        mqtt_client.subscribe(bytes(MQTT_TOPIC, 'utf-8'))
        mqtt_client.wait_msg()
    except Exception as e:
        print(e)            

def connect_mqtt():    
    global mqtt_client

    mqtt_client = MQTTClient(client_id=MQTT_CLIENT_ID, 
                                 server=MQTT_HOST, 
                                 port=MQTT_PORT, 
                                 keepalive=5000, 
                                 ssl=True)
    mqtt_client.connect()
    print('MQTT conectado')    

        

        
    except Exception as e:
        print('No se puede conectar MQTT: ' + str(e))
        raise

while True:
    #start execution
    try:
        print("Conectando a WIFI")
        #connect_wifi(WIFI_SSID, WIFI_PW)
        print("Conectando MQTT")
        connect_mqtt()
        print("Publicando")
        pub_msg("{\"SMART_HOME-32\":" + str(time.time()) + "}")
        print("OK")
        sub_msg()
        time.sleep(10)
    except Exception as e:
        print(str(e))


      