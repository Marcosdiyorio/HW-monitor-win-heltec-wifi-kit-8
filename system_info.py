import psutil
import wmi

def get_cpu_temperature_windows():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature' and "CPU" in sensor.Name:
                return int(sensor.Value)
        return "N/A"
    except Exception as e:
        print("Error al obtener la temperatura de la CPU en Windows:", e)
        return "N/A"

def get_cpu_power_consumption_windows():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        power_infos = w.Sensor()
        for sensor in power_infos:
            if sensor.SensorType == u'Power' and "CPU Package" in sensor.Name:
                return int(sensor.Value)
        return "N/A"
    except Exception as e:
        print("Error al obtener el consumo de energía de la CPU en Windows:", e)
        return "N/A"

def get_cpu_usage():
    try:
        return int(psutil.cpu_percent())
    except Exception as e:
        print("Error al obtener el uso de la CPU:", e)
        return "N/A"

def get_memory_usage():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Load' and "Memory" in sensor.Name:
                return int(sensor.Value)
        return "N/A"
    except Exception as e:
        print("Error al obtener el uso de memoria en Windows:", e)
        return "N/A"

def get_gpu_temperature_windows():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Temperature' and "GPU" in sensor.Name:
                return int(sensor.Value)
        return "N/A"
    except Exception as e:
        print("Error al obtener la temperatura de la GPU en Windows:", e)
        return "N/A"

def get_gpu_usage_windows():
    try:
        w = wmi.WMI(namespace="root\\OpenHardwareMonitor")
        temperature_infos = w.Sensor()
        for sensor in temperature_infos:
            if sensor.SensorType == u'Load' and "GPU Core" in sensor.Name:
                return int(sensor.Value)
        return "N/A"
    except Exception as e:
        print("Error al obtener el uso de la GPU en Windows:", e)
        return "N/A"
