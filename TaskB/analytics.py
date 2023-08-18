import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import sys
import os


# Get the path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Import modules
from extras.repository import Database
# Restoring sys.path to its original state
sys.path.remove(parent_dir)


class DataVisulisation:
    @staticmethod
    def create_matplotlib_linegraph(x,y,xLabel,yLabel,imageName,title):
       plt.plot(x,y,marker='o')
       plt.title(title)
       plt.xlabel(xLabel)
       plt.ylabel(yLabel)
       plt.savefig(imageName, dpi=300)
       plt.close()
    
    @staticmethod
    def create_seaborn_bargraph(df, x, xLabel,yLabel,imageName,title):
        sns.set_theme(style="whitegrid")
        sns.countplot(data=df,x=x)
        plt.title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.savefig(imageName, dpi=300)
        plt.close()
        

if __name__ == "__main__":
    myDb = Database()
    df = myDb.getDataFrame()
    
    x = df['recorded_time'].values
    y = df['temperature'].values
    y2 = df['humidity'].values
    
    DataVisulisation.create_matplotlib_linegraph(x,y,"Time Recorded","Temperature (C)","temperature_plot.png","Temperature Recorded Over Time")
    DataVisulisation.create_matplotlib_linegraph(x,y2,"Time Recorded","Humidity","humidity_plot.png","Humidity Recorded Over Time")
    DataVisulisation.create_seaborn_bargraph(df,"temperature_category","Temperature Category","Total Count","temperature_category_plot.png","Total Count of Temperature Categories")
    DataVisulisation.create_seaborn_bargraph(df,"humidity_category","Humidity Category","Total Count","humidity_category_plot.png","Total Count of Temperature Categories")