#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// WiFi/MQTT parameters
#define WLAN_SSID       "HP-Photosmart-D1100"
#define WLAN_PASS       "lmaothisisnotaprinter"
#define BROKER_IP       "10.0.0.130"

//pins
#define LED 5 //define 
#define BUTTON 4

int buttonState = 0; 

WiFiClient client;
PubSubClient mqttclient(client);

void callback (char* topic, byte* payload, unsigned int length) {
  Serial.println(topic);
  Serial.write(payload, length); //print incoming messages
  Serial.println("");

  payload[length] = '\0'; // add null terminator to byte payload so we can treat it as a string

  // test for sending message to pi
  //mqttclient.publish("/test", "Hello pi", false);

  if (strcmp(topic, "/led") == 0){
     if (strcmp((char *)payload, "on") == 0){
        digitalWrite(LED, HIGH);
     } else if (strcmp((char *)payload, "off") == 0){
        digitalWrite(LED, LOW);
     }
  }
}


void setup() {
  Serial.begin(115200);
  
  // connect to wifi
  WiFi.mode(WIFI_STA);
  WiFi.begin(WLAN_SSID, WLAN_PASS);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(F("."));
  }

  Serial.println(F("WiFi connected"));
  Serial.println(F("IP address: "));
  Serial.println(WiFi.localIP());

  // connect to mqtt server
  mqttclient.setServer(BROKER_IP, 1883);
  mqttclient.setCallback(callback);
  connect();

  //setup pins
  pinMode(LED, OUTPUT); // setup pin for input
  pinMode(BUTTON, INPUT); 
  //mqttclient.publish("/test", "hey", false);
}

void loop() {
  if (!mqttclient.connected()) {
    connect();
  }
  //mqttclient.publish("/test", "hey", false); 
  
  // sending message to pi
  buttonState = digitalRead(BUTTON);
  if(buttonState == HIGH){
    mqttclient.publish("/test", "on", false); 
  }
  else if(buttonState == LOW){
    mqttclient.publish("/test", "off", false); 
  }
  

  mqttclient.loop();
}


void connect() {
  while (WiFi.status() != WL_CONNECTED) {
    Serial.println(F("Wifi issue"));
    delay(3000);
  }
  Serial.print(F("Connecting to MQTT server... "));
  while(!mqttclient.connected()) {
    if (mqttclient.connect(WiFi.macAddress().c_str())) {
      Serial.println(F("MQTT server Connected!"));

       mqttclient.subscribe("/led");
      
    } else {
      Serial.print(F("MQTT server connection failed! rc="));
      Serial.print(mqttclient.state());
      Serial.println("try again in 10 seconds");
      // Wait 5 seconds before retrying
      delay(20000);
    }
  }
}
