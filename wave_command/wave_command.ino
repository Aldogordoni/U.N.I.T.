#include <Servo.h>

Servo myservo; 
Servo servo2;
 // create servo object to control a servo
// twelve servo objects can be created on most boards

int pos = 0;    // variable to store the servo position
//int pos2 = 180;

void setup() {
  myservo.attach(9);  // attaches the servo on pin 9 to the servo object
  //servo2.attach(10);
}

void loop() {
  for (pos = 0; pos <= 300; pos += 1) { // goes from 0 degrees to 180 degrees
    // in steps of 1 degree
    myservo.write(pos);
    delay(15);
  }
}
