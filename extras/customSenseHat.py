from sense_hat import SenseHat
from extras.emoji import Emoji
from extras.utils import get_cpu_temp, get_smooth

class CustomSenseHat:
    """
    A custom class that extends the functionality of the SenseHat module for Raspberry Pi.
    """

    def __init__(self):
        """
        Initializes the CustomSenseHat object and connects to the Sense HAT hardware.
        """
        self.sense = SenseHat()

    def calibrate_temperature(self, temperature1, temperature2):
        """
        Calibrates the temperature readings using CPU temperature and returns a smoothed result.

        Parameters:
        - temperature1 (float): Temperature reading from humidity sensor.
        - temperature2 (float): Temperature reading from pressure sensor.

        Returns:
        float: Calibrated and smoothed temperature value.
        """
        t_cpu = get_cpu_temp()  # Assuming this function is defined somewhere
        temperature = (temperature1 + temperature2) / 2
        tempature_corr = temperature - ((t_cpu - temperature) / 1.5)
        return get_smooth(tempature_corr)  # Assuming this function is defined somewhere

    def get_calibrated_temperature(self):
        """
        Retrieves the calibrated temperature reading by averaging humidity and pressure 
        sensor values.

        Returns:
        float: Calibrated temperature value.
        """
        temperature1 = self.sense.get_temperature_from_humidity()
        temperature2 = self.sense.get_temperature_from_pressure()
        return self.calibrate_temperature(temperature1, temperature2)

    def get_humidity(self):
        """
        Retrieves the current humidity reading from the humidity sensor.

        Returns:
        float: Humidity value.
        """
        return self.sense.get_humidity()

    def display_emoji(self, emoji: Emoji):
        """
        Displays an emoji pattern on the LED matrix.

        Parameters:
        emoji (Emoji): An instance of the Emoji class representing the desired emoji pattern.
        """
        self.sense.set_pixels(emoji.get_pattern())

    def detect_shaking(self, shake_threshold):
        """
        Detects shaking motion based on accelerometer readings.

        Parameters:
        shake_threshold (float): Threshold value for accelerometer readings.

        Returns:
        bool: True if shaking is detected, False otherwise.
        """
        acceleration = self.sense.get_accelerometer_raw()
        x_axis = abs(acceleration['x'])
        y_axis = abs(acceleration['y'])
        z_axis = abs(acceleration['z'])
        return x_axis > shake_threshold or y_axis > shake_threshold or z_axis > shake_threshold

    def display_message(self, message, colour, scroll_time):
        """
        Displays a scrolling text message with specified text color and scroll speed.

        Parameters:
        message (str): The text message to be displayed.
        colour (tuple): RGB tuple representing the text color.
        scroll_time (float): Scroll speed of the message.
        """
        self.sense.show_message(message, text_colour=colour, scroll_speed=scroll_time)

    def clear(self):
        """
        Clears the LED matrix, turning off all pixels.
        """
        self.sense.clear()

    def check_temperature_threshold(self, temperature, low, high):
        """
        Compares the given temperature against low and high thresholds and returns status color 
        and label.

        Parameters:
        temperature (float): Temperature value to be checked.
        low (float): Lower temperature threshold.
        high (float): Upper temperature threshold.

        Returns:
        tuple: RGB tuple representing the status color, and a string indicating the status label.
        """
        if temperature < low:
            return (163, 163, 163), "cold"
        if temperature > high:
            return (255, 0, 0), "hot"
        return (0, 255, 0), "normal"

    def check_humidity_threshold(self, humidity, low, high):
        """
        Compares the given humidity against low and high thresholds and returns status color 
        and label.

        Parameters:
        humidity (float): Humidity value to be checked.
        low (float): Lower humidity threshold.
        high (float): Upper humidity threshold.

        Returns:
        tuple: RGB tuple representing the status color, and a string indicating the status label.
        """
        if humidity < low:
            return (105, 50, 168), "dry"
        if humidity > high:
            return (0, 0, 255), "wet"
        return (0, 255, 0), "normal"
        