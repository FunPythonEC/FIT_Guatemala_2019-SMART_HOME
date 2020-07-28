# SMART HOME



<p align="center">
  <src="https://raw.githubusercontent.com/FunPythonEC/ConectateGT/master/media/arcoriiris.jpeg
">
</p>

<p align="center">
  <img width="800" height="565" src="/imagenes/SmartHomes.jpg">
</p>

## DISPOSITIVOS

### Temperatura, humedad y presión atmosférica - I2C
ESP32 | BME280
--- | ---
SCL 22 | SCK 4
SDA 23 | SDI 3

### Acelerometro/Giroscopio - I2C
ESP32 | MMA8452QT
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

### FOTORESISTENCIA - ADC
ESP32 | FOTORESISTENCIA
--- | ---
GPIO 2 | ADC

### NEOPIXEL 
ESP32 | LED
--- | ---
GPIO 15  | DIN
GND | GND
5V | 5V


