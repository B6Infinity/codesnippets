/*
Author: B6Infinity
This code is meant for `DEVICE=stm32f103c8`.
Originally targetted for the STM based Blue Pill.

If a Voltage above 1.5V is detected on the PA0 pin of the Blue Pill, the built in LED of the Bluepill blinks rapidly.
If below 1.5V, it blinks at a slower rate. 
*/

#include <libopencm3/stm32/rcc.h>
#include <libopencm3/stm32/gpio.h>
#include <libopencm3/stm32/adc.h>
#include <libopencm3/cm3/systick.h>

#define THRESHOLD 1861   // ~1.5V for 12-bit ADC @ 3.3V
#define LED_PORT GPIOC
#define LED_PIN  GPIO13

static void clock_setup(void) {
    rcc_clock_setup_in_hse_8mhz_out_72mhz();
    
	rcc_periph_clock_enable(RCC_GPIOC); // LED Port C

    rcc_periph_clock_enable(RCC_ADC1);  // ADC1 machine
    rcc_periph_clock_enable(RCC_GPIOA); // ADC input pin PA0
}

static void gpio_setup(void) {
    // LED on PC13
    gpio_set_mode(LED_PORT, GPIO_MODE_OUTPUT_2_MHZ,
                  GPIO_CNF_OUTPUT_PUSHPULL, LED_PIN);

    // ADC input on PA0
    gpio_set_mode(GPIOA, GPIO_MODE_INPUT, GPIO_CNF_INPUT_ANALOG, GPIO0);
}

static void adc_setup(void) {
    adc_power_off(ADC1); // Turn off the machine

    adc_disable_scan_mode(ADC1); // Dont need to scan every ADC Channel
    adc_set_single_conversion_mode(ADC1); // 1 measurement everytime we ask
    adc_set_sample_time(ADC1, ADC_CHANNEL0, ADC_SMPR_SMP_239DOT5CYC); // Sample time

    adc_power_on(ADC1); // Turn on the machine

    adc_reset_calibration(ADC1);
    adc_calibrate(ADC1); // Calibration sequence
}

static uint16_t read_adc(uint8_t channel) {
    adc_set_regular_sequence(ADC1, 1, &channel);
    adc_start_conversion_direct(ADC1);
    while (!adc_eoc(ADC1));
    return adc_read_regular(ADC1);
}

// crude delay function (~ms)
static void delay_ms(uint32_t ms) {
    for (uint32_t i = 0; i < ms * 8000; i++) {
        __asm__("nop");
    }
}

int main(void) {
    clock_setup();
    gpio_setup();
    adc_setup();

    while (1) {
        uint16_t val = read_adc(ADC_CHANNEL0);

        if (val < THRESHOLD) {
            // Voltage < 1.5V → blink 500ms
            gpio_toggle(LED_PORT, LED_PIN);
            delay_ms(1000);
        } else {
            // Voltage >= 1.5V → blink 100ms
            gpio_toggle(LED_PORT, LED_PIN);
            delay_ms(500);
        }
    }
}
