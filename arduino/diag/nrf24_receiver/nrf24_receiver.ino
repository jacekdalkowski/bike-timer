



//"SPI.h/Nordic_nRF8001.h/RBL_nRF8001.h" are needed in every new project
#include <SPI.h>
//#include <Nordic_nRF8001.h>
#include <EEPROM.h>
#include <boards.h>
#include <RBL_nRF8001.h>
#include <nRF24L01.h>
#include <RF24.h>
//#include <RF24_config.h>

RF24 radio(9,8);
//RF24 radio(13, 12);
const byte rxAddr[6] = "00001";

void setup()
{
  //  
  // For BLE Shield or Blend:
  //   Default pins set to 9 and 8 for REQN and RDYN
  //   Set your REQN and RDYN here before ble_begin() if you need
  //
  // For Blend Micro:
  //   Default pins set to 6 and 7 for REQN and RDYN
  //   So, no need to set for Blend Micro.
  //
  //ble_set_pins(3, 2);
  
  // Set your BLE advertising name here, max. length 10
  ble_set_name("teraz");
  
  // Init. and start BLE library.
  ble_begin();
  
  // Enable serial debug
  Serial.begin(9600);

  radio.begin();
  radio.openReadingPipe(0, rxAddr);
  
  radio.startListening();
}

unsigned char buf[16] = {0};
unsigned char len = 0;

void loop()
{
  if(ble_busy()){
    Serial.println("ble busy");
  }else if ( ble_available() ){
    Serial.println("ble available");
    while ( ble_available() )
    {
      Serial.write(ble_read());
    }
    Serial.println();
  }else if (radio.available()){
    Serial.println("radio available");
    /*if ( ble_connected() )
    {
      ble_write('H');
      ble_write('e');
      ble_write('l');
      ble_write('l');
      ble_write('o');
      ble_write(' ');
      ble_write('W');
      ble_write('o');
      ble_write('r');
      ble_write('l');
      ble_write('d');
      ble_write('!');
    }*/
    char text[32] = {0};
    radio.read(&text, sizeof(text));

    Serial.println("read sth: ");
    Serial.println(text);
  }else{
    Serial.println("nothing available teraz");
  }

  ble_do_events();
  
  /*if ( ble_available() )
  {
    while ( ble_available() )
    {
      Serial.write(ble_read());
    }
    
    Serial.println();
  }*/


 
  delay(1000);  
}

