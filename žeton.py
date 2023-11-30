import pygame
import random
from pygame.sprite import Sprite

class Jaje(Sprite):
    def __init__(self, speed, image):
        super().__init__()
        screen = pygame.display.set_mode((600, 750))
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect.x = random.randrange(20, self.screen_rect.right-30)
        self.rect.y = 0
        self.y = float(self.rect.y)

        self.brzina = speed

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()

    def update(self):
        self.y += self.brzina
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)
