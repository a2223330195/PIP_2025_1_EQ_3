int pot =A0;
int led1 =8;


void setup() {
  // put your setup code here, to run once:
}

void loop() {
 int v=analogRead(pot);
  v=v/4;

  analogWrite(led1,v);
 
  delay(10);
}
 
