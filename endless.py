import pygame
import sys
from random import *


pygame.init()
pygame.display.set_caption("TheCatcher: Worldwide Thievery Thrust")

screen=pygame.display.set_mode((600,750))
background= pygame.image.load("Slike\\pozadina_igrica.jpg").convert()


aktivnost_igrice=True
score=0
lives=3
        

class Pirat():
    def __init__(self):
        # self.pirat_image=pygame.image.load("Slike\\likpirata.png").convert_alpha()
        self.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\likpirata.png"), (120, 120)).convert_alpha()
        self.pirat_rect=self.pirat_image.get_rect(midbottom= (300, 650))
        

        self.kretanje_desno=False
        self.kretanje_lijevo=False
        self.jump=False

        self.brzina= 2
        self.gravity= 5
        self.jump_height= 15

    def kretanje_komande(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.kretanje_desno = True
        if keys[pygame.K_LEFT]:
            self.kretanje_lijevo = True
        # if event.type == pygame.KEYDOWN: 
        if keys[pygame.K_SPACE]:
            self.jump = True
    
    def kretanje_ekran(self):
        if self.kretanje_desno and self.pirat_rect.right < 650:
            self.pirat_rect.x += self.brzina
            self.kretanje_desno=False
        if self.kretanje_lijevo and self.pirat_rect.left > -50:
            self.pirat_rect.x -= self.brzina
            self.kretanje_lijevo=False
        if  self.jump:
            self.pirat_rect.y -= self.gravity
            self.gravity -= 2                 
            if self.gravity < -self.jump_height:
                self.jump=False
                self.gravity=self.jump_height

                screen.blit(self.pirat_image, self.pirat_rect)
		    
            if self.pirat_rect.bottom >= 650:
                self.pirat_rect.bottom = 650

    def update(self):
        self.kretanje_komande()
        self.kretanje_ekran()
        
    
    def draw(self):
        screen.blit(self.pirat_image, self.pirat_rect)

class Novcic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.novcic_slika=pygame.image.load("Slike\\slikacoin.png").convert_alpha()
        self.novcic_rect=self.novcic_slika.get_rect(midtop= (randint(150, 450), -50))

        self.brzina_dropa=1

    def update(self):
        self.novcic_rect.y += self.brzina_dropa
        

    def draw(self):
        screen.blit(self.novcic_slika, self.novcic_rect)


player=Pirat()
objekti=pygame.sprite.Group()


def sudar_sprite(novcic_rect):
    if player.pirat_rect.colliderect(novcic_rect):
        return True
    else: 
        return False

def drop_novcici():
    if len(objekti) == 0:
        novi_novcic = Novcic()
        objekti.add(novi_novcic)

    if score>=10:
        if len(objekti) == 1:
            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 300:
                    novi_novcic = Novcic()
                    objekti.add(novi_novcic)
    if score>=20:
        for objekt in objekti.sprites():
            objekt.brzina_dropa=1.5
    
    if score>=30:
        if len(objekti) == 2:
            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 550:
                    novi_novcic = Novcic()
                    objekti.add(novi_novcic)
    
    if score>=40:
        for objekt in objekti.sprites():
            objekt.brzina_dropa=2
        
    if score>=50:
        if len(objekti) == 3:
            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 450:
                    novi_novcic = Novcic()
                    objekti.add(novi_novcic)

    if score>=60:
        for objekt in objekti.sprites():
            objekt.brzina_dropa=3


    
    for objekt in objekti.sprites():
        if objekt.novcic_rect.bottom > 660:
            objekti.remove(objekt)
    

    
        

# player = pygame.sprite.GroupSingle()
# player.add(Pirat())

# objekt = pygame.sprite.GroupSingle()

while True:
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    exit()

    if aktivnost_igrice:
        screen.blit(background, (0,0))

        player.draw()
        player.update()

        drop_novcici()
        for novcic in objekti.sprites():
            novcic.draw()
            novcic.update()


            if sudar_sprite(novcic.novcic_rect)==True:
                score+=1
                aktivnost_igrice=True
                objekti.remove(novcic)
            else:
                if novcic.novcic_rect.bottom > 660:
                    lives-=1
                    if lives==0:
                        aktivnost_igrice=False
                    else:
                        aktivnost_igrice=True


            print (score)
            print (lives)


        
                    
    
    pygame.display.update()











    



    

    

        



    