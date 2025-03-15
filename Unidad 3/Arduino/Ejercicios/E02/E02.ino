int pot=A0;
int led1=5;
int led2=6;
int led3=7;
int led4=8;
void setup() {
  // put your setup code here, to run once:
  pinMode(led1,OUTPUT);
  pinMode(led2,OUTPUT);
  pinMode(led3,OUTPUT);
  pinMode(led4,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int v=analogRead(pot);
  Serial.println(v);
  if(v>500){
    prenderder();
  }
  else{
    prenderizq();
  }


}
void prenderder()
{
  digitalWrite(led3,1);
  delay(100);
  digitalWrite(led3,0);
  digitalWrite(led4,1);
  delay(100);
  digitalWrite(led4,0);
  digitalWrite(led1,1);
  delay(100);
  digitalWrite(led1,0);
  digitalWrite(led2,1);
  delay(100);
  digitalWrite(led2,0);
}
void prenderizq()
{
  digitalWrite(led2,1);
  delay(100);
  digitalWrite(led2,0);
  digitalWrite(led1,1);
  delay(100);
  digitalWrite(led1,0);
  digitalWrite(led4,1);
  delay(100);
  digitalWrite(led4,0);
  digitalWrite(led3,1);
  delay(100);
  digitalWrite(led3,0);
}

