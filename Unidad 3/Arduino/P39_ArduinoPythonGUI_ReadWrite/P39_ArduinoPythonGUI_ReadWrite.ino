int v;
int sensor = A0;
int led=13;
void setup() {
  pinMode(led,OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(100);

}

void loop() {
  v=analogRead(sensor);
  Serial.println("V. Sensor:"+String(v));
  
  if(Serial.available()>0){
    v=Serial.readString().toInt();
    digitalWrite(led,v);
  }
  delay(100);

}
