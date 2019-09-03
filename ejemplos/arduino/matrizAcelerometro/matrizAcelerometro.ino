/* Ejemplo para badge Smart FIT basado en el ESP32
 * 
 * Este ejemplo muestra una flecha apuntado hacia 
 * arriba y en caso que el badge este en posicion plana 
 * muestra una cara feliz.
 * 
 * Ejemplo de prueba
 * 
 * Especificaciones del entorno de Desarrollo:
 * IDE: Arduino 1.8.9
 * Librerias: 
 *        -LedMatrix (https://github.com/squix78/MAX7219LedMatrix)
 *        -Sparkfun MMA8452Q (https://github.com/sparkfun/SparkFun_MMA8452Q_Arduino_Library)
 *        
 * Eduardo Contreras @ Electronic Cats 2019
 * 
 * Este código es beerware si tu me ves ( o cualquier otro miembro de Electronic Cats)
 * a nivel local, y tu has encontrado nuestro código útil ,
 * por favor comprar una ronda de cervezas!
 */


#include <SPI.h>
#include <Wire.h>
#include "LedMatrix.h"
#include "SparkFun_MMA8452Q.h"    

//IO22  SCL 
//IO23  SDA
//IO35  LED
//IO16  DI 
//IO17  CS
//IO21  CLK 


byte right[] = { B00011000,B00111100,B01111110,B11111111,B00011000,B00011000,B00011000,B00011000};
byte left[] = { B00011000,B00011000,B00011000,B00011000,B11111111,B01111111,B00111100,B00011000};
byte up[] = { B00001000,B00001100,B00001110,B11111111,B11111111,B00001110,B00001100,B00001000};
byte down[] = { B00010000,B00110000,B01110000,B11111111,B11111111,B01110000,B00110000,B00110000};
byte happy[] = { B00100100,B00100100,B00100100,B00100100,B00000000,B10000001,B01000010,B00111100};

void scanI2C(void);

LedMatrix ledMatrix = LedMatrix(1, 17);
MMA8452Q accel;                   


void setup(){
  SPI.begin(21,-1,16,17);
  Wire.begin(23,22);
  Serial.begin(9600);
  scanI2C();
  if (accel.begin() == false) {
    Serial.println("Error en acelerometro");
    while (1);
  }
  ledMatrix.init();
  ledMatrix.setIntensity(10); // range is 0-15
  ledMatrix.clear();
}
 
void loop(){
    if (accel.isRight() == true) {
      Serial.println("Right");
      for(int i=0;i<8;i++){
        ledMatrix.clear();
        ledMatrix.setColumn(i,right[i]);
        ledMatrix.commit();
      }
    }
    else if (accel.isLeft() == true) {
      Serial.println("Left");
      for(int i=0;i<8;i++){
        ledMatrix.clear();
        ledMatrix.setColumn(i,left[i]);
        ledMatrix.commit();
      }
    }
    else if (accel.isUp() == true) {
      Serial.println("Up");
      for(int i=0;i<8;i++){
        ledMatrix.clear();
        ledMatrix.setColumn(i,up[i]);
        ledMatrix.commit();
      }
    }
    else if (accel.isDown() == true) {
      Serial.println("Down");
      for(int i=0;i<8;i++){
        ledMatrix.clear();
        ledMatrix.setColumn(i,down[i]);
        ledMatrix.commit();
      }
    }
    else if (accel.isFlat() == true) {
      Serial.println("Flat");
      for(int i=0;i<8;i++){
        ledMatrix.clear();
        ledMatrix.setColumn(i,happy[i]);
        ledMatrix.commit();
      }
    }
}



void scanI2C(){
  byte error, address;
  int nDevices;
    
  Serial.println("Scanning...");
  nDevices = 0;
  for(address = 1; address < 127; address++ ) 
  {
    // The i2c_scanner uses the return value of
    // the Write.endTransmisstion to see if
    // a device did acknowledge to the address.
    Wire.beginTransmission(address);
    error = Wire.endTransmission();

    if (error == 0)
    {
      Serial.print("I2C device found at address 0x");
      if (address<16) 
        Serial.print("0");
      Serial.print(address,HEX);
      Serial.println("  !");

      nDevices++;
    }
    else if (error==4) 
    {
      Serial.print("Unknown error at address 0x");
      if (address<16) 
        Serial.print("0");
      Serial.println(address,HEX);
    }    
  }
  if (nDevices == 0)
    Serial.println("No I2C devices found\n");
  else
    Serial.println("done\n");

  delay(1000);           // wait 5 seconds for next scan
  }
