# Import datetime for timestamps
from datetime import datetime

try:
    # This will create an error because division by zero is not allowed
    result = 10 / 0

except Exception as error:

    # Create timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Get the error type
    error_type = type(error).__name__

    # Get the error message
    error_message = str(error)

    # Save error details into error_log.txt
    with open("./Day 09/error_log.txt", "a") as log_file:
        log_file.write(f"Timestamp: {timestamp}\n")
        log_file.write(f"Error Type: {error_type}\n")
        log_file.write(f"Message: {error_message}\n")
        log_file.write("----------------------\n")

    # Print friendly message
    print("Error saved to error_log.txt")