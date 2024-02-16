/*
 * Código empleado en la captura de las lecturas del giroscopio (unidad grados/segundo).
 */

#include <Arduino_LSM9DS1.h>

// Settings
#define LED_R_PIN           22        // Estable RGB en rojo

void setup() {

  //Habilita LED RGB en
  pinMode(LED_R_PIN, OUTPUT);
  digitalWrite(LED_R_PIN, HIGH);

  // Transmisión serial
  Serial.begin(115200);

  // Inicialización del giroscopio
  if (!IMU.begin()) {
    Serial.println("Failed to initialize IMU!");
    while (1);
  }
}

void loop() {

  float gyr_x;
  float gyr_y;
  float gyr_z;
  unsigned long timestamp;
  unsigned long start_timestamp;

  // LED  RGB
  pinMode(LED_R_PIN, OUTPUT);
  digitalWrite(LED_R_PIN, LOW);

  // Medición tiempo
  start_timestamp = millis();

  //Ciclo infinito lectura y transmisión por puerto serial
  //del giroscopio
  while(1){

    timestamp = millis();

    //Lectura giroscopio (grados/seg)
    IMU.readGyroscope(gyr_x, gyr_y, gyr_z);

    //Transmite unidad tiempo de la captura
    Serial.print(timestamp - start_timestamp, 3);
    Serial.print(" ");
    //Transmite eje x
    Serial.print(gyr_x, 3);
    Serial.print(" ");
    //Transmite eje y
    Serial.print(gyr_y, 3);
    Serial.print(" ");
    //Transmite eje z
    Serial.println(gyr_z, 3);

  }

  digitalWrite(LED_R_PIN, HIGH);

}
