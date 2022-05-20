#include <Servo.h>

Servo myservo; 
Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
 // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
int pos2 = 30;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  servo1.attach(10);
  servo2.attach(11);
  servo3.attach(12);
  servo4.attach(13);
}

void loop() {
  for (pos = 0; pos <= 300; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);
    servo1.write(pos);
    servo2.write(pos);
    servo3.write(pos);
    servo4.write(pos);
    delay(10);
  }
}
