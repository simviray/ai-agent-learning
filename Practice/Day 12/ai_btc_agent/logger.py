# Import datetime to create timestamps
from datetime import datetime

# Import log file paths from config
from config import TRADE_MEMORY_FILE, ERROR_LOG_FILE

# Function to create readable timestamp
def get_timestamp():

    # Return current date and time
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Function to save successful trade monitoring records
def save_trade_memory(scan_number, timestamp, btc_price, decision):

    # Open trade memory file safely in append mode
    with open(TRADE_MEMORY_FILE, "a") as memory_file:

        # Save scan details
        memory_file.write(f"Scan Number: {scan_number}\n")
        memory_file.write(f"Timestamp: {timestamp}\n")
        memory_file.write(f"BTC Price: {btc_price}\n")
        memory_file.write(f"Decision: {decision}\n")
        memory_file.write("----------------------\n")

# Function to save error records
def save_error_log(error):

    # Create timestamp for the error
    timestamp = get_timestamp()

    # Get error type name
    error_type = type(error).__name__

    # Get readable error message
    error_message = str(error)

    # Open error log file safely in append mode
    with open(ERROR_LOG_FILE, "a") as error_file:

        # Save error details
        error_file.write(f"Timestamp: {timestamp}\n")
        error_file.write(f"Error Type: {error_type}\n")
        error_file.write(f"Message: {error_message}\n")
        error_file.write("----------------------\n")