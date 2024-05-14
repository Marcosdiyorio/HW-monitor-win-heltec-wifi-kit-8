import time
import platform
import serial
from system_info import *

# Si el sistema es Windows, importa la biblioteca wmi
if platform.system() == "Windows":
    import wmi

# Intentar abrir el puerto serial
try:
    ser = serial.Serial('COM4', 115200)  # Reemplaza 'COM4' con el puerto serial correcto
except serial.SerialException as e:
    print(f"Error al abrir el puerto serial: {e}")
    exit()

# Bucle principal para actualizar y enviar los datos
while True:
    # Obtener datos del sistema
    cpu_temp = get_cpu_temperature_windows()
    cpu_usage = get_cpu_usage()
    cpu_power = get_cpu_power_consumption_windows()  # Agregamos esta línea para obtener la potencia de la CPU
    memory_usage = get_memory_usage()
    gpu_temp = get_gpu_temperature_windows()
    gpu_usage = get_gpu_usage_windows()

    # Enviar los datos al ESP8266
    ser.write(f"µP {cpu_temp}° {cpu_usage}% {cpu_power}w\n".encode())
    ser.write(f"G {gpu_temp}° {gpu_usage}% m {memory_usage}%\n".encode())
    
      # Separador para mayor claridad

    # Esperar 1 segundos antes de la próxima actualización
    time.sleep(1)

# Cierra la conexión serial al salir del bucle (esto normalmente no se ejecutará)
ser.close()
