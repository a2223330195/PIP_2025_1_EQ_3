String resp;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0)
  {
    resp=Serial.readString();
    Serial.println(resp);

  }
delay(100);
}
