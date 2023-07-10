import pygame
from pygame.locals import *
import random


class Walker():
    def __init__(self, x, y, size, screen_width, screen_height):
        self.x = x
        self.y = y
        self.size = size
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        self.direction = random.choice(["up", "down", "left", "right"])
        if self.direction == "up":
            self.y -= self.size
        elif self.direction == "down":
            self.y += self.size
        elif self.direction == "left":
            self.x -= self.size
        elif self.direction == "right":
            self.x += self.size

        self.check_collision()

    def check_collision(self):
        if self.x < 0 or self.x >= self.screen_width or self.y < 0 or self.y >= self.screen_height:
            self.direction = self.choose_new_direction()

    def choose_new_direction(self):
        available_directions = []
        if self.x > 0:
            available_directions.append("left")
        if self.x < self.screen_width - self.size:
            available_directions.append("right")
        if self.y > 0:
            available_directions.append("up")
        if self.y < self.screen_height - self.size:
            available_directions.append("down")

        return random.choice(available_directions)

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.size, self.size))
