Código fuente Laboratorio # 5 STM32/Arduino: GPIO, Giroscopio, comunicaciones, TinyML

Se desarrolla un HAR (Human Activity Recognition) empleando la biblioteca de Tensorflow, a través de la plataforma
Edge Impulse. El modelo es capas de detectar si sé ha realizado un movimiento de arriba a abajo, estacionario o golpe frontal, dependiendo de las lecturas del Giroscopio implementado por el Arduino Nano 33 Ble Sense Lite.

Como Hardware se utiliza una laptop para la captura de los datos.
Se emplea el Giroscopio LSM9DS1 IMU, presente en la tarjeta Arduino Nano 33 Ble Sense Lite

La carpete captura_datos_movimiento_giroscopio, contiene el código encargado de realizar la captura de las lecturas
del Giroscopio para el entrenamiento del modelo de encargado de reconocer el tipo de movimiento.

La carpeta test_detector_tipo_movimiento_continuo, contine el código para las pruebas del modelo creado, que es
probado en la tarjeta Arduino Nano 33 Ble Sense Lite.

La biblioteca con el modelo generado se encuentra en el archivo ei-lab5_har-arduino-1.0.1.zip, se debe agregar al IDE
de Arduino para poder ser utilizado.
