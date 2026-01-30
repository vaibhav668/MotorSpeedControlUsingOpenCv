int enA = 9;
int in1 = 8;
int in2 = 7;

void setup() {
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  Serial.begin(9600);
}

void loop() {
  if (Serial.available()) {
    int speed = Serial.parseInt();
    speed = constrain(speed, 0, 255);
    analogWrite(enA, speed);
  }
}
