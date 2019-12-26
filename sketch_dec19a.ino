void setup() {
  // put your setup code here, to run once:
  
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  float vibrationSensor = analogRead(A0);
  float soundSensor = analogRead(A1);
  float switchVibrationSensor = analogRead(A2);
  String result = ""; 
  result = "(" + (String)vibrationSensor + "," + (String)soundSensor +","+ (String)switchVibrationSensor + ")";
  Serial.println(result);
  delay(2000);
  }
