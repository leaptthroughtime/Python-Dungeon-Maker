# Dungeon Generator in Python 3
# By @LeaptThroughTime
# Description: A random dungeon generator for D&D

import sys
import pygame
from pygame.locals import *
import random
from typing import List
from itertools import tee, islice, chain

STEPS = 100
DISPLAY_WIDTH = 600
DISPLAY_LENGTH = 600
FPS = 30

COLOR = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0)
}


class DungeonGenerator:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display_size = (DISPLAY_WIDTH, DISPLAY_LENGTH)
        self.display = pygame.display.set_mode(self.display_size)
        self.display_origin = (DISPLAY_WIDTH / 2, DISPLAY_LENGTH / 2)
        self.walker_location = self.display_origin
        self.walker_size = 10
        self.walker_speed = 15
        self.walker_list = []
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
            pygame.display.update()
            self.clock.tick(FPS)
        self.wait()

    def generate_Path(self):
        self.walker_list.append(self.walker_location)
        for i in range(STEPS):
            self.walker_location = self.get_direction()
            self.walker_list.append(self.walker_location)

    def get_direction(self) -> int:
        direction = random.randint(1, 4)
        match direction:
            case 1:
                return (self.walker_location[0],
                        self.walker_location[1] + self.walker_size)
            case 2:
                return (self.walker_location[0] + self.walker_size,
                        self.walker_location[1])
            case 3:
                return (self.walker_location[0],
                        self.walker_location[1] - self.walker_size)
            case 4:
                return (self.walker_location[0] - self.walker_size,
                        self.walker_location[1])

    def previous_and_next(self) -> tuple:
        prevs, items, nexts = tee(self.walker_list, 3)
        prevs = chain([None], prevs)
        nexts = chain(islice(nexts, 1, None), [None])
        return zip(prevs, items, nexts)

    def reset(self):
        self.display.fill(COLOR['black'])
        self.walker_location = self.display_origin
        self.walker_list = []
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
