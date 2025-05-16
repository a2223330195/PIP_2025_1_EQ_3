#include <IRremote.h>

const int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;

// Pines para LEDs
const int led1 = 5;
const int led2 = 6;
const int led3 = 7;
const int ledExtra = 2; // LED que se enciende cuando detecta objeto

// Buzzer
const int buzzerPin = 8;
bool buzzerState = false;

// Sensor ultrasónico
const int trigPin = 12;
const int echoPin = 13;

// Potenciómetro y motor (ventilador)
const int Potenciometro = A0;
const int MotorPWM = 9;

String modo = "AUTO";  // "MANUAL" o "AUTO"
int pwmManual = 0;

void setup() {
  Serial.begin(9600);
  irrecv.enableIRIn();

  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  pinMode(ledExtra, OUTPUT);
  pinMode(buzzerPin, OUTPUT);
  pinMode(MotorPWM, OUTPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
  digitalWrite(ledExtra, LOW);
  digitalWrite(buzzerPin, LOW);
  digitalWrite(MotorPWM, LOW);
}

void loop() {
  // IR remoto físico
  if (irrecv.decode(&results)) {
    unsigned long code = results.value;
    Serial.print("Código IR recibido: ");
    Serial.println(code, HEX);
    manejarCodigo(code);
    irrecv.resume();
  }

  // Lectura desde Python por Serial
  if (Serial.available()) {
    String comando = Serial.readStringUntil('\n');
    comando.trim();

    if (comando == "MANUAL") {
      modo = "MANUAL";
    } else if (comando == "AUTO") {
      modo = "AUTO";
    } else if (comando.length() == 8 && comando.startsWith("20DF")) {
      // Código IR enviado desde Python
      unsigned long code = strtoul(comando.c_str(), NULL, 16);
      manejarCodigo(code);
    } else {
      // Si es número, lo usamos como PWM
      pwmManual = comando.toInt();
    }
  }

  // Sensor ultrasónico
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duracion = pulseIn(echoPin, HIGH);
  float distancia = duracion * 0.034 / 2;

  Serial.print("Distancia: ");
  Serial.print(distancia);
  Serial.println(" cm");

  if (buzzerState && distancia <= 3) {
    digitalWrite(buzzerPin, HIGH);
    digitalWrite(ledExtra, HIGH);
    Serial.println("ALARMA: Objeto cercano (<30cm)");
  } else {
    digitalWrite(buzzerPin, LOW);
    digitalWrite(ledExtra, LOW);
  }

  // Control del ventilador
  if (modo == "MANUAL") {
    int valorPOT = analogRead(Potenciometro);
    int valorPWM = map(valorPOT, 0, 1023, 0, 255);
    analogWrite(MotorPWM, valorPWM);
    Serial.print("Potenciómetro: ");
    Serial.print(valorPOT);
    Serial.print(" | PWM Ventilador (LED): ");
    Serial.println(valorPWM);
  } else {
    analogWrite(MotorPWM, pwmManual);
  }

  delay(200);
}

void manejarCodigo(unsigned long code) {
  if (code == 0x20DF8877) {
    digitalWrite(led1, HIGH);
    Serial.println("LED1 ENCENDIDO");
  } else if (code == 0x20DF48B7) {
    digitalWrite(led2, HIGH);
    Serial.println("LED2 ENCENDIDO");
  } else if (code == 0x20DFC837) {
    digitalWrite(led3, HIGH);
    Serial.println("LED3 ENCENDIDO");
  } else if (code == 0x20DF08F7) {
    digitalWrite(led1, LOW);
    digitalWrite(led2, LOW);
    digitalWrite(led3, LOW);
    Serial.println("TODOS LOS LEDS APAGADOS");
  } else if (code == 0x20DF906F) {
    buzzerState = !buzzerState;
    Serial.println(buzzerState ? "BUZZER ACTIVADO" : "BUZZER DESACTIVADO");
    if (!buzzerState) {
      digitalWrite(buzzerPin, LOW);
      digitalWrite(ledExtra, LOW);
    }
  } else {
    Serial.println("Código NO reconocido");
  }
}
