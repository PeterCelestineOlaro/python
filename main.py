import os
import psutil
import platform
import logging
import subprocess

logging.basicConfig(filename='system_health_check.log', level=logging.DEBUG)

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    logging.info(f"CPU Usage: {cpu_usage}%")
    if cpu_usage > 90:
        logging.warning("CPU Usage is very high!")

def check_memory_usage():
    memory = psutil.virtual_memory()
    logging.info(f"Memory Usage: {memory.percent}%")
    if memory.percent > 90:
        logging.warning("Memory Usage is very high!")

def check_disk_usage():
    disk = psutil.disk_usage('/')
    logging.info(f"Disk Usage: {disk.percent}%")
    if disk.percent > 90:
        logging.warning("Disk Usage is very high!")

def check_system_logs():
    try:
        if platform.system() == 'Windows':
            logs = subprocess.check_output('eventvwr.msc /s', shell=True)
            logging.info(f"System logs: {logs}")
        else:
            logs = subprocess.check_output('journalctl -xe', shell=True)
            logging.info(f"System logs: {logs.decode()}")
    except Exception as e:
        logging.error(f"Error checking system logs: {e}")

def check_for_errors():
    try:
        check_system_logs()
    except Exception as e:
        logging.error(f"Error during health check: {e}")

def main():
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
    check_for_errors()
    logging.info("System health check completed.")

if __name__ == "__main__":
    main()
