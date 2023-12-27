void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(7, OUTPUT);
  digitalWrite(7, HIGH);
  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);
  pinMode(5, OUTPUT);
  digitalWrite(5, HIGH);
  digitalWrite(13, LOW);

}

void loop() {
  // put your main code here, to run repeatedly:
  int PhaseShift = analogRead(A0);
  int PowerDiff = analogRead(A5);


  float PSVolt = PhaseShift * (5.0 / 1023.0);
  float PDVolt = PowerDiff * (5.0 / 1023.0);

  Serial.print(PSVolt);
  Serial.print(";");
  Serial.println(PDVolt);
  delay(1000);
}
