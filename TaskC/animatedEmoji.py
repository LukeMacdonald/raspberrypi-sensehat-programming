from sense_hat import SenseHat
from time import sleep
from emoji import EmojiList

if __name__ == '__main__':
    sense = SenseHat()
    emoji_list = EmojiList()
    while True:
        current_emoji = emoji_list.cycleEmoji()
        # Display these colours on the LED matrix
        sense.set_pixels(current_emoji.getPattern())
        sleep(2)