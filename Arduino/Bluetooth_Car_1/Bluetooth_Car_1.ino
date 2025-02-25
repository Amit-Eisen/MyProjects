#include <SoftwareSerial.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// Initialize the LCD display
LiquidCrystal_I2C lcd(0X27, 16, 2);

// Motor control pins
int motor1_PWM = 6;
int motor1_DirA = 7;
int motor1_DirB = 8;
int motor2_PWM = 5;
int motor2_DirA = 4;
int motor2_DirB = 3;

// Ultrasonic sensor pins
int trigpin_front = 12;
int echopin_front = 13;
int trigpin_back = 9;
int echopin_Back = 10;

// Light pins
int leftlight = 9;
int rightlight = 2;

// Bluetooth communication
SoftwareSerial bluetooth(10, 11);

void setup() {
  // Motor control pins as output
  pinMode(motor1_PWM, OUTPUT);
  pinMode(motor1_DirA, OUTPUT);
  pinMode(motor1_DirB, OUTPUT); 
  pinMode(motor2_PWM, OUTPUT); 
  pinMode(motor2_DirA, OUTPUT);
  pinMode(motor2_DirB, OUTPUT);

  // Light pins as output
  pinMode(leftlight, OUTPUT);
  pinMode(rightlight, OUTPUT);

  // Ultrasonic sensor pins
  pinMode(trigpin_front, OUTPUT);
  pinMode(echopin_front, INPUT);
  pinMode(trigpin_back, OUTPUT);
  pinMode(eechopin_Back, INPUT);

  //LCD setup
  lcd.begin(16,2);

  // Set up Bluetooth communication
  Serial.begin(9600);
  bluetooth.begin(9600);
}

void loop() {
    if (bluetooth.available() > 0){
      char command = bluetooth.read();

      // Control the car based on the input
      switch ( command) {
        case 'F':
          moveForward();
          break;
        case 'B':
          moveBackward();
          break;
        case 'L':
          turnLeft();
          break;
        case 'R':
          turnRight();
          break;
        case 'S':
          stopCar();
          break;
      }
    } else {
      // Display a messsage if Bluetooth is not connected
      lcd.clear();
      lcd.print("Bluetooth");
      lcd.setCursor(0, 1);
      lcd.print("Not Connected");
      delay(500);
    }

  // Display distance on LCD
  displayDistance();
}

void moveForward() {
  int distanceFront = getDistance(trigpin_front, echopin_front);

  if (distanceFront > 10) {
    // Move forward if there is no obstacle
    digitalWrite(motor1_DirA, HIGH);
    digitalWrite(motor1_DirB, LOW);
    analogWrite(motor1_PWM, 255);

    digitalWrite(motor2_DirA, HIGH);
    digitalWrite(motor2_DirB, LOW);
    analogWrite(motor2_PWM, 255);

    // Turn off lights when moving forward
    digitalWrite(leftlight, LOW);
    digitalWrite(rightlight, LOW);
  } else {
    stopCar(); // Stop car if too close
  }
}

void moveBackward() {
  int distanceBack = getDistance(trigpin_back, echopin_Back);
  
  if (distanceBack > 10) {
    // Move backward if there is no obstacle
    digitalWrite(motor1_DirA, LOW);
    digitalWrite(motor1_DirB, HIGH);
    analogWrite(motor1_PWM, 255);

    digitalWrite(motor2_DirA, LOW);
    digitalWrite(motor2_DirB, HIGH);
    analogWrite(motor2_PWM, 255);
  } else{
    // Stop car if too close
    stopCar(); 
  }
    // Turn off lights when moving backward
    digitalWrite(leftlight, LOW);
    digitalWrite(rightlight, LOW);
}

void turnLeft() {
  digitalWrite(motor1_DirA, LOW);
  digitalWrite(motor1_DirB, HIGH);
  analogWrite(motor1_PWM, 150);

  digitalWrite(motor2_DirA, HIGH);
  digitalWrite(motor2_DirB, LOW);
  analogWrite(motor2_PWM, 150);

  // Turn on left light when turning left
  blinklight(leftlight);
  digitalWrite(rightlight, LOW);
}

void turnRight() {
  digitalWrite(motor1_DirA, HIGH);
  digitalWrite(motor1_DirB, LOW);
  analogWrite(motor1_PWM, 150);

  digitalWrite(motor2_DirA, LOW);
  digitalWrite(motor2_DirB, HIGH);
  analogWrite(motor2_PWM, 150);

  // Turn on right light when turning rightc:\Users\eisen\Downloads\Ex4 UDF.c
  blinklight(rightlight);
  digitalWrite(leftlight, LOW);
}

void stopCar() {
  digitalWrite(motor1_DirA, LOW);
  digitalWrite(motor1_DirB, LOW);
  digitalWrite(motor1_PWM, 0);

  digitalWrite(motor2_DirA, LOW);
  digitalWrite(motor2_DirB, LOW);
  digitalWrite(motor2_PWM, 0);

    // Turn on lights when stopping
  digitalWrite(leftlight, HIGH);
  digitalWrite(rightlight, HIGH);
}

void blinklight(int lightPin) {
    // Blink the specified light
  digitalWrite(lightPin, HIGH);
  delay(250);  // Blink rate
  digitalWrite(lightPin, LOW);
}

void displayDistance() {
  // Reading distance from the front sensor
  int distanceFront = getDistance(trigpin_front, echopin_front);
  lcd.setCursor(0, 0);
  lcd.print("Front : ");
  lcd.print(distanceFront);
  lcd.print(" cm.");

  // Reading distance from the back sensor
  int distanceBack = getDistance(trigpin_back, echopin_Back);
  lcd.setCursor(0, 1);
  lcd.print("Back : ");
  lcd.print(distanceBack);
  lcd.print(" cm.");
}

int getDistance(int trigPin, int echoPin) {
  // Measuring distance using ultrasonic sensor
  digitalWrite(trigPin, LOW);
  delayMicroseconds(3);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);

  return pulseIn(echoPin, HIGH) / 2;
}