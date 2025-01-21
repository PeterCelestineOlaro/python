import subprocess
import logging
import os

# Setup logging
logging.basicConfig(filename='battery_health_check.log', level=logging.DEBUG)

def get_battery_health_windows():
    try:
        # Run powercfg to generate battery report
        battery_report = subprocess.check_output('powercfg /batteryreport', shell=True, text=True)
        
        # Output the report path (it will be saved in the user directory)
        logging.info(f"Battery report generated: {battery_report.split(' ')[-1].strip()}")
        
        # Read the report file
        report_file_path = os.path.expanduser('~') + '\\battery-report.html'
        with open(report_file_path, 'r') as report_file:
            report_data = report_file.read()
            logging.info("Battery health report:\n" + report_data)
    except Exception as e:
        logging.error(f"Error generating battery report: {e}")

def main():
    get_battery_health_windows()
    logging.info("Battery health check completed.")

if __name__ == "__main__":
    main()
