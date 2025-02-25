const int relaysPins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
const int thermistorPins[8] = {A0, A1, A2, A3, A4, A5, A6, A7};

void setup() {
    Serial.begin(9600);

    for (int i = 0; i < 8; i++) 
    {
        pinMode(relaysPins[i], OUTPUT);
        digitalWrite(relaysPins[i], HIGH);
    }
}

void loop() {
    // Read analog sensor states and relay states
    
    int analogSensorStates[8];
    int relayStates[8];

    for (int i = 0; i < 8; i++)
    {
        analogSensorStates[i] = analogRead(thermistorPins[i]);
        relayStates[i] = digitalRead(relaysPins[i]);
    }

    // Check for incoming commands from Python
    if (Serial.available() > 0)
    {
        String command = Serial.readStringUntil('\n');
        if (command.startsWith("RELAY ")) {
            int relayIndex = command.substring(6, 7).toInt();
            int newState = command.substring(8, 9).toInt();
            if (relayIndex >= 0 && relayIndex < 8) {
                digitalWrite(relaysPins[relayIndex], newState);
                relayStates[relayIndex] = newState;
            } else {
                Serial.println("Invalid relay index received from Python.");
            }
        } else {
            Serial.println("Invalid command received from Python.");
        }
    }

    // Send analog readings and relay states to Python
    for (int i = 0; i < 8; i++)
    {
        Serial.print("Th ");
        Serial.print(i);
        Serial.print(": ");
        Serial.print(analogSensorStates[i]);
        Serial.print(": ");
        Serial.println(relayStates[i]);
    }

    delay(1000);
}