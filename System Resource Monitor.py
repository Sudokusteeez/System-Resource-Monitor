import psutil
import time

def display_usage(cpu_usage, mem_usage, disk_usage, cpu_temp, bars=50):
    cpu_percent = (cpu_usage / 100.0)
    cpu_bar = '█' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))
    mem_percent = (mem_usage / 100.0)
    mem_bar = '█' * int(mem_percent * bars) + '-' * (bars - int(mem_percent * bars))
    disk_percent = (disk_usage.percent / 100.0)
    disk_bar = '█' * int(disk_percent * bars) + '-' * (bars - int(disk_percent * bars))

    print(f"\rCPU Usage: |{cpu_bar}| {cpu_usage:.2f}%  ", end="")
    print(f"MEM Usage: |{mem_bar}| {mem_usage:.2f}%  ", end="")
    print(f"Disk Usage: |{disk_bar}| {disk_usage.percent:.2f}%  ", end="")
    print(f"CPU Temp: {cpu_temp:.1f}°C", end="\r")

    # Check for usage above 90% and display warnings
    if cpu_usage > 90:
        print("\nWarning: High CPU Usage! Consider optimizing processes.")
    if mem_usage > 95:
        print("\nWarning: High Memory Usage! Check for memory leaks or resource-heavy applications.")
    if disk_usage.percent > 90:
        print("\nWarning: High Disk Usage! Free up disk space to avoid performance issues.")

if __name__ == "__main__":
    while True:
        cpu_usage = psutil.cpu_percent()
        mem_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/')  # Replace '/' with the path of the disk you want to monitor

        # Get CPU temperature
        cpu_temp = 0.0
        if hasattr(psutil, "sensors_temperatures"):
            temps = psutil.sensors_temperatures()
            if "coretemp" in temps:
                cpu_temp = temps["coretemp"][0].current

        display_usage(cpu_usage, mem_usage, disk_usage, cpu_temp, 30)
        time.sleep(0.5)