# Dungeon Generator in Python 3
# By @LeaptThroughTime
# Description: A random dungeon generator for D&D

import sys
import pygame
from pygame.locals import *
import random
from typing import List
from itertools import tee, islice, chain

STEPS = 1000
DISPLAY_WIDTH = 600
DISPLAY_LENGTH = 600
FPS = 24

COLOR = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0)
}


class DungeonGenerator:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.clock = pygame.time.Clock()
        self.display_size = (DISPLAY_WIDTH, DISPLAY_LENGTH)
        self.display = pygame.display.set_mode(self.display_size)
        self.display_origin = (DISPLAY_WIDTH / 2, DISPLAY_LENGTH / 2)
        self.walker_location = self.display_origin
        self.walker_size = 10
        self.walker_speed = 15
        self.walker_list = []
        self.step_count = 0
        self.font = pygame.font.Font(None, 36)
        self.step_text = self.font.render(f'Steps: {self.step_count}',
                                          True, COLOR["white"])
        pygame.display.update()
        pygame.display.set_caption("@LeaptThroughTime's Dungeon Generator")
        self.path = self.generate_Path()

    def walk(self) -> List[int]:
        for previous, item, nxt in self.previous_and_next():
            if previous is not None:
                pygame.draw.rect(self.display, COLOR['white'],
                                 [previous[0], previous[1],
                                 self.walker_size, self.walker_size])
            pygame.draw.rect(self.display, COLOR['red'],
                             [item[0], item[1],
                              self.walker_size, self.walker_size])
            self.step_text = self.font.render(f'Steps: {self.step_count}',
                                              True, COLOR["white"])
            self.erase_count()
            self.display.blit(self.step_text, (10, 10))
            self.step_count += 1
            pygame.display.update()
            self.clock.tick(FPS)
        self.wait()

    def generate_Path(self):
        self.walker_list.append(self.walker_location)
        for i in range(STEPS):
            self.walker_location = self.get_direction()
            self.walker_list.append(self.walker_location)

    def get_direction(self) -> int:
        off_screen = False
        while not off_screen:
            direction = random.randint(1, 4)
            match direction:
                case 1:
                    new_location = (self.walker_location[0],
                                    self.walker_location[1] + self.walker_size)
                    if self.is_on_screen(new_location):
                        return new_location
                case 2:
                    new_location = (self.walker_location[0] + self.walker_size,
                                    self.walker_location[1])
                    if self.is_on_screen(new_location):
                        return new_location
                case 3:
                    new_location = (self.walker_location[0],
                                    self.walker_location[1] - self.walker_size)
                    if self.is_on_screen(new_location):
                        return new_location
                case 4:
                    new_location = (self.walker_location[0] - self.walker_size,
                                    self.walker_location[1])
                    if self.is_on_screen(new_location):
                        return new_location

    def is_on_screen(self, location: tuple) -> bool:
        if location[0] not in range(0, DISPLAY_WIDTH) or location[1] not in range(0, DISPLAY_LENGTH):
            return False
        return True

    def previous_and_next(self) -> tuple:
        prevs, items, nexts = tee(self.walker_list, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])
        return zip(prevs, items, nexts)

    def erase_count(self) -> None:
        self.display.fill(COLOR['black'], (0, 0, 200, 100))

    def reset(self):
        self.display.fill(COLOR['black'])
        self.walker_location = self.display_origin
        self.walker_list = []
        self.step_count = 0
        self.generate_Path()
        self.walk()

    def wait(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_q or event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_SPACE:
                        self.reset()


if __name__ == "__main__":
    dg = DungeonGenerator()
    dg.walk()
