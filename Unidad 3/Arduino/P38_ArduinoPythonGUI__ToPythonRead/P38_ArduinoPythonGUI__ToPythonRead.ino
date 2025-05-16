int v;
int sensor = A0;
void setup() {
  Serial.begin(9600);

}

void loop() {
  v=analogRead(sensor);
  Serial.println("V. Seonsor:"+String(v));
  delay(100);

}
