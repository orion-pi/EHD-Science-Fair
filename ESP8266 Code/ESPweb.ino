#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include "SparkFun_Qwiic_Scale_NAU7802_Arduino_Library.h"
#include <Wire.h>

const size_t LEN_BUF = 1024;
const int PORT = 8888;
const int SERIAL_BAUDRATE = 115200; 
WiFiServer server(PORT);
NAU7802 Loadcell; 


void setup() {
  delay(1000);

  Serial.begin(SERIAL_BAUDRATE);
  
  Serial.println("Calibrated system offset");
  Serial.print("Configuring access point...");
  WiFi.softAP("Science Fair");
  IPAddress myIP = WiFi.softAPIP();
  server.begin();
  Serial.println(WiFi.localIP());  
  Wire.begin();
  if (Loadcell.begin() == false)
  {
    Serial.println("Scale not detected. Please check wiring. Freezing...");
    while (1);
  }
  Serial.println("Scale detected!");
  Loadcell.setSampleRate(NAU7802_SPS_320);
  Loadcell.calibrateAFE(); 
}



void loop() {
  
  
  WiFiClient client = server.available();
  
  if (client) {
    while(client.connected()){   
      while(client.available()>0){
        // read data from the connected client
        
      
      if(Loadcell.available() == true && client.read() == 'c')
  {
    long currentReading = Loadcell.getAverage(128);
    Serial.println(currentReading);
        client.print(currentReading);
  }
    }
    }
    client.stop();
    Serial.println("Client disconnected");    
  }
}
