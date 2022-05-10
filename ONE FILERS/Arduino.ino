#include <Servo.h>
Servo myServo;

int pinServo = 9;
int pinButton = 2;
int pinPotentiometer = A2;

float teaspoons;
int potentiometerValue;
int buttonValue;

void setup() {
  Serial.begin(9600);
  pinMode(pinButton, INPUT);
  digitalWrite(pinButton, HIGH);
  myServo.attach(pinServo);
}

void loop() {
  buttonValue = digitalRead(pinButton);

  if (buttonValue == 0) {
    potentiometerValue = analogRead(pinPotentiometer); // 0-1023

    myServo.write(180);
    delay(potentiometerValue * 2);
    myServo.write(0);

    // delay(2000);
  }
}

// ##################################################
// BASIC BUTTON

// int pinButton = 2;
// int buttonValue;

// void setup() {
//   Serial.begin(9600);
//   pinMode(pinButton, INPUT);
//   digitalWrite(pinButton, HIGH); // This is an important line
// }

// void loop() {
//   buttonValue = digitalRead(pinButton);
//   Serial.println(buttonValue);
//   delay(500);
// }



// ##################################################
// BASIC READING FROM POTENTIOMETER

// int pinPotentiometer=A2;
// int potentiometerValue;

// void setup() {
//   // Setup code
//   Serial.begin(9600);
// }

// void loop() {
//   // Read the volt over the potentiometer
//   potentiometerValue = analogRead(pinPotentiometer); // 0-1023
//   Serial.println(potentiometerValue);
// }



// ##################################################
// SERVO BASIC EXAMPLE

// #include <Servo.h>

// int pinServo=9;

// // Min:0 Max:180
// int servoPosition=10;
// // int servoPosition=170;
// // int servoPosition=180;

// Servo myServo;

// void setup() {
//   // put your setup code here, to run once:
//   Serial.begin(9600);
//   myServo.attach(pinServo);
// }

// void loop() {
//   // put your main code here, to run repeatedly:
//   myServo.write(servoPosition);
// }