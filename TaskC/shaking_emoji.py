"""
Main script for running the LED matrix emoji cycling program.
"""
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
            # Checks if raspberry pi has been shaken
            if sense.detect_shaking(2):
                current_emoji = emoji_list.cycle_emoji()
                # Display these colours on the LED matrix
                sense.display_emoji(current_emoji)
    except KeyboardInterrupt:
            sense.clear()