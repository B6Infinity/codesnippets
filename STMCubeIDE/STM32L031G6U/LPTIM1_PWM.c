/*
-----------PLEASE REMOVE THIS COMMENT CHUNK BEFORE PLACING IT IN THE CUBEIDE-----------
In the IOC file:
1. Go to Timers > LPTIM1:
2. Mode: Count internal clock events
  2. a. Enable Waveform Generation
3. Configuration: Configure the "Clock Prescaler" and "Output" as necessary.

*/

... 

int main(void)
{
  uint32_t period = 33; // ARR
  uint32_t pulse  = 24;   // CMP (0.8 * 30000 duty)

  // f_PWM = f_SYSTEM / Ticks Per Cycle
  
  HAL_LPTIM_PWM_Start(&hlptim1, period, pulse);

  ...

  while (1)
  {
    
  }
}
