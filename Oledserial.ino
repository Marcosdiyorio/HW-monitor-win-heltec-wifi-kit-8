#include <Wire.h>
#include "heltec.h"

#define MAX_LINES 2
#define MAX_CHARS_PER_LINE 10

String lines[MAX_LINES]; // Buffer para almacenar las líneas de texto
int currentLine = 0; // Índice de la línea actual en el buffer
unsigned long lastUpdateTime = 0; // Tiempo de la última actualización del display
const unsigned long updateInterval = 500; // Intervalo de actualización en milisegundos (ajustar según sea necesario)

void setup() {
  Serial.begin(115200); // Inicializa el puerto serial a 115200 baudios
  Heltec.begin(true, true); // Inicializa el display OLED
  Heltec.display->init(); // Inicializa el display OLED
  Heltec.display->flipScreenVertically(); // Voltea la pantalla verticalmente (opcional)
  Heltec.display->setFont(ArialMT_Plain_16); // Establece la fuente del texto
  
  Heltec.display->clear(); // Limpia el contenido actual del display
  Heltec.display->drawString(0, 0, "Esperando..."); // Muestra un mensaje inicial
  Heltec.display->display(); // Muestra el mensaje en el display
  delay(5000); // Espera 5 segundos antes de continuar
}

void loop() {
  if (Serial.available() > 0) { // Verifica si hay datos disponibles en el puerto serial
    String data = Serial.readStringUntil('\n'); // Lee una línea de texto desde el puerto serial
    
    // Almacena la línea de texto en el buffer circular
    lines[currentLine] = data;
    currentLine = (currentLine + 1) % MAX_LINES;
    
    unsigned long currentTime = millis(); // Obtiene el tiempo actual en milisegundos
    // Verifica si ha pasado suficiente tiempo desde la última actualización
    if (currentTime - lastUpdateTime >= updateInterval) {
      updateDisplay(); // Actualiza el contenido del display
      lastUpdateTime = currentTime; // Actualiza el tiempo de la última actualización
    }
  }
}

void updateDisplay() {
  Heltec.display->clear(); // Borra el contenido actual del display
  // Muestra las líneas de texto almacenadas en el buffer en el display
  for (int i = 0; i < MAX_LINES; i++) {
    int y = i * 16; // Calcula la posición vertical de la línea en el display
    Heltec.display->drawString(0, y, lines[i]); // Dibuja la línea de texto en el display
  }
  Heltec.display->display(); // Muestra el contenido actualizado en el display
}