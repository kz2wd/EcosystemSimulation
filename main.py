import pygame

from simulation.colors import Color
from simulation.simulation import Simulation


def color_count_display(color_counts: dict[Color, int], font, surface):
    for i, (color, amount) in enumerate(color_counts.items()):
        text = font.render(f"{color.name.capitalize()} : {amount}", True, (50, 50, 50))
        surface.blit(text, (0, i * font.get_linesize() + 10))


if __name__ == "__main__":


    widow_size = (width, height) = (700, 700)
    framerate = 144
    ball_speed = 1.5
    ball_amount = 50
    screen = pygame.display.set_mode(widow_size)
    clock = pygame.time.Clock()

    # Init simulation here
    current_simulation = Simulation(ball_amount, widow_size)

    pygame.init()
    font = pygame.font.Font('freesansbold.ttf', 32)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        dt = clock.tick(framerate)
        screen.fill((255, 255, 255))
        current_simulation.draw(screen)
        current_simulation.update(dt/10 * ball_speed)

        color_count_display(current_simulation.agents_counts, font, screen)
        pygame.display.update()












