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
        
        myDb = Database()
        sense = CustomSenseHat()
        
        with open('config.json', 'r') as f:
            threshold_data = json.load(f)
        try: 
            while True:
                
                temperature = sense.getCalibratedTemperature()
                humidity = sense.getHumditity()
                # humid_color = (0,255,0)
                # temp_color = (0, 255, 0)
                # tempature_category = "normal"
                # humidity_category = "normal"

                tempature_output = round(temperature)
                humidity_output = round(humidity)
                
                temp_color, temperature_category = sense.checkTemperatureThresold(
                    tempature_output,
                    int(threshold_data['cold_temperature_upper_limit']),
                    int(threshold_data["hot_temperature_lower_limit"])
                )
                
                humid_color, humidity_category = sense.checkHumidityThresold(
                    humidity,
                    int(threshold_data['dry_humidity_upper_limit']),
                    int(threshold_data['wet_humidity_lower_limit'])
                )

                # if humidity < int(threshold_data['dry_humidity_upper_limit']):
                #     humid_color = (105, 50, 168)
                #     humidity_category = "dry"
                # elif humidity > int(threshold_data['wet_humidity_lower_limit']):
                #     humid_color = (0,0,255)
                #     humidity_category = "wet"

                # if tempature_output  < int(threshold_data['cold_temperature_upper_limit']):
                #     temp_color = (163,163,163)
                #     tempature_category = "cold"
                # elif tempature_output  > int(threshold_data["hot_temperature_lower_limit"]):
                #     temp_color= (255,0,0)
                #     tempature_category = "hot"
                    
                data = {
                    "recorded_time": str(datetime.now()),
                    "temperature": temperature,
                    "temperature_category":temperature_category, 
                    "humidity":humidity, 
                    "humidity_category":humidity_category
                }
                
                myDb.insert(data)
                myDb.select()
                
                sense.displayMessage(f"T {str(tempature_output)}",temp_color,0.2)

                # Wait for 5 seconds
                time.sleep(5)
                
                sense.displayMessage(f"H {str(humidity_output)}",temp_color,0.2)
                time.sleep(5)
                sense.clear()
        except KeyboardInterrupt:
            sense.clear()