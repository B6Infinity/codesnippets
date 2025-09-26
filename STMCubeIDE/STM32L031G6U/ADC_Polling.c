/*
-----------PLEASE REMOVE THIS COMMENT CHUNK BEFORE PLACING IT IN THE CUBEIDE-----------
In the IOC file:
0. Select the Pin (PA4)
1. Go to Analog > ADC > Parameter Settings:
*/


	  if (HAL_ADC_Start(&hadc) != HAL_OK) {
		  // handle error
	  }
	  // Wait for conversion 10ms
	  if (HAL_ADC_PollForConversion(&hadc, 10) == HAL_OK){
		  uint32_t raw = HAL_ADC_GetValue(&hadc); // 0 - 4095 for 12-bit ADC

	  	  /* Convert to millivolts (integer math to avoid float/printf float issues) */
	  	  const uint32_t VREF_mV = 3600U; // change if your VDDA differs
	  	  uint32_t mV = (raw * VREF_mV) / 4095U;

	  	  int len = snprintf(buff, sizeof(buff), "ADC raw=%lu, %lu mV\r\n", (unsigned long)raw, (unsigned long)mV);

	  	  HAL_UART_Transmit(&huart2, (uint8_t*)buff, (uint16_t)len, HAL_MAX_DELAY);
	  }

	  HAL_ADC_Stop(&hadc);
