"""Fetch the following system stats:
CPU Usage (percentage).
Memory Usage (percentage used).
Disk Usage (percentage used for /).
System Uptime (time since last boot).
Log these stats to a file (logs/system_logs.log).
Write the Core Functions:

Function to fetch the stats.
Function to log the stats to a file in the logs/ directory."""
import psutil
from datetime import datetime
import os

Logfile = "logs/system_logs.log"


def cpu_usage():
    return psutil.cpu_percent(interval = 1)
def memory_usage():
    return psutil.virtual_memory().percent
def disk_usage():
    return psutil.disk_usage('/').percent
def system_uptime():
    boot_time = datetime.fromtimestamp(psutil.boot_time())
    current_time = datetime.now()
    uptime = current_time - boot_time
    return str(uptime).split('.')[0] 
def log_stats():
    stats = {"Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "CPU": cpu_usage(),
        "Memory": memory_usage(),
        "Disk": disk_usage(),
        "Uptime": system_uptime()
    }
    log_entry = (f"[{stats['Time']}] CPU: {stats['CPU']}%, "
                 f"Memory: {stats['Memory']}%, "
                 f"Disk: {stats['Disk']}%, "
                 f"Uptime: {stats['Uptime']}\n")
    
    os.makedirs("logs",exist_ok = True)
    with open(Logfile, "a") as log_file:
        log_file.write(log_entry)
    print("Log entry added:", log_entry.strip())
if __name__ == "__main__":
    log_stats()