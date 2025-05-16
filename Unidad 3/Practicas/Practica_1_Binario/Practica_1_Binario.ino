void setup() {
  for (int i = 5; i <= 12; i++) {
    pinMode(i, OUTPUT);
  }
  Serial.begin(9600);
  Serial.setTimeout(100); 
}
int valor;
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
    i++;}
  for (int j = 0; j < 8; j++) {
    digitalWrite(5 + j, b[j]);}
    
  
  delay(4500);
  
  for (int i = 0; i < 8; i++) {
      digitalWrite(5 + i, LOW); 
    }

  }
void loop() {
  if (Serial.available() > 0) {
    valor = Serial.readString().toInt();
    valor = constrain(valor, 0, 255);
    Serial.println(valor);
    db(valor);
    

     }}