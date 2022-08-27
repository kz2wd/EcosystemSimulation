import random

import pygame

from simulation.agent import Agent, AgentStates, CreatureAgent
from simulation.colors import Color
from simulation.field import Field


class Simulation:
    def __init__(self, field_size: tuple[int, int], agents):
        self.agents = agents
        self.field: Field = Field(field_size)
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

        # Clear dead agents
        self.agents = list(filter(lambda a: a.state != AgentStates.DEAD, self.agents))



    def draw(self, agent_surface):
        for agent in self.agents:
            pygame.draw.circle(agent_surface, agent.color.name, (agent.coordinates.x, agent.coordinates.y), agent.radius)

