# Import necessary libraries
from datetime import datetime
import os
import time
import json
import sys

# Get the path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Import modules from other directory
from extras.customSenseHat import CustomSenseHat
from extras.repository import Database
# Restoring sys.path to its original state
sys.path.remove(parent_dir)

if __name__ == "__main__":
    # Initialize the database and Sense Hat objects
    myDb = Database()
    sense = CustomSenseHat()

    # Load configuration data from a JSON file
    with open('config.json', 'r', encoding='utf-8') as f:
        threshold_data = json.load(f)

    try:
        while True:
            # Get calibrated temperature and humidity readings
            temperature = sense.get_calibrated_temperature()
            humidity = sense.get_humidity()           
            # Round temperature and humidity values
            tempature_output = round(temperature)
            humidity_output = round(humidity)
            # Determine temperature category and associated color
            temp_color, temperature_category = sense.check_temperature_threshold(
                tempature_output,
                int(threshold_data['cold_temperature_upper_limit']),
                int(threshold_data["hot_temperature_lower_limit"])
            )
            # Determine humidity category and associated color
            humid_color, humidity_category = sense.check_humidity_threshold(
                humidity,
                int(threshold_data['dry_humidity_upper_limit']),
                int(threshold_data['wet_humidity_lower_limit'])
            )
            # Prepare data for database insertion
            data = {
                "recorded_time": str(datetime.now()),
                "temperature": temperature,
                "temperature_category": temperature_category,
                "humidity": humidity,
                "humidity_category": humidity_category
            }
            # Insert data into the database and retrieve records
            myDb.insert(data)
            myDb.select()

            # Display temperature on LED matrix and wait for 5 seconds
            sense.display_message(f"T {str(tempature_output)}", temp_color, 0.2)
            time.sleep(5)
            # Display humidity on LED matrix and wait for 5 seconds
            sense.display_message(f"H {str(humidity_output)}", temp_color, 0.2)
            time.sleep(5)
            # Clear the LED matrix
            sense.clear()
    except KeyboardInterrupt:
        # Clear the LED matrix in case of a keyboard interrupt
        sense.clear()
        