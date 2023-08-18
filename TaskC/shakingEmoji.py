from sense_hat import SenseHat
from animatedEmoji import emojis

def is_shaken(acceleration,shake_threshold):
    x = abs(acceleration['x'])
    y = abs(acceleration['y'])
    z = abs(acceleration['z'])
    return x > shake_threshold or y > shake_threshold or z > shake_threshold

if __name__ == '__main__':
    sense = SenseHat()
    emoji_list = emojis()
    while True:

        acceleration = sense.get_accelerometer_raw()

        if is_shaken(acceleration, 2):
            current_emoji = emoji_list.pop(0)
            emoji_list.append(current_emoji)
            # Display these colours on the LED matrix
            sense.set_pixels(current_emoji)