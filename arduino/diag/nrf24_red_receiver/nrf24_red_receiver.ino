



//"SPI.h/Nordic_nRF8001.h/RBL_nRF8001.h" are needed in every new project
#include <SPI.h>
//#include <Nordic_nRF8001.h>
#include <EEPROM.h>
#include <boards.h>
#include <RBL_nRF8001.h>
//#include <nRF24L01.h>
#include <RF24.h>
//#include <RF24_config.h>

RF24 radio(9,8);
//RF24 radio(13, 12);
const byte rxAddr[6] = "00001";

void setup()
{ 
  // Set your BLE advertising name here, max. length 10
  ble_set_name("teraz 2");
  
  // Init. and start BLE library.
  ble_begin();
  
  // Enable serial debug
  Serial.begin(9600);

  radio.begin();
  radio.openReadingPipe(0, 1);
  radio.startListening();
}

void loop()
{
ble_do_events();
  
  if(ble_busy()){
    Serial.println("BLE busy.");
  }else if ( ble_available() ){
    while ( ble_available() )
      Serial.write(ble_read());
      
    Serial.println();
  }else if (radio.available()){
    Serial.println("Radio available.");
    char text[32] = {0};
    radio.read(text, sizeof(text));
    Serial.println("Received: ");
    Serial.println(text);
  }else{
    Serial.println("Nothing available now.");
  }

  

  delay(1000);  
}

