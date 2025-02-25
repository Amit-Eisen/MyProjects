Bluetooth Controlled Car with Obstacle Avoidance
This Arduino project implements a Bluetooth-controlled car with obstacle avoidance capabilities. 
The car is equipped with ultrasonic sensors for distance measurement and is remotely controlled using a Bluetooth-enabled device.

Components Used:
 - Arduino board
 - Motor driver module
 - Ultrasonic sensors
 - Bluetooth module (e.g., HC-05)
 - LCD Display

Libraries:
 - SoftwareSerial
 - Wire
 - LiquidCrystal_I2C

Functionality:
 - Bluetooth communication for remote control.
 - Motor control (forward, backward, left, right).
 - Obstacle avoidance using ultrasonic sensors.
 - Real-time distance feedback displayed on an LCD screen.

Usage:
 - Upload the provided Arduino code (Bluetooth_Car.ino) to your Arduino board.
 - Connect the components based on the wiring instructions.
 - Power up the Arduino and pair it with your Bluetooth-enabled device.
 - Use commands ('F', 'B', 'L', 'R', 'S') to control the car.

Notes:
 - Establish Bluetooth connection before controlling the car.
 - LCD display shows real-time distance from obstacles.
