import random

import pygame

from simulation.agent import Agent
from simulation.colors import Color
from simulation.field import Field


class Simulation:
    def __init__(self, agent_amount: int, field_size: tuple[int, int]):
        self.field: Field = Field(field_size)
        colors = list(Color)
        default_agent_size = 20
        self.agents: list[Agent] = [Agent(self.field.get_random_coordinates(default_agent_size),
                                          random.choice(colors),
                                          default_agent_size) for _ in range(agent_amount)]

        self.agents_counts: dict[Color: int] = {color: len([a for a in self.agents if a.color == color]) for color in Color}

    def update(self, dt):

        # Agent movement
        for agent in self.agents:
            agent.move(dt)

        # Agent collision with terrain
        for agent in self.agents:
            if not agent.radius < agent.coordinates.x < self.field.width - agent.radius:
                agent.movement.x *= -1
            if not agent.radius < agent.coordinates.y < self.field.height - agent.radius:
                agent.movement.y *= -1

        # Agent collision with other agents
        # Very bad improve
        for agent in self.agents:
            for a2 in self.agents:
                if a2 != agent:
                    agent.handle_collision(a2, self.agents_counts)

    def draw(self, surface):
        for agent in self.agents:
            pygame.draw.circle(surface, agent.color.name, (agent.coordinates.x, agent.coordinates.y), agent.radius)
