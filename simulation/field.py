import random

from maths.vector2d import Vector2D


class Field:
    def __init__(self, size: tuple[int, int]):
        self.size: tuple[int, int] = size

    @property
    def width(self):
        return self.size[0]

    @property
    def height(self):
        return self.size[1]

    @staticmethod
    def get_random_coordinates(size, padding=0):
        return Vector2D(random.uniform(padding, size[0] - (padding + 1)),
                        random.uniform(padding, size[1] - (padding + 1)))

