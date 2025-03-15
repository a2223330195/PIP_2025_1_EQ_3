String resp;
void setup() {
  // put your setup code here, to run once:
  Serial.being(9600);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(Serial.avaible()>0){
    resp= Serial.readString();
    Serial.println(resp);
  }
  delay(100);

}
