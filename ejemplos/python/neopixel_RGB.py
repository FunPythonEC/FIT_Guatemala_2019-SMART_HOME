import machine, neopixel, time

numero_leds=10
pin_salida=15

np = neopixel.NeoPixel(machine.Pin(pin_salida), numero_leds)
#ROJO
for led in range(0,numero_leds,1):
    np[led]=(255,0,0)
    np.write()
    time.sleep(1)
print("ROJO")
#VERDE
for led in range(0,numero_leds,2):
    np[led]=(0,255,0)
    np.write()
    time.sleep(1)  
print("VERDE")  
#AZUL
for led in range(0,numero_leds,3):
    np[led]=(0,0,255)
    np.write()
    time.sleep(1)  
print("AZUL")
#BLANCO
for led in range(0,numero_leds,1):
    np[led]=(255,255,255)
    np.write()
    time.sleep(1)  
print("BLANCO")

#APAGAR
for led in range(0,numero_leds):
    np[led]=(0,0,0)
    np.write()  
print("APAGADO")

