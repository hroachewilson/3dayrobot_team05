//#include <Servo.h>

int Input_sensor = A0;
int prev_feedback;
int Direction = 2;
bool brake_state = 1;
int braking_pin = 11;

void braking(bool brake_state);

//Servo Actuator;

void setup() {
  // put your setup code here, to run once:
  pinMode(Direction, OUTPUT);
  pinMode(braking_pin, OUTPUT);

  
  Serial.begin(9600);

  //Actuator.attach(48);
}

void loop() {
  // put your main code here, to run repeatedly
  moveActuator(0);
  
  if (Serial.available() > 0) 
  {
    // read the incoming byte:
    brake_state = Serial.read();
    braking(brake_state);
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
    //Actuator.write(1023);
    digitalWrite(Direction, HIGH);
    analogWrite(braking_pin, 1023);
  } 
  else if (newpos   > oldpos) 
  {
    Serial.print(" newpos > oldpos ");

    digitalWrite(Direction, LOW);
    //Actuator.write(1023);
    analogWrite(braking_pin, 1023);
  }
}


void braking(bool brakeState)
{
  switch (brakeState) 
  {
    case 1:
      //Braking
      moveActuator(1023);
      break;
    case 0:
      //No Braking
      moveActuator(0);
      break;
    default:
      // statements
      return;
   }
}


