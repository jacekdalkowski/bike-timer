#include <SPI.h>
#include "RF24.h"

RF24 radio(7,8);

byte address[] = "00001";
const char text[] = "bike";

void setup() {
  Serial.begin(9600);
  radio.begin();
  radio.openWritingPipe(address);
}

void loop() {
  Serial.println(F("Now sending"));
  if(radio.write(text, sizeof(text) )){
    Serial.println("succesfully sent");
  }else{
    Serial.println("NOT succesfully sent");
  }
    
  delay(500);
} 

