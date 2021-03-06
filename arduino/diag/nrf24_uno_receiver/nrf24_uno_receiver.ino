#include <SPI.h>
#include <RF24.h>

RF24 radio(7,8);
const byte rxAddr[6] = "00001";

void setup()
{
  Serial.begin(9600);

  radio.begin();
  radio.openReadingPipe(0, 1);
  radio.startListening();
}

unsigned char buf[16] = {0};
unsigned char len = 0;

void loop()
{
  if (radio.available()){
    Serial.println("========== Radio available. ==========");

    char text[32] = {0};
    while(radio.available()){
      radio.read(text, sizeof(text));
      Serial.println("Received: ");
      Serial.println(text);
    }
    Serial.println("======================================");
  }else{
    Serial.println("Nothing available.");
  }
 
  delay(500);  
}

