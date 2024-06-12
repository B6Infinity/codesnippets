#include <ESP8266WiFi.h>

void setup() {
  // put your setup code here, to run once:
  pinMode(LED_BUILTIN, OUTPUT); digitalWrite(LED_BUILTIN, HIGH);
  Serial.begin(115200);

  WiFi.persistent(false);

  digitalWrite(LED_BUILTIN, LOW); delay(500); digitalWrite(LED_BUILTIN, HIGH); delay(500); // Blink
  digitalWrite(LED_BUILTIN, LOW); delay(500); digitalWrite(LED_BUILTIN, HIGH); delay(500); // Blink
  digitalWrite(LED_BUILTIN, LOW); delay(500); digitalWrite(LED_BUILTIN, HIGH); delay(2000); // Blink
  Serial.println("Startin wifi...");
  WiFi.softAP("DigiDent", "digident");
  Serial.println("WiFi started");
  digitalWrite(LED_BUILTIN, LOW); delay(500); digitalWrite(LED_BUILTIN, HIGH); // Blink
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(LED_BUILTIN, HIGH);
  delay(3000);
  digitalWrite(LED_BUILTIN, LOW); delay(100); digitalWrite(LED_BUILTIN, HIGH); delay(100); digitalWrite(LED_BUILTIN, LOW); delay(100); digitalWrite(LED_BUILTIN, HIGH); delay(100); digitalWrite(LED_BUILTIN, LOW); delay(100); 
  Serial.print("PING...");
}
