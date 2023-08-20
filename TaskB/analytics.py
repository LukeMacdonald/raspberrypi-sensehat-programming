"""
This script demonstrates data visualization using Matplotlib and Seaborn.
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import seaborn as sns
import numpy as np



# Get the path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Import modules
from extras.repository import Database
# Restoring sys.path to its original state
sys.path.remove(parent_dir)


class DataVisulisation:
    """
    Provides static methods for creating data visualizations using Matplotlib and Seaborn.
    """

    @staticmethod
    def create_matplotlib_linegraph(x, y, x_label, y_label, image_name, title):
        """
        Create a line graph using Matplotlib.

        Parameters:
        x (array-like): X-axis data.
        y (array-like): Y-axis data.
        x_label (str): Label for the X-axis.
        y_label (str): Label for the Y-axis.
        image_name (str): Filename for saving the graph image.
        title (str): Title of the graph.
        """
        
        ### The Code marked between the 3 hashes was obtained through ChatGPT to allow x-axis ticks 
        # to be placed evenly within range between first and last recorded datetimes.
        
        # Calculate min and max datetime values
        min_datetime = np.min(x)
        max_datetime = np.max(x)
        
        # Calculate number of desired ticks
        num_ticks = 10
        
        # Generate a sequence of evenly spaced datetime ticks
        tick_delta = (max_datetime - min_datetime) / (num_ticks - 1)
        tick_positions = [min_datetime + i * tick_delta for i in range(num_ticks)]
        
        # Convert datetime64 objects to microseconds since epoch
        tick_micros = (tick_positions - np.datetime64('1970-01-01T00:00:00')) / np.timedelta64(1, 'us')
        
        # Format datetime ticks
        formatted_ticks = [str(datetime.utcfromtimestamp(int(micros / 1e6)).strftime('%Y-%m-%d:%H:%M:%S')) for micros in tick_micros]
        ###
        
        plt.figure(figsize=(10, 8))
        plt.plot(x, y, marker='o')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xticks(tick_positions, [str(i) for i in formatted_ticks], rotation=90)
        plt.subplots_adjust(bottom=0.4)
        plt.tight_layout()
        plt.savefig(image_name, dpi=300)
        plt.close()

    @staticmethod
    def create_seaborn_bargraph(df, x, x_label, y_label, image_name, title):
        """
        Create a bar graph using Seaborn.

        Parameters:
        df (DataFrame): Pandas DataFrame containing the data.
        x (str): Column name for the X-axis data.
        x_label (str): Label for the X-axis.
        y_label (str): Label for the Y-axis.
        image_name (str): Filename for saving the graph image.
        title (str): Title of the graph.
        """
        sns.set_theme(style="whitegrid")
        sns.countplot(data=df, x=x)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.savefig(image_name, dpi=300)
        plt.close()     

if __name__ == "__main__":
    myDb = Database()
    df = myDb.get_dataframe()
    
    x = df['recorded_time'].values
    y = df['temperature'].values
    y2 = df['humidity'].values
    
    DataVisulisation.create_matplotlib_linegraph(
        x, y, "Time Recorded", "Temperature (C)",
        "temperature_plot.png", "Temperature Recorded Over Time"
    )
    DataVisulisation.create_matplotlib_linegraph(
        x, y2, "Time Recorded", "Humidity",
        "humidity_plot.png", "Humidity Recorded Over Time"
    )
    DataVisulisation.create_seaborn_bargraph(
        df, "temperature_category", "Temperature Category",
        "Total Count", "temperature_category_plot.png",
        "Total Count of Temperature Categories"
    )
    DataVisulisation.create_seaborn_bargraph(
        df, "humidity_category", "Humidity Category",
        "Total Count", "humidity_category_plot.png",
        "Total Count of Humidity Categories"
    )
    