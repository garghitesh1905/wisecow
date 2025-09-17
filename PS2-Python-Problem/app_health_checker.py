import requests
from datetime import datetime

APP_URL = "https://www.python.org"  
REQUEST_TIMEOUT = 10                
LOG_FILE = "app_status.log"

def record_status(message):
    """Log status messages with timestamp to console and file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] {message}"
    print(entry)
    with open(LOG_FILE, "a") as log_file:
        log_file.write(entry + "\n")

def check_app():
    """Perform a GET request and assess if the app is up or down."""
    try:
        response = requests.get(APP_URL, timeout=REQUEST_TIMEOUT)
        if response.status_code == 200:
            record_status(f"Application is ONLINE | {APP_URL} | Status: 200 OK")
        else:
            record_status(f"Application may be DOWN | {APP_URL} | Status: {response.status_code}")
    except requests.RequestException as error:
        record_status(f"Application is OFFLINE | {APP_URL} | Error: {error}")

if __name__ == "__main__":
    print(f"Checking {APP_URL}...")
    check_app()
