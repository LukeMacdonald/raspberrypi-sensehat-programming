"""
Temperature and Smoothing Utilities

This module provides functions to retrieve CPU temperature and perform moving average smoothing.
"""
import os

def get_cpu_temp():
    """
    Get the CPU temperature of the Raspberry Pi.

    Returns:
    float: The CPU temperature in degrees Celsius.
    """
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=", "").replace("'C\n", ""))

def get_smooth(x):
    """
    Smooth a value using a moving average over the last three readings.

    Parameters:
    x (float): The value to be smoothed.

    Returns:
    float: The smoothed value.
    """
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x, x, x]
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x

    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3
