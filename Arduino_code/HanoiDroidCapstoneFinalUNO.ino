/*
The following code is part of the capstone HANOI DROID -  Camosun College. Term: Fall 2023
Purpose: control a set of servomotors that are part of the Inmoov Robot (https://inmoov.fr/), moving the arm to reach discs and solve the Hanoi Towers Game.
It is heavily supported with a Python program that using OpenCV detects the discs position 
Hardware: Arduino UNO

Hanoi complete set of movements:
1 to 3,  1 to 2, 3 to 2, 1 to 3, 2 to 1, 2 to 3, 1 to 3.


The strategy:

From the target position, we need to reach a hover position before, after, and between each target, the hover position is mandatory. I similar like a manual gearbox of a car, before moving between the gears,
it is necesary to go to a kind of transition level.


h0-----h1------h2------h3
|       |      |        |
|       |      |        |
|       |      |        |
p0      p1     p2       p3

p0 is the rest position, and p1, p2 and p3 the positions respectively

Command Codes for movements:

S (uppercase): start the robot: this for initalize the robot and rise the hand to start the movements. from p0 - h0. It is suppposed the Robot rest in p0
a:  movement disc from 1 to 3. This is h1-p1-h1-h3-p3-h3
b:  movement disc from 1 to 2. this is h1-p1-h1-h2-p2-h2
c:  movement disc from 3 to 2. this is h3-p3-h3-h2-p2-h2
d:  movement disc from 1 to 3. this is h1-p1-h1-h3-p3-h3
e:  movement disc from 2 to 1. this is h2-p2-h2-h1-p1-h1
f:  movement disc from 2 to 3. this is h2-p2-h2-h3-p3-h3
g:  movement disc from 1 to 3. this is h1-p1-h1-h3-p3-h3
R (uppercase): rest. Send the robot arm to the rest position. h0 - p0

*/

//---------LIBRARIES-------------
#include <Servo.h>
//---------END OF LIBRARIES-------------




//----------MACROS -------------------
#define rMagnetPin A0  //Digital pin A0
//--------END OF MACROS-----------------------


//-------------OBJECTS DECLARATION-------------------
Servo rthumb, rindex, rmajeur, rpinky, rring, rbicep, rrotate, rshoulder, rclavi;
//-------------END OF OBJECTS DECLARATION-------------------



//--------------GLOBAL VARIABLES--------------

bool robotStarted = false;
char rMagnetInUse = 0;  // indicates if the magnet is on or off

//--------END OF GLOBAL VARIABLES ---------------------------------

//---------FUNCTION DECLARATION--------------------
void rUseMagnet(void);      //function used to turn on or off the magnet -  right arm. this Function works in alternate mode.
void rGoToHover0(void);     //function that send commands to the servomotors to go to the hover0 position
void rGoToHover1(void);     //function that send commands to the servomotors to go to the hover1 position
void rGoToHover2(void);     //function that send commands to the servomotors to go to the hover2 position
void rGoToHover3(void);     //function that send commands to the servomotors to go to the hover3 position
void rGoToPosition0(void);  //function that send commands to the servomotors to go to the rest position
void rGoToPosition1(void);  //function that send commands to the servomotors to go to the disc1 position
void rGoToPosition2(void);  //function that send commands to the servomotors to go to the disc2 position
void rGoToPosition3(void);  //function that send commands to the servomotors to go to the disc3 position
//---------END OF FUNCTION DECLARATION--------------------


void setup() {


  //attach all the the servos names to a specific pin in the board (UNO)
  rthumb.attach(2);
  rindex.attach(3);
  rmajeur.attach(4);
  rpinky.attach(6);
  rring.attach(7);
  rbicep.attach(8);
  rrotate.attach(9);
  rshoulder.attach(10);
  rclavi.attach(11);

  delay(2000);
  // open the serial port:
  Serial.begin(115200);

  //this pin is the one to turn on/off the magnet. It setup as digital output
  pinMode(rMagnetPin, OUTPUT);

  //all the servos to rest position or p0
  rthumb.write(90);
  rindex.write(90);
  rrotate.write(80);
  rshoulder.write(60);
  rbicep.write(110);
  rclavi.write(105);
}


