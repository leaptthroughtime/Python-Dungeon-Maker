# Dungeon Generator in Python 3
# By @LeaptThroughTime
# Description: A random dungeon generator for D&D
import pygame
import random
import time

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

display_x = 800
display_y = 800
display = pygame.display.set_mode((display_x, display_y))

origin_x = display_x / 2
origin_y = display_y / 2
origin = (origin_x, origin_y)

pygame.display.update()
pygame.display.set_caption("@LeaptThroughTime 's Dungeon Generator")

clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [display_x / 2, display_y / 2])

def walk(walk_x, walk_y, squareSize):
    direction = random.randint(1, 4)
    if direction == 1:
        walk_y += 1
    elif direction == 2:
        walk_y -= 1
    elif direction == 3:
        walk_x += 1
    else:
        walk_x -= 1

def gameLoop(origin_x, origin_y):
    walk_x = origin_x
    walk_y = origin_y
    squareSize = 10
    
    #dungeon_coords = []
    pygame.draw.rect(display, black, [walk_x, walk_y, squareSize, squareSize]) #default starting block

    for i in range(100):
        walk(walk_x, walk_y, squareSize)
        display.fill(white)
        pygame.draw.rect(display, black, [walk_x, walk_y, squareSize, squareSize])
        pygame.display.update()

    clock.tick(30)

    time.sleep(5)

gameLoop(origin_x, origin_y)