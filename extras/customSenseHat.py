from sense_hat import SenseHat
from extras.emoji import Emoji
from extras.utils import get_cpu_temp, get_smooth

class CustomSenseHat:
    def __init__(self):
        self.sense = SenseHat()
    
    def calibrateTemperature(self,t1,t2):
        t_cpu = get_cpu_temp()
        t = (t1 + t2) / 2
        t_corr = t - ((t_cpu - t) / 1.5)
        return get_smooth(t_corr)
        
    def getCalibratedTemperature(self):
        t1 = self.sense.get_temperature_from_humidity()
        t2 = self.sense.get_temperature_from_pressure()
        return self.calibrateTemperature(t1,t2)
       
    def getHumditity(self):
        return self.sense.get_humidity()
    
    def displayEmoji(self, emoji: Emoji):
        self.sense.set_pixels(emoji.getPattern())
    
    def detectShaking(self,shake_threshold):
        acceleration = self.sense.get_accelerometer_raw()
        x = abs(acceleration['x'])
        y = abs(acceleration['y'])
        z = abs(acceleration['z'])
        return x > shake_threshold or y > shake_threshold or z > shake_threshold
    
    def displayMessage(self,message,colour,scoll_time):
        self.sense.show_message(message,text_colour=colour,scroll_speed=scoll_time)
     
    def clear(self):
        self.sense.clear()
    
    def checkTemperatureThresold(self, temperature,low, high):
        if temperature < low:
            return (163,163,163), "cold"
        elif temperature > high:
            return (255,0,0), "hot"
        else:
            return (0, 255, 0), "normal"
    
    def checkHumidityThresold(self, humidity,low, high):
        if humidity < low:
            return (105, 50, 168), "dry"
        elif humidity > high:
            return (0, 0, 255), "wet"
        else:
            return (0, 255, 0), "normal"
    
        