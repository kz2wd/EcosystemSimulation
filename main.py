import random

import pygame

from maths.vector2d import Vector2D
from simulation.agent import Agent, CreatureAgent
from simulation.colors import Color
from simulation.field import Field
from simulation.simulation import Simulation


def color_count_display(color_counts: dict[Color, int], font, surface):
    for i, (color, amount) in enumerate(color_counts.items()):
        text = font.render(f"{color.name.capitalize()} : {amount}", True, (50, 50, 50))
        surface.blit(text, (0, i * font.get_linesize() + 10))


def simple_agents() -> list[Agent]:
    colors = list(Color)
    agents: list[Agent] = [
        Agent(Field.get_random_coordinates(window_size, balls_size), random.choice(colors),
              balls_size) for _ in range(balls_amount)]
    return agents


def creature_agents() -> list[CreatureAgent]:
    colors = list(Color)
    agents: list[CreatureAgent] = []
    for _ in range(balls_amount):

        agents.append(CreatureAgent(Field.get_random_coordinates(window_size, balls_size), random.choice(colors),
                      random.randint(5, 15)))
    return agents


if __name__ == "__main__":

    window_size = (width, height) = (700, 700)
    framerate = 144
    balls_speed = 1.5
    balls_amount = 50
    balls_size = 20
    screen = pygame.display.set_mode(window_size)
    agent_layer = pygame.surface.Surface(window_size)

    clock = pygame.time.Clock()

    # Init simulation here

    # simulation_agents = simple_agents()
    simulation_agents = creature_agents()

    current_simulation = Simulation(window_size, simulation_agents)

    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 32)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(framerate)
        screen.fill((255, 255, 255))
        agent_layer.fill((255, 255, 255))
        current_simulation.draw(agent_layer)
        screen.blit(agent_layer, (0, 0))
        current_simulation.update(dt/10 * balls_speed)

        color_count_display(current_simulation.agents_counts, font, screen)
        pygame.display.update()












