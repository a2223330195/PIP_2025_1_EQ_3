int led =6;
void setup() {
  // put your setup code here, to run once:
}

void loop() {
 
 for(int i=0;i<255;i++)
 {
  analogWrite(led,i);
  delay(10);

 }
for(int i=255;i>0;i--)
 {
  analogWrite(led,i);
  delay(10);

 }
}
