
#define BUTTON 5 // for GPIO 5
#define LED 4 // for GPIO 4

int buttonState = 0; 

void setup() {
  // initialize the LED pin as an output:
  Serial.begin(9600); 
  pinMode(BUTTON, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {
  buttonState = digitalRead(BUTTON); 
  if(buttonState == HIGH){
    digitalWrite(LED, HIGH);
  }
  if(buttonState == LOW){
    digitalWrite(LED, LOW); 
  }
  
}
