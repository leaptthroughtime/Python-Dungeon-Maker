# Dungeon Generator in Python 3
# By @LeaptThroughTime
# Description: A random dungeon generator for D&D

import pygame
from Walker import Walker
from pygame.locals import *

COLOR = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0)
}


class DungeonGenerator:
    def __init__(self, screen_width, screen_height, walker_steps):
        pygame.init()

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.walker_steps = walker_steps

        self.window = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("@LeaptThroughTime's Dungeon Generator")

        self.clock = pygame.time.Clock()
        self.running = False
        self.paused = False
        self.walker = None
        self.step_counter = 0
        self.trail = []

    def start(self):
        self.running = True
        self.paused = False
        self.step_counter = 0
        self.walker = Walker(self.screen_width // 2, self.screen_height // 2, 10, self.screen_width, self.screen_height)
        self.trail = []

        while self.running:
            self.handle_events()

            if not self.paused and self.step_counter < self.walker_steps:
                self.walker.move()
                self.step_counter += 1
                self.trail.append((self.walker.x, self.walker.y))

            self.draw()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_q or event.key == K_ESCAPE)):
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.paused = not self.paused
                elif event.key == K_RETURN and (self.paused or self.step_counter >= self.walker_steps):
                    self.start()
                elif event.key == K_p:
                    self.export_screenshot()

    def draw(self):
        self.window.fill((0, 0, 0))  # Clear the screen

        if self.walker:
            self.walker.draw(self.window)

        for trail_pos in self.trail:
            pygame.draw.rect(self.window, (255, 255, 255), (trail_pos[0], trail_pos[1], self.walker.size, self.walker.size))

        # Draw step counter in the top left corner
        font = pygame.font.Font(None, 24)
        text = font.render("Steps: {}".format(self.step_counter), True, COLOR["white"])
        self.window.blit(text, (10, 10))

    def export_screenshot(self):
        pygame.image.save(self.window, "screenshot.png")
        print("Screenshot saved as screenshot.png")


if __name__ == "__main__":
    dungeon_generator = DungeonGenerator(800, 600, 1000)
    dungeon_generator.start()
