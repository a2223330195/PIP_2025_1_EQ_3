void setup() {
  Serial.begin(9600);
}
byte v=0;
void loop() {

  Serial.println("valor "+String(v));
  v+=1;
  delay(250);
}
