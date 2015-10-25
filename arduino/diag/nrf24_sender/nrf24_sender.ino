
/*
* Getting Started example sketch for nRF24L01+ radios
* This is a very basic example of how to send data from one node to another
* Updated: Dec 2014 by TMRh20
*/

#include <SPI.h>
#include <nRF24L01.h>
#include <RF24.h>


/* Hardware configuration: Set up nRF24L01 radio on SPI bus plus pins 7 & 8 */
RF24 radio(7,8);
/**********************************************************/

byte address[6] = "00001";
const char text[] = "ab";


void setup() {
  Serial.begin(9600);
  Serial.println(F("RF24/examples/GettingStarted"));
  Serial.println(F("*** PRESS 'T' to begin transmitting to the other node"));
  
  radio.begin();

  // Set the PA Level low to prevent power supply related issues since this is a
 // getting_started sketch, and the likelihood of close proximity of the devices. RF24_PA_MAX is default.
  //radio.setPALevel(RF24_PA_LOW);
  
radio.setRetries(15, 15);
radio.stopListening();
    radio.openWritingPipe(address);
    

}

void loop() {
  
  
/****************** Ping Out Role ***************************/  

    
    Serial.println(F("Now sending"));
    if(radio.write(&text, sizeof(text) )){
      Serial.println("succesfully sent!!!!!!!!!!!!!!!!!!!!!!!!!");
    }else{
      Serial.println("NOT succesfully sent");
    }
    
delay(2000);

} // Loop
