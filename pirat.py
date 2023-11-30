import pygame

class Košarica:
    def __init__(self, image):
        screen = pygame.display.set_mode((600, 750))
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.brzina = 10
        self.x = float(self.rect.x)
        self.desno = False
        self.lijevo = False

        self.slika = pygame.image.load(image).convert_alpha()
        self.rect = self.slika.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

    def changeSpeed(self, x):
        self.brzina = x
        
    def update(self):
        if self.desno and self.rect.right < self.screen_rect.right:
            self.x += self.brzina
        if self.lijevo and self.rect.left > 0:
            self.x -= self.brzina
        self.rect.x = self.x

    def draw(self):
        self.screen.blit(self.image, self.rect)