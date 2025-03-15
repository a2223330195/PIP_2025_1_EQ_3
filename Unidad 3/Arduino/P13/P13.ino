int pot = A0;
int led1 = 5;
int led2 = 6;
int led3 = 7;
int led4 = 8;

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(led4, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10);
}

void loop() {
  int valorSensor = analogRead(pot);
  int valorMapeado = map(valorSensor, 0, 1023, 0, 1000); 

  Serial.print("Valor Mapeado: ");
  Serial.println(valorMapeado);

  if (valorMapeado <= 250) {
    digitalWrite(led1, 1);
    digitalWrite(led2, 0);
    digitalWrite(led3, 0);
    digitalWrite(led4, 0);
  } else if (valorMapeado <= 500) {
    digitalWrite(led1, 0);
    digitalWrite(led2, 1);
    digitalWrite(led3, 0);
    digitalWrite(led4, 0);
  } else if (valorMapeado <= 750) {
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
    digitalWrite(led3, 1);
    digitalWrite(led4, 0);
  } else {
    digitalWrite(led1, 0);
    digitalWrite(led2, 0);
    digitalWrite(led3, 0);
    digitalWrite(led4, 1);
  }
  delay(100);
}