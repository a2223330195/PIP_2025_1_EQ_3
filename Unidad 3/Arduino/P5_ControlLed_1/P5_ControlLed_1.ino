int led =5;
void setup() {
  pinMode(led,OUTPUT);
}
void loop() {
  digitalWrite(led,1);
  delay(100);
  digitalWrite(led,0);
  

}
