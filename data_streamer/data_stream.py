import random
import time
from datetime import datetime

#   DATA GENERATION FUNCTION
def generate_temperature():
    """
    Generates a mock temperature reading between 20°C and 35°C.
    Returns a float rounded to 2 decimal places.
    """
    return round(random.uniform(20.0, 35.0), 2)

#   LOGGING FUNCTION
def log_data(value):
    """
    Logs the data value with a timestamp into a file named 'data_stream.log'.
    Each line contains: timestamp, value
    """
    timestamp = datetime.now().isoformat()
    with open("data_stream.log", "a") as file:
        file.write(f"{timestamp}, {value}\n")

#   CONTINUOUS DATA STREAM
def start_stream(interval_seconds=2):
    """
    Starts an infinite loop that generates and logs temperature data
    every 'interval_seconds' seconds.
    """
    print(f"Starting data stream... Logging new values every {interval_seconds} seconds.")
    print("Press CTRL + C to stop.\n")

    while True:
        temp = generate_temperature()
        log_data(temp)
        print(f"Logged -> Temperature: {temp}°C")
        time.sleep(interval_seconds)


#   MAIN PROGRAM ENTRY POINT
if __name__ == "__main__":
    start_stream(interval_seconds=2)
