import sys
import os
# Get the path of the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Add the parent directory to sys.path
sys.path.append(parent_dir)
# Now you can import the module
from extras.customSenseHat import CustomSenseHat
from extras.emoji import EmojiList
# Restoring sys.path to its original state (optional)
sys.path.remove(parent_dir)

if __name__ == '__main__':
    sense = CustomSenseHat()
    emoji_list = EmojiList()
    try:
        while True:
            if sense.detectShaking(2):
                current_emoji = emoji_list.cycleEmoji()
                # Display these colours on the LED matrix
                sense.displayEmoji(current_emoji)
    except KeyboardInterrupt:
            sense.clear()