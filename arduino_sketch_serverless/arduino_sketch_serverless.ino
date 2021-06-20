#include <SoftwareSerial.h>

#define BT_TX_PIN 12
#define BT_RX_PIN 11
SoftwareSerial bt =  SoftwareSerial(BT_RX_PIN, BT_TX_PIN);
int greenLedPin = 4;
const int yellowLedPin = 3;
const int redLedPin = 2;
const int piezoPin = 8;
const int photoresistorPin = A0;
int photoresistorValue = 0;
int photoresistorValueMax = 0;
int photoresistorValueMin = 1023;
int danger = 0;

void setup() {
  pinMode(BT_RX_PIN, INPUT);
  pinMode(BT_TX_PIN, OUTPUT);

  //Serial communication
  Serial.begin(9600);

  //Bluetooth communication
  bt.begin(9600);
  setupAndSetLedPin(); 
  
  photoresistorSetupAndCalibration();
  
  waitForBluetoothConnection();
  delay(3000);
}

void photoresistorSetupAndCalibration(){
  setLedSensor(HIGH, LOW, LOW);
  while(millis() < 5000){
    photoresistorValue = analogRead(photoresistorPin);
    if(photoresistorValue > photoresistorValueMax){
      photoresistorValueMax = photoresistorValue;  
    }
    
    if(photoresistorValue < photoresistorValueMin){
      photoresistorValueMin = photoresistorValue;  
    }
  }
}

void waitForBluetoothConnection(){
  setLedSensor(HIGH, HIGH, LOW);
  while (bt.available()==0){
    Serial.println("Waiting for connection");
    delay(1000);
  }
  setLedSensor(HIGH, HIGH, HIGH);
}

void setupAndSetLedPin(){
  pinMode(greenLedPin, OUTPUT);
  pinMode(yellowLedPin, OUTPUT);
  pinMode(redLedPin, OUTPUT);
  setLedSensor(LOW, LOW, LOW);
}

void loop() {
  photoresistorValue = analogRead(photoresistorPin);
  bt.println(photoresistorValue);
  danger = map(photoresistorValue, photoresistorValueMin, photoresistorValueMax, 1, 3);
  if(danger == 1){
    setLedSensor(HIGH, LOW, LOW);
  }else if(danger == 2){
    setLedSensor(HIGH, HIGH, LOW);
    emitAlarm(photoresistorValue);
  }else if(danger == 3){
    setLedSensor(HIGH, HIGH, HIGH);
    emitAlarm(photoresistorValue);
  }
  delay(200);
}

void setLedSensor(int greenLedValue, int yellowLedValue, int redLedValue){
  digitalWrite(greenLedPin, greenLedValue);
  digitalWrite(yellowLedPin, yellowLedValue);
  digitalWrite(redLedPin, redLedValue);
}

void emitAlarm(int photoresistorValue){
  int pitch = map(photoresistorValue, photoresistorValueMin, photoresistorValueMax, 50, 4000);
  tone(piezoPin, pitch, 20);  
}
