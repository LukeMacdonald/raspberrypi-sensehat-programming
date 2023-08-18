from sense_hat import SenseHat
import os
import time
import json

# The below two functions were taken from lecture 4 to calibrate the temperature 
# measured by the SenseHat

# Get CPU temperature.
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    return float(res.replace("temp=","").replace("'C\n",""))

# Use moving average to smooth readings.
def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
    
    get_smooth.t[2] = get_smooth.t[1]
    get_smooth.t[1] = get_smooth.t[0]
    get_smooth.t[0] = x

    return (get_smooth.t[0] + get_smooth.t[1] + get_smooth.t[2]) / 3

with open('config.json', 'r') as f:
    data = json.load(f)
print(data['cold_temperature_upper_limit'])


sense = SenseHat()
while True:

    t1 = sense.get_temperature_from_humidity()
    t2 = sense.get_temperature_from_pressure()
    t_cpu = get_cpu_temp()

    h = sense.get_humidity()
    p = sense.get_pressure()

    # Calculates the real temperature compesating CPU heating.
    t = (t1 + t2) / 2
    t_corr = t - ((t_cpu - t) / 1.5)
    t_corr = get_smooth(t_corr)
    print(t_corr)


    humid_color = (0,255,0)
    temp_color = (0, 255, 0)

    tempature = int(t_corr)
    humidity = int(h)

    if humidity < int(data['dry_humidity_upper_limit']):
        humid_color = (105, 50, 168)
    elif humidity > int(data['wet_humidity_lower_limit']):
        humid_color = (0,0,255)

    if tempature  < int(data['cold_temperature_upper_limit']):
       temp_color = (163,163,163)
    elif tempature  > int(data["hot_temperature_lower_limit"]):
        temp_color= (255,0,0)



    sense.show_message("T" + str(tempature),text_colour=temp_color,scroll_speed=0.2)

    # Wait for 5 seconds
    time.sleep(5)
    sense.show_message("H" + str(humidity),text_colour=humid_color,scroll_speed=0.2)
    time.sleep(5)
    sense.clear()