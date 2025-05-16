int potx = A0;
int poty = A1;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int v1 = analogRead(potx);
  int v2 = analogRead(poty);
  Serial.println(String(v1) + " " + String(v2));
}