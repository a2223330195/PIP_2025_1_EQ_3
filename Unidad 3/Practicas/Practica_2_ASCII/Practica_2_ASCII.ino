void setup() {
  for (int i = 5; i <= 12; i++) {
    pinMode(i, OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100);
}

void db(int num) {
  int b[8];
  if (num == 0) {
    for (int i = 0; i < 8; i++) {
      digitalWrite(5 + i, LOW);
    }
    return;
  }
  int i = 0;
  while (num > 0 && i < 8) {
    b[i] = num % 2;
    num = num / 2;
    i++;
  }
  while (i < 8) {
    b[i] = 0;
    i++;
  }
  for (int j = 0; j < 8; j++) {
    digitalWrite(5 + j, b[j]);
  }

  delay(5000);

  

  for (int i = 0; i < 8; i++) {
    digitalWrite(5 + i, LOW);
  }
}

String upperCamelCase(String palabra) {
  if (palabra.length() == 0) {
    return "";
  }
  palabra.toUpperCase(); 
  palabra.setCharAt(0, toupper(palabra.charAt(0)));
  return palabra;
}

void loop() {
  if (Serial.available() > 0) {
    String palabra = Serial.readString();
    palabra.trim();

    if (palabra.length() <= 5) {
      palabra = upperCamelCase(palabra);
      for (int i = 0; i < palabra.length(); i++) {
        int valorASCII = (int)palabra.charAt(i);
        Serial.print(palabra.charAt(i));
        Serial.print(" ASCII: ");
        Serial.print(valorASCII);
        Serial.print(" Binario: ");
        db(valorASCII);
        Serial.println();
      }
    } else {
      Serial.println("Palabra demasiado larga (máximo 5 letras).");
    }
  }
}