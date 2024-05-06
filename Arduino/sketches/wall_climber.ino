#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <ESPAsyncTCP.h>
#include <ESPAsyncWebServer.h>
#include <Servo.h>

#define ESC_PIN D4
Servo esc;

const char* ssid     = "Wall-Climber";
const char* password = "12348765";

void moveW();
void moveA();
void moveS();
void moveD();
void move0();
void bldcON();
void bldcOFF();

const int inp1 = D8;
const int inp2 = D7;
const int inp3 = D5;
const int inp4 = D3;

// Create AsyncWebServer object on port 80
AsyncWebServer server(80);

// Generally, you should use "unsigned long" for variables that hold time
// The value will quickly become too large for an int to store
unsigned long previousMillis = 0;    // will store last time DHT was updated


const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Window Cleaning Bot</title>
    <style>
        .container {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        button {
            padding: 10px 20px;
            font-size: 20px;
            margin: 0 10px;
            cursor: pointer;
            width: 150px;
            height: 50px;
        }
    </style>
</head>
<body>
    <div class="container">
        <p><button onclick="window.location.href='/move0'">STOP</button></p>
        <p><button onclick="window.location.href='/moveW'">UP</button></p>
        <p><button onclick="window.location.href='/moveS'">DOWN</button></p>
        <p><button onclick="window.location.href='/moveD'">RIGHT</button></p>
        <p><button onclick="window.location.href='/bldcON'">BLDC ON</button></p>
        <p><button onclick="window.location.href='/bldcOFF'">BLDC OFF</button></p>
    </div>
</body>
</html>)rawliteral";

void setup(){

  pinMode(inp1, OUTPUT);
  pinMode(inp2, OUTPUT);
  pinMode(inp3, OUTPUT);
  pinMode(inp4, OUTPUT);

  // Serial port for debugging purposes
  Serial.begin(115200);

  
  Serial.print("Setting AP (Access Point)…");
  // Remove the password parameter, if you want the AP (Access Point) to be open
  WiFi.softAP(ssid, password);

  IPAddress IP = WiFi.softAPIP();
  Serial.print("AP IP address: ");
  Serial.println(IP);

  // Print ESP8266 Local IP Address
  Serial.println(WiFi.localIP());

  
  //Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/html", index_html);
  });

  server.on("/moveW", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("W");
    moveW();
    request->redirect("/");
  });
  server.on("/moveA", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("A");
    moveA();
    request->redirect("/");
  });
  server.on("/moveS", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("S");
    moveS();
    request->redirect("/");
  });
  server.on("/moveD", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("D");
    moveD();
    request->redirect("/");
  });
  server.on("/move0", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("0");
    move0();
    request->redirect("/");
  });
  server.on("/bldcON", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("(");
    bldcON();
    request->redirect("/");
  });
  server.on("/bldcOFF", HTTP_GET, [] (AsyncWebServerRequest *request) {
    Serial.print("(");
    bldcOFF();
    request->redirect("/");
  });

  // Start server
  server.begin();

  //bldc
  esc.attach(ESC_PIN,  1000, 2000);
  esc.write(180);
  delay(5000);
  esc.write(0);
  delay(2000);
  for (int i = 0; i<= 180; i++) {
    esc.write(i);
    delay(200);
  }
  delay(2000);
  esc.write(0);

}
 
void loop(){  
  
}

void bldcON(){
  for (int i = 0; i<= 180; i++) {
    esc.write(i);
    delay(200);
  }
}
void bldcOFF(){
  delay(200);
  esc.write(0);
  delay(500);
}

void moveW(){
	digitalWrite(inp1, HIGH);
  digitalWrite(inp2, LOW);
	digitalWrite(inp3, HIGH);
  digitalWrite(inp4, LOW);
}
void move0(){
	digitalWrite(inp1, LOW);
  digitalWrite(inp2, LOW);
	digitalWrite(inp3, LOW);
  digitalWrite(inp4, LOW);
}
void moveA(){ // Left
	digitalWrite(inp1, HIGH);
  digitalWrite(inp2, LOW);
	digitalWrite(inp3, LOW);
  digitalWrite(inp4, HIGH);
}
void moveD(){ // Left
	digitalWrite(inp1, LOW);
  digitalWrite(inp2, HIGH);
	digitalWrite(inp3, HIGH);
  digitalWrite(inp4, LOW);
}
void moveS(){ // Left
	digitalWrite(inp1, LOW);
  digitalWrite(inp2, HIGH);
	digitalWrite(inp3, LOW);
  digitalWrite(inp4, HIGH);
}