void loop() {


  if (Serial.available() > 0) {

    char receivedChar = Serial.read();



    if (!robotStarted && receivedChar == 'S') {
      // Check for the "start" command sent by the Python script
      startRobot();
      rGoToHover0();

      return;
    }


    //  Serial.print("Received command for servoPin: ");
    // Serial.println(commandMov);

    switch (receivedChar) {

      case 'a':  // movement disc from 1 to 3. This is h1-p1-h1-h3-p3-h3


        rGoToHover1();
        rGoToPosition1();
        rUseMagnet();
        delay(2000);
        rGoToHover1();
        rGoToHover3();
        rGoToPosition3();
        rUseMagnet();
        delay(1000);
        rGoToHover3();


        break;


      case 'b':  //movement disc from 1 to 2. this is h1-p1-h1-h2-p2-h2

        rGoToHover1();
        rGoToPosition1();
        rUseMagnet();
        delay(2000);
        rGoToHover1();
        rGoToHover2();
        rGoToPosition2();
        rUseMagnet();
        delay(1000);
        rGoToHover2();


        break;

      case 'c':  // movement disc from 3 to 2. this is h3-p3-h3-h2-p2-h2

        rGoToHover3();
        rGoToPosition3();
        rUseMagnet();
        delay(1000);
        rGoToHover3();
        rGoToHover2();
        rGoToPosition2();
        rUseMagnet();
        delay(1000);
        rGoToHover2();


        break;


      case 'd':  //movement disc from 1 to 3. this is h1-p1-h1-h3-p3-h3

        rGoToHover1();
        rGoToPosition1();
        rUseMagnet();
        delay(1000);
        rGoToHover1();
        rGoToHover3();
        rGoToPosition3();
        rUseMagnet();
        delay(1000);
        rGoToHover3();


        break;

      case 'e':  //movement disc from 2 to 1. this is h2-p2-h2-h1-p1-h1


        rGoToHover2();
        rGoToPosition2();
        rUseMagnet();
        delay(1000);
        rGoToHover2();
        rGoToHover1();
        rGoToPosition1();
        rUseMagnet();
        delay(1000);
        rGoToHover1();


        break;


      case 'f':  //movement disc from 2 to 3. this is h2-p2-h2-h3-p3-h3

        rGoToHover2();
        rGoToPosition2();
        rUseMagnet();
        delay(1000);
        rGoToHover2();
        rGoToHover3();
        rGoToPosition3();
        rUseMagnet();
        delay(1000);
        rGoToHover3();

        break;

      case 'g':  //movement disc from 1 to 3. this is h1-p1-h1-h3-p3-h3

        rGoToHover1();
        rGoToPosition1();
        rUseMagnet();
        delay(2000);
        rGoToHover1();
        rGoToHover3();
        rGoToPosition3();
        rUseMagnet();
        delay(1000);
        rGoToHover3();


        break;

      case 'R':  // Rest. Send the robot arm to the rest position. h0 - p0

        rGoToHover0();
        rGoToPosition0();
        digitalWrite(rMagnetPin, LOW);

        rMagnetInUse = 0;
        robotStarted = false;


        digitalWrite(3, HIGH);  // DEBUGGING

        break;

      default:
        break;
    }
  }
}

//------------- CUSTOM FUNCTION DEFINITIONS--------------

void startRobot() {
  // Implement your robot startup logic here
  robotStarted = true;
  // Add any necessary actions to start the robot

  // Add any additional logic or commands needed when the robot starts

  return;  // Exit the function to prevent further execution in the loop
}


void rGoToHover0() {

  rshoulder.write(110);
  rclavi.write(120);
  delay(1000);
  rrotate.write(80);
  rbicep.write(130);
  delay(2000);
}


void rGoToHover1() {

  rshoulder.write(120);
  rrotate.write(40);
  delay(2000);
  rclavi.write(120);
  delay(1000);
  rbicep.write(135);
  delay(1000);
}

void rGoToHover2() {

  rshoulder.write(120);
  rclavi.write(97);
  rbicep.write(120);
  delay(2000);
  rrotate.write(25);
  delay(2000);
}

void rGoToHover3() {

  rshoulder.write(120);
  rclavi.write(95);
  rbicep.write(135);
  delay(2000);
  rrotate.write(10);
  delay(2000);
}


void rGoToPosition0() {

  rrotate.write(80);
  rshoulder.write(60);
  rbicep.write(110);
  rclavi.write(110);
}


void rGoToPosition1() {
  rrotate.write(20);
  delay(2000);
  rshoulder.write(90);
  delay(3000);
}

void rGoToPosition2() {

  rclavi.write(97);
  rrotate.write(25);
  delay(1000);
  rshoulder.write(95);
  delay(3000);
}

void rGoToPosition3() {

  rrotate.write(10);
  delay(2000);
  rshoulder.write(93);
  delay(3000);
}

void rUseMagnet() {

  if (rMagnetInUse == 0) {
    digitalWrite(rMagnetPin, HIGH);
    // digitalWrite(33, HIGH);
    rMagnetInUse = 1;
    Serial.println("magnets on");

  } else {
    digitalWrite(rMagnetPin, LOW);
    //digitalWrite(33, LOW);
    rMagnetInUse = 0;
    Serial.println("magnets off");
  }
}

//------------- END OF CUSTOM FUNCTION DEFINITIONS--------------
