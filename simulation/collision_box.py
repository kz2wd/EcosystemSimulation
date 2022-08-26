from __future__ import annotations

from maths.vector2d import Vector2D


class CollisionBox:
    def __init__(self, center: Vector2D, radius: int):
        self.center = center
        self.radius = radius

    def is_colliding(self, other_box: CollisionBox):
        return self.center.distance(other_box.center) <= self.radius + other_box.radius
