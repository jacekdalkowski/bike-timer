#include <SPI.h>
#include <RF24.h>

RF24 radio(9,8);

void setup()
{ 
  Serial.begin(9600);
  radio.begin();
  radio.openReadingPipe(0, 1);
  radio.startListening();
}

void loop()
{  
  if (radio.available()){
    Serial.println("Radio available.");
    while(radio.available()){
      char text[32] = {0};
      radio.read(text, sizeof(text));
      Serial.println("Received: ");
      Serial.println(text);
    }
  }else{
    Serial.println("Nothing available now.");
  }

  delay(1000);  
}

