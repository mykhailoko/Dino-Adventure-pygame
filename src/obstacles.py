import pygame
import os
import random
from assets import *

pygame.init()

os.environ['SDL_VIDEO_CENTERES'] = '1'
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width - 3, screen_height - 60

SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width


class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, obstacles, game_speed):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)


class Zombi(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 410
        self.index = 0

    def update(self, obstacles, game_speed):
        self.rect.x -= (game_speed + 2)
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1


class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 435


class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 410


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 300
        self.index = 0

    def update(self, obstacles, game_speed):
        self.rect.x -= (game_speed + 5)
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1
