#include <Servo.h>

int Input_sensor = A7;
int prev_feedback;
int Direction = 52;
byte gear_select;
int gear;

void gearSelect(int gearState);

Servo Actuator;

void setup() {
  // put your setup code here, to run once:
  pinMode(Direction, OUTPUT);
  Serial.begin(9600);

  Actuator.attach(50);

}

void loop() {
  // put your main code here, to run repeatedly
  if (Serial.available() > 0) 
  {
    // read the incoming byte:
    gear = Serial.read();
    gearSelect(gear);
  }
  
  //moveActuator(700);
  
}

void moveActuator(int newpos) {
  int oldpos = analogRead(Input_sensor);

  Serial.print("Input sensor Position: ");
  Serial.println(oldpos);
  
  if (oldpos  > newpos ) 
  {
    Serial.print(" oldpos > newpos ");
    Actuator.write(180);
    digitalWrite(Direction, HIGH);
  } 
  else if (newpos   > oldpos) 
  {
    Serial.print(" newpos > oldpos ");

    digitalWrite(Direction, LOW);
    Actuator.write(180);
  }
}


void gearSelect(int gearState)
{
  switch (gearState) 
  {
    case 1:
      //Parking
      moveActuator(700);
      break;
    case 2:
      //Reverse
      moveActuator(535);
      break;
    case 3:
      //Neutral
      moveActuator(477);
      break;
    case 4:
      //Drive
      moveActuator(425);
    default:
      // statements
      return;
   }
}


