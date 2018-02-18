void setup() {
  Serial.begin(9600);
}

void loop() 
{
  String data=Serial.readStringUntil('\n');
  if(data=="\n"){return;}
  Serial.print(data);
}
