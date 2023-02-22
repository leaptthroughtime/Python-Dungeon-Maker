# Dungeon Generator in Python 3
# By @LeaptThroughTime
# Description: A random dungeon generator for D&D

import pygame
import random

pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)

dis_width=600
dis_length=600
dis_size=(dis_width, dis_length)

dis_origin=(origin_x, origin_y)
walker_size=10
walker_speed=15
clock = pygame.time.Clock()

dis=pygame.display.set_mode(dis_size)

pygame.display.update()
pygame.display.set_caption("@LeaptThroughTime's Dungeon Generator")

def walkerPath(walker_size, walker_list):
    for x in walker_list:
        pygame.draw.rect(dis, black, [x[0], x[1], walker_size, walker_size])

def gameLoop():
    game_over=False
    game_close=False

    origin_x=dis_width/2
    origin_y=dis_length/2

    walker_list = []
    walker_length = 1

    

    while not game_over:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True
        dis.fill(white)
        pygame.draw.rect(dis,black,[origin_x,origin_y,walker_size,walker_size])
        pygame.display.update()

    pygame.quit()
    quit()