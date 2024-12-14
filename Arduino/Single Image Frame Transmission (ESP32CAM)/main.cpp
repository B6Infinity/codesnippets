#include <Arduino.h>
#include "esp_camera.h"
#include "camera_pins.h"

#define CAMERA_MODEL_AI_THINKER

#define LED_BUILTIN 33 // Define LED_BUILTIN for ESP32

void setup()
{
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(115200);
    delay(500);

    Serial.println("Camera initialising...");

    camera_config_t config;

    // Declaring pins in the config
    {

        config.ledc_channel = LEDC_CHANNEL_0;
        config.ledc_timer = LEDC_TIMER_0;

        config.pin_d0 = Y2_GPIO_NUM;
        config.pin_d1 = Y3_GPIO_NUM;
        config.pin_d2 = Y4_GPIO_NUM;
        config.pin_d3 = Y5_GPIO_NUM;
        config.pin_d4 = Y6_GPIO_NUM;
        config.pin_d5 = Y7_GPIO_NUM;
        config.pin_d6 = Y8_GPIO_NUM;
        config.pin_d7 = Y9_GPIO_NUM;
        config.pin_xclk = XCLK_GPIO_NUM;
        config.pin_pclk = PCLK_GPIO_NUM;
        config.pin_vsync = VSYNC_GPIO_NUM;
        config.pin_href = HREF_GPIO_NUM;
        config.pin_sccb_sda = SIOD_GPIO_NUM; // Replaced `sscb` with `sccb`
        config.pin_sccb_scl = SIOC_GPIO_NUM; // Replaced `sscb` with `sccb`
        config.pin_pwdn = PWDN_GPIO_NUM;
        config.pin_reset = RESET_GPIO_NUM;
        config.xclk_freq_hz = 20000000; // Can be set to 10000000 for slower refresh rate but could lead to stable (slower) execution
        config.pixel_format = PIXFORMAT_JPEG;
    }

    // Initialize the camera
    if (psramFound())
    {
        Serial.println("PSRAM FOUND! Setting framesize to QVGA");
        // config.frame_size = FRAMESIZE_QVGA; // 320x240 resolution
        config.frame_size = FRAMESIZE_VGA; // 640x480 resolution
        config.jpeg_quality = 5;
        config.fb_count = 2;
    }
    else
    {
        Serial.println("PSRAM NOT FOUND! Setting framsize to CIF");
        config.frame_size = FRAMESIZE_CIF;
        config.jpeg_quality = 20; // not 12 (0-63; lower means high quality)
        config.fb_count = 1;
    }

    esp_err_t err = esp_camera_init(&config);

    if (err != ESP_OK)
    {
        Serial.printf("Camera init failed with error 0x%x\n", err);
        return;
    }

    Serial.println("Camera initialized successfully!");
}

/*
typedef struct  {
    uint8_t *buf;   // Pointer to the image data (raw bytes)
    size_t len;     // Length of the image data (size in bytes)
    size_t width;   // Width of the image (in pixels)
    size_t height;  // Height of the image (in pixels)
    pixformat_t format; // Pixel format of the image (e.g., JPEG, RGB565, etc.)
    int64_t timestamp;  // Timestamp of when the frame was captured
} camera_fb_t;
*/

void loop()
{

    if (Serial.available())
    {
        String rcvdTxt = Serial.readString();

        if (rcvdTxt == "CAP")
        {
            // Capturing image
            camera_fb_t *fb = esp_camera_fb_get();
            if (!fb)
            {
                Serial.println("FAILED!");
            }
            else
            {
                Serial.println(fb->len); // Send the length
                Serial.write(fb->buf, fb->len);

                esp_camera_fb_return(fb);
            }
        }
        else
        {
            Serial.print("I heard: ");
            Serial.println(rcvdTxt);
        }

        digitalWrite(LED_BUILTIN, HIGH);
        delay(1000);
        digitalWrite(LED_BUILTIN, LOW);
    }
}


