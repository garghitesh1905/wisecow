import psutil
import time
from datetime import datetime

CPU_LIMIT = 80        
MEMORY_LIMIT = 80     
DISK_LIMIT = 90       
INTERVAL = 60         
LOG_FILE = "system_monitor.log"

def write_log(message):
    """Append message to log file with timestamp and print to console."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    full_message = f"[{timestamp}] {message}"
    print(full_message)
    with open(LOG_FILE, "a") as log:
        log.write(full_message + "\n")

def gather_system_info():
    """Retrieve CPU, memory, and disk usage statistics."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    return cpu, memory, disk

def check_limits(cpu, memory, disk):
    """Compare metrics to thresholds and log warnings if needed."""
    if cpu > CPU_LIMIT:
        write_log(f"WARNING: CPU usage is high ({cpu}%)")
    if memory > MEMORY_LIMIT:
        write_log(f"WARNING: Memory usage is high ({memory}%)")
    if disk > DISK_LIMIT:
        write_log(f"WARNING: Disk space low ({disk}% used)")
    if cpu <= CPU_LIMIT and memory <= MEMORY_LIMIT and disk <= DISK_LIMIT:
        write_log(f"System healthy | CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

if __name__ == "__main__":
    print("Starting system monitoring...")
    while True:
        cpu_val, mem_val, disk_val = gather_system_info()
        check_limits(cpu_val, mem_val, disk_val)
        time.sleep(INTERVAL)
