#include <Servo.h>
#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
#include <math.h>

// Define motors pins
const int base_servo_pin = 9;
const int arm_servo_pin = 10;

// Define PID parameters, calculate and testing is needed

double Kp = 1.0;
double Ki = 0.1;
double Kd = 0.01;

// Define setpoint for servo
double base_setpoint = 90;
double arm_setpoint = 90;

// PID variables
double base_integral, arm_integral;
double base_error, arm_error;
double base_derivative, arm_derivative;
double base_output, arm_output;


// Initialize servos and acceleromter
Servo base_servo;
Servo arm_servo;
Adafruit_ADXL345_Unified accel;


void setup() {
  Serial.begin(9600);

  // Attach servo to pin
  base_servo.attach(base_servo_pin);
  arm_servo.attach(arm_servo_pin);

  // Checking accelerometer intiliazition
  if (!accel.begin()) {
    Serial.println("Couldn't find sensor");
    while (1);
  }
}

void loop() {
  sensors_event_t event;
  accel.getEvent(&event);

  // Calculate roll and pitch angles in radians
  double roll = atan2(-event.acceleration.y, event.acceleration.z);
  double pitch = atan2(event.acceleration.x, sqrt(pow(event.acceleration.y, 2) + pow(event.acceleration.z,2)));

  // Map angles to servo positions
  double arm_angle = map(roll * RAD_TO_DEG, -90, 90 , 0, 180);
  double base_angle = map(pitch * RAD_TO_DEG, -90, 90, 0, 180);

  // PID control for each servo
  base_error = base_setpoint - base_angle;
  base_integral += base_error;
  base_derivative = base_error - base_derivative;
  base_output = (Kp * base_error) + (Ki * base_integral) + (Kd * base_derivative);

  arm_error = arm_setpoint - arm_angle;
  arm_integral += arm_error;
  arm_derivative = arm_error - arm_derivative;
  arm_output = (Kp * arm_error) + (Ki * arm_integral) + (Kd * arm_derivative);

  base_servo.write(base_setpoint + base_output);
  arm_servo.write(arm_setpoint + arm_output);

  // Print data for debug
  Serial.print("Pitch: ");
  Serial.print(pitch);
  Serial.print("\t Roll: ");
  Serial.print(roll);
  Serial.print("\t Base angle: ");
  Serial.print(base_angle);
  Serial.print("\t Arm angle: ");
  Serial.println(arm_angle);

  delay(100);
}