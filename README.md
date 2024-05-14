# HW Monitor para Windows con Heltec WiFi Kit 8

Este proyecto consiste en un monitor de hardware para sistemas Windows utilizando la placa Heltec WiFi Kit 8 con display OLED. El monitor recopila datos del sistema, como la temperatura de la CPU, el uso de la CPU, la memoria, la temperatura de la GPU, etc., utilizando la biblioteca OpenHardwareMonitor para interactuar con los sensores del sistema en Windows, y los muestra en tiempo real en el display OLED de la placa.

## Requisitos

- Python 3.x
- pySerial
- psutil
- wmi
- Arduino IDE

## Instalación y Uso

1. Clona o descarga este repositorio en tu computadora.
2. Conecta la placa Heltec WiFi Kit 8 a tu computadora mediante USB.

Para el script de Python:

1. Asegúrate de tener los requisitos previos instalados.
2. Abre el archivo `main.py` en un editor de texto y ajusta el puerto serial en la línea `ser = serial.Serial('COM4', 115200)` según corresponda.
3. Ejecuta el script `main.py` desde tu terminal o entorno Python.

Para el sketch de Arduino:

1. Abre el archivo `main.ino` en Arduino IDE y carga el código en la placa Heltec WiFi Kit 8.

## Notas

- Asegúrate de tener los controladores USB instalados correctamente para la placa Heltec WiFi Kit 8.
  https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers

- Este proyecto está diseñado para sistemas Windows y utiliza la biblioteca OpenHardwareMonitor para obtener datos del sistema.
  https://openhardwaremonitor.org/
- Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, siéntete libre de enviar un pull request.
