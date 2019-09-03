from machine import Pin
import machine, neopixel, time

# numero de pixeles
n = 10
# pin GPIO
p = 15
np = neopixel.NeoPixel(machine.Pin(p), n)

def wheel(pos):
  if pos < 0 or pos > 255:
    return (0, 0, 0)
  if pos < 85:
    return (255 - pos * 3, pos * 3, 0)
  if pos < 170:
    pos -= 85
    return (0, 255 - pos * 3, pos * 3)
  pos -= 170
  return (pos * 3, 0, 255 - pos * 3)

def rainbow_cycle(wait):
  for j in range(255):
    for i in range(n):
      rc_index = (i * 256 // n) + j
      np[i] = wheel(rc_index & 255)
    np.write()
    time.sleep_ms(wait)

#apagar
def clear():
  for i in range(n):
    np[i] = (0, 0, 0)
    np.write()

while True:
    rainbow_cycle(1) # para variar la velocidad de transicion cambiar el valor desde 1
