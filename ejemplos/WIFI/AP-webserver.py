import network 
import socket
import time

ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid='Tu-nombre')
ap.config(authmode=3, password='123456789')
ap.ifconfig()

html= """<html>
  <head>
    <meta charset="uft-8"/>
    <title>Hola Mundo en HTML</title>
  </head>
  <body>
    <h1>Hola FIT 2019</h1>
  </body>
</html>"""

 #Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
time.sleep(3)
s.bind(('', 80))
s.listen(5)
while True:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        print(request)
        
        
        response = html
        conn.send(response)
        conn.close()

    