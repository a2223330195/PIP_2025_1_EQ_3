void setup() {
  Serial.begin(9600);
}
byte valor=0;
void loop() {

  Serial.println(valor);
  valor+=1;
  delay(100);
}
