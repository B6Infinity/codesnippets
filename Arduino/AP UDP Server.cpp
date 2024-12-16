#include <Arduino.h>
#include "WiFi.h" // Include the Wi-Fi libraries
#include "WiFiUdp.h"


#define LED_BUILTIN 33 // Define LED_BUILTIN for ESP32

// Wi-Fi AP credentials
const char *ssid = "YOUR_SSID_HERE";
const char *password = "PASSWORD123";

// Set up UDP
WiFiUDP udp;
unsigned int localUdpPort = 12345; // Local port to listen on
char incomingPacket[255];          // Buffer for incoming UDP packets
char replyPacket[] = "I heard: ";  // Response to be sent back



// Util Funcs

void lightLog(int times, int delay_ms = 100)
{
    // Assuming the LED_BUILTIN is always on, flashes the LED off for taken values

    for (int i = 0; i < times; i++)
    {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(delay_ms);
        digitalWrite(LED_BUILTIN, LOW);
        delay(delay_ms);
    }
}

///////////////////////


void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(115200);
    delay(200);

    Serial.println("Setting up Access Point (AP)...");
    WiFi.mode(WIFI_AP);
    WiFi.softAP(ssid, password);
    delay(800);
    Serial.println(WiFi.softAPIP());
    lightLog(3);

    udp.begin(localUdpPort);
    Serial.printf("Listening on UDP port %d\n", localUdpPort);
}

void loop()
{
    int packetSize = udp.parsePacket(); // Check if there’s data to read
    if (packetSize)
    {
        // Read incoming packet...
        int len = udp.read(incomingPacket, 255);
        if (len > 0)
        {
            incomingPacket[len] = 0; // Null-terminate the string
        }
        // Print the received message
        Serial.printf("Received %d bytes from %s, port %d: %s\n",
                      len,
                      udp.remoteIP().toString().c_str(),
                      udp.remotePort(),
                      incomingPacket);

        // Send a response (echo)
        String response = String(replyPacket) + String(incomingPacket);
        udp.beginPacket(udp.remoteIP(), udp.remotePort());
        udp.write((const uint8_t*)response.c_str(), response.length());
        udp.endPacket();

        Serial.println("Reply sent!");
    }
}
