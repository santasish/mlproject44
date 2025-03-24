import logging
import os
from datetime import datetime

# Generate the log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the logs directory path
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)  # Create the logs directory if it doesn't exist

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Debugging prints
print(f"Current working directory: {os.getcwd()}")
print(f"Logs directory path: {logs_path}")
print(f"Log file path: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

