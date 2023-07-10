import pygame
from pygame.locals import *


class EventHandler:
    def __init__(self):
        pygame.init()

        self.window_width, self.window_height = 800, 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Event Handler Example")

        self.clock = pygame.time.Clock()
        self.running = False

    def handle_events(self):
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == ACTIVEEVENT:
                    self.handle_active_event(event)
                else:
                    self.handle_event(event)

            self.update()
            self.draw()
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()

    def handle_event(self, event):
        # Override this method to handle specific events
        pass

    def handle_active_event(self, event):
        if event.gain == 0:  # Focus lost
            self.handle_focus_lost()
        else:  # Focus gained
            self.handle_focus_gained()

    def handle_focus_lost(self):
        # Override this method to handle focus lost event
        pass

    def handle_focus_gained(self):
        # Override this method to handle focus gained event
        pass

    def update(self):
        # Override this method for game logic updates
        pass

    def draw(self):
        # Override this method for drawing game graphics
        pass