import os
import platform
import psutil
import time


def api_host_informations():
    memory = psutil.virtual_memory()
    total_memory = memory.total / (1024**3)
    used_memory = memory.used / (1024**3)
    memory_percentage = memory.percent
    print(
        f"Memory Usage: {used_memory:.2f} GB / {total_memory:.2f} GB ({memory_percentage}%)"
    )
    disk_usage = psutil.disk_usage("/")
    total_disk = disk_usage.total / (1024**3)
    used_disk = disk_usage.used / (1024**3)
    disk_percentage = disk_usage.percent
    print(f"Disk Usage: {used_disk:.2f} GB / {total_disk:.2f} GB ({disk_percentage}%)")
    # System Uptime
    uptime_seconds = time.time() - psutil.boot_time()
    uptime_hours = uptime_seconds // 3600
    uptime_minutes = (uptime_seconds % 3600) // 60
    print(f"System Uptime: {int(uptime_hours)} hours, {int(uptime_minutes)} minutes")
    return [
        {"key": "Host Name", "value": str(os.name)},
        {"key": "System Type", "value": str(platform.system())},
        {"key": "Processor", "value": str(platform.processor())},
        {"key": "Release Version", "value": str(platform.release())},
        {"key": "CPU Count", "value": str(os.cpu_count())},
        {
            "key": "Memory Usage",
            "value": f"{used_memory:.2f} GB / {total_memory:.2f} GB ({memory_percentage}%)",
        },
        {
            "key": "System Uptime",
            "value": f"{int(uptime_hours)} hours, {int(uptime_minutes)} minutes",
        },
    ]
