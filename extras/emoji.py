"""
Module containing Emoji and EmojiList classes for managing LED matrix emojis.
"""
class Emoji:
    """
    Represents an emoji pattern to be displayed on an LED matrix.
    """

    def __init__(self, pattern):
        """
        Initializes an Emoji instance with the specified pixel pattern.

        Parameters:
        pattern (list): A list representing the pixel pattern of the emoji.
        """
        self.__pattern = pattern
            
    def set_pattern(self, pattern):
        """
        Sets the pixel pattern of the emoji.

        Parameters:
        pattern (list): A list representing the new pixel pattern of the emoji.
        """
        self.__pattern = pattern

    def get_pattern(self):
        """
        Retrieves the pixel pattern of the emoji.

        Returns:
        list: A list representing the pixel pattern of the emoji.
        """
        return self.__pattern

class EmojiList:
    """
    Represents a collection of predefined emojis.
    """
    def __init__(self):
        """
        Initializes an EmojiList instance and populates it with predefined emojis.
        """
        self.__emojis = []
        self.__emoji_index = 0  # Initialize the index of the current emoji

        # Define color constants
        y = (255, 255, 0)   # yellow
        e = (0, 0, 0)       # empty
        r = (255,0,0)       # red
        b = (0,0,255)       # blue
        w = (255,255,255)   # white
        g = (0,255,0)       # green
        p = (240,67,237)    # pink
        o = (240,130,67)    # orange
        d = (0, 5, 145)     # dark blue
        m = (32, 110, 23)   # dark green
        q = (136, 201, 129) # light green
         # Initialize and append predefined emojis
        creeper_pixels = [
            g, g, g, g, g, g, g, g,
            m, m, m, m, m, m, m, m,
            q, e, e, q, q, e, e, q,
            g, e, e, g, g, e, e, g,
            m, m, m, e, e, m, m, m,
            q, q, e, e, e, e, q, q,
            g, g, e, e, e, e, g, g,
            m, m, e, m, m, e, m, m
        ]
        smile_face = [
            e, e, y, y, y, y, e, e,
            e, y, e, e, e, e, y, e,
            y, e, b, e, e, b, e, y,
            y, e, e, e, e, e, e, y,
            y, e, r, e, e, r, e, y,
            y, e, e, r, r, e, e, y,
            e, y, e, e, e, e, y, e,
            e, e, y, y, y, y, e, e
        ]
        pacman_face = [
            d, d, y, y, y, d, d, d,
            d, y, y, y, y, y, d, d,
            y, y, y, y, y, d, d, d,
            y, y, y, y, d, d, w, d,
            y, y, y, y, y, d, d, d,
            d, y, y, y, y, y, d, d,
            d, d, y, y, y, d, d, d,
            d, d, d, d, d, d, d, d
        ]
        arrow = [
            e, e, e, w, w, e, e, e,
            e, e, y, y, y, y, e, e,
            e, r, e, r, r, e, r, e,
            b, e, e, b, b, e, e, b,
            e, e, e, g, g, e, e, e,
            e, e, e, w, w, e, e, e,
            e, e, e, y, y, e, e, e,
            e, e, e, r, r, e, e, e
        ]
        
        heart = [
            e, e, e, e, e, e, e, e,
            e, p, p, e, e, p, p, e,
            r, r, r, r, r, r, r, r,
            o, o, o, o, o, o, o, o,
            e, p, p, p, p, p, p, e,
            e, e, r, r, r, r, e, e,
            e, e, e, o, o, e, e, e,
            e, e, e, e, e, e, e, e
        ]
        # Add all emoji pixel matrixes to list
        self.__emojis.append(Emoji(creeper_pixels))
        self.__emojis.append(Emoji(smile_face))
        self.__emojis.append(Emoji(pacman_face))
        self.__emojis.append(Emoji(arrow))
        self.__emojis.append(Emoji(heart))
    
    def cycle_emoji(self):
        """
        Cycles the emoji list and returns the next emoji.

        Returns:
        Emoji: The next emoji in the list after cycling.
        """
        current_emoji = self.__emojis[self.__emoji_index]
        self.__emoji_index = (self.__emoji_index + 1) % len(self.__emojis)
        return current_emoji
        