from enum import Enum


# Color instead of symbols, rock paper scissor like function

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


# fixed, if you want more control
winning_color = {Color.RED: Color.GREEN,
                 Color.GREEN: Color.BLUE,
                 Color.BLUE: Color.RED}


# Dynamic, if you want more colors
def get_winning_color(color: Color):

    if color.value == len(Color):
        return Color(1)
    else:
        return Color(color.value + 1)

