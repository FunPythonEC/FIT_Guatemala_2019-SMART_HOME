from machine import Pin
import time

rele1 = Pin(12, Pin.OUT)
rele2 = Pin(13, Pin.OUT)

rele1.on()
time.sleep(1)
rele2.on()
time.sleep(1)
rele1.on()
time.sleep(1)
rele1.off()
rele2.off()
