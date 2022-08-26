from __future__ import annotations

import math
import numbers


class Vector2D:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y

    def __add__(self, other):
        if isinstance(other, Vector2D):
            x = self.x + other.x
            y = self.y + other.y
        else:
            raise Exception(f"Addition not implemented between Vector2D and {type(other)}")
        return Vector2D(x, y)

    def __iadd__(self, other):
        if isinstance(other, Vector2D):
            self.x += other.x
            self.y += other.y
        else:
            self.x += other[0]
            self.y += other[1]
        return self

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x - other
            y = self.y - other
        elif isinstance(other, Vector2D):
            x = self.x - other.x
            y = self.y - other.y
        else:
            raise Exception(f"Substraction not implemented between Vector2D and {type(other)}")
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x * other
            y = self.y * other
        else:
            raise Exception(f"Multiplication not implemented between Vector2D and {type(other)}")
        return Vector2D(x, y)

    def __imul__(self, other):
        if isinstance(other, numbers.Number):
            x = self.x * other
            y = self.y * other
        elif isinstance(other, Vector2D):
            x = self.x * other.x
            y = self.y * other.y
        else:
            raise Exception(f"Multiplication not implemented between Vector2D and {type(other)}")
        return Vector2D(x, y)

    def __iter__(self):
        return self.x, self.y

    def __str__(self):
        return f"{self.x:.1f} {self.y:.1f}"

    def distance(self, other: Vector2D) -> float:
        return abs(self.x - other.x) + abs(self.y - other.y)

    @property
    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def normalize(self):
        _len = self.length
        return Vector2D(self.x / _len, self.y / _len)



