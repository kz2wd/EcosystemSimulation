from __future__ import annotations

import random
import threading
from enum import Enum
import winsound

import playsound

from simulation.collision_box import CollisionBox
from simulation.colors import Color, get_winning_color
from maths.vector2d import Vector2D


class AgentStates(Enum):
    DEAD = 0
    ALIVE = 1


class Agent:

    def __init__(self, coordinates: Vector2D, color: Color, radius: int = 10):
        self.movement: Vector2D = Vector2D(random.random(), random.random())  # init with random movement vector
        self.color: Color = color
        self.collision_box = CollisionBox(coordinates, radius)
        self.state = AgentStates.ALIVE
        self.speed = 1

    @property
    def coordinates(self):
        return self.collision_box.center

    @property
    def radius(self):
        return self.collision_box.radius

    def move(self, dt):
        self.collision_box.center += self.movement * dt * self.speed

    def handle_collision(self, other: Agent, counts: dict[Color: int]):
        if self.collision_box.is_colliding(other.collision_box):

            # Update movement
            new_direction = (other.coordinates - self.coordinates)
            self.movement = new_direction.normalize * -1

            # winsound.PlaySound("C:\\Users\\itrot\\PycharmProjects\\EcosystemSimulation\\mixkit-cartoon-quick-splat-2890.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

            # Update color
            if other.color == get_winning_color(self.color):
                # prevent from loosing a color
                # if counts[self.color] > 2:
                counts[self.color] -= 1
                self.color = other.color
                counts[self.color] += 1


class CreatureAgent(Agent):
    MAX_RADIUS = 2000

    def handle_collision(self, other: CreatureAgent, counts: dict[Color: int]):
        if self.collision_box.is_colliding(other.collision_box):

            if self.radius < other.radius:
                self.state = AgentStates.DEAD
            else:
                self.collision_box.radius = min(other.radius + self.radius, CreatureAgent.MAX_RADIUS)
                self.speed = 10 / self.radius
