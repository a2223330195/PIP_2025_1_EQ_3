int pot = A0;
int led1 = 3;
int led2 = 4;
int led3 = 5;
int led4 = 6;
int led5= 7;
int led6 = 8;
int led7 = 9;
int led8 = 10;
void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  pinMode(led5, OUTPUT);
  pinMode(led6, OUTPUT);
  pinMode(led7, OUTPUT);
  pinMode(led8, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}
void loop() {
  int valorSensor = analogRead(pot);
  int valorMapeado = map(valorSensor, 0, 1023, 0, 255); 
  printf(valorSensor);
  Serial.print(valorSensor);
  Serial.print("Decimal: ");
  Serial.print(valorMapeado);
  digitalWrite(led1, (valorMapeado >> 0) & 1);
  digitalWrite(led2, (valorMapeado >> 1) & 1);
  digitalWrite(led3, (valorMapeado >> 2) & 1);
  digitalWrite(led4, (valorMapeado >> 3) & 1);
  digitalWrite(led5, (valorMapeado >> 4) & 1);
  digitalWrite(led6, (valorMapeado >> 5) & 1);
  digitalWrite(led7, (valorMapeado >> 6) & 1);
  digitalWrite(led8, (valorMapeado >> 7) & 1);
  delay(100);
}