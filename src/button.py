import pygame
import os

pygame.init()
pygame.mixer.init()
base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))

os.environ['SDL_VIDEO_CENTERED'] = '1' 
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width, screen_height - 10

SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width
SCREEN = pygame.display.set_mode((window_width, window_height), pygame.RESIZABLE)
pygame.display.set_caption("Dino Adventure")

BUTTON_CLICK_SOUND = pygame.mixer.Sound(os.path.join(base_path, "Assets", "Sounds", "button_click.mp3"))

class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                self.clicked = True
                BUTTON_CLICK_SOUND.play()
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))
        return action

    def is_hovered(self):
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)
