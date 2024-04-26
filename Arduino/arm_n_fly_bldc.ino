#include <Servo.h>

#define ESC_PIN D4

Servo esc;

void setup() 
{
  esc.attach(ESC_PIN,  1000, 2000);
  esc.write(180);
  delay(5000);
  esc.write(0);
  delay(2000);

  //FLY
  esc.write(180);  
}

void loop() 
{
}
