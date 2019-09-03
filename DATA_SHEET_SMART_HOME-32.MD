# SMART BADGE

<p align="center">
  <img width="640" height="480" src="/imagenes/SmartHomes.png">
</p>

## DISPOSITIVOS

### Temperatura, humedad y presión atmosférica - I2C
ESP32 | BME280
--- | ---
SCL 22 | SCK 4
SDA 23 | SDI 3

### Acelerometro/Giroscopio - I2C
ESP32 | MMA8425QT
--- | ---
SCL 22 | SCL 4
SDA 23 | SDA 6

### RELES - GPIO DIGITAL
 . | RELE Izquierda | RELE Derecha
--- | --- | ---
ESP32 | GPIO 12 | GPIO 13

### BUZZER - GPIO PMW
ESP32 | BUZZER
--- | ---
GPIO 14  | DIN
GND | GND

### NEOPIXEL 
ESP32 | LED
--- | ---
GPIO 15  | DIN
GND | GND
5V | 5V