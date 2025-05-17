int ldrPin = A0;
int ledPins[] = {3, 4, 5, 6}; // Pines conectados a los LEDs

void setup() {
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  Serial.begin(9600);
}

void loop() {
  int ldrValue = analogRead(ldrPin);
  Serial.println(ldrValue); // Para observar el valor de la luz

  // Apaga todos los LEDs
  for (int i = 0; i < 4; i++) {
    digitalWrite(ledPins[i], LOW);
  }

  // Enciende LEDs según nivel de oscuridad
  if (ldrValue < 700) digitalWrite(ledPins[0], HIGH);
  if (ldrValue < 500) digitalWrite(ledPins[1], HIGH);
  if (ldrValue < 300) digitalWrite(ledPins[2], HIGH);
  if (ldrValue < 200) digitalWrite(ledPins[3], HIGH);

  delay(100);
}