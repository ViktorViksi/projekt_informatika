import pygame
from random import *
import time


pygame.init()
pygame.display.set_caption("TheCatcher: Worldwide Thievery Thrust")

screen=pygame.display.set_mode((600,750))
background= pygame.image.load("Slike\\levelAustralija.png").convert()


aktivnost_igrice=True
score=0
        

class Pirat():
    def __init__(self):
        # self.pirat_image=pygame.image.load("Slike\\likpirata.png").convert_alpha()
        self.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\likpirata.png"), (110, 180)).convert_alpha()
        self.pirat_rect=self.pirat_image.get_rect(midbottom= (300, 700))
        

        self.kretanje_desno=False
        self.kretanje_lijevo=False
        self.jump=False

        self.brzina= 1
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
		    
        if self.pirat_rect.bottom >= 700:
            self.pirat_rect.bottom = 700

    def update(self):
        self.kretanje_komande()
        self.kretanje_ekran()
        
    
    def draw(self):
        screen.blit(self.pirat_image, self.pirat_rect)

class Novcic(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelAustralija.png"), (40,40)).convert_alpha()
        # if broj_levela==1:
            
        # elif broj_levela==2:
        #     self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelBrazil.png"), (40,40)).convert_alpha()
        # elif broj_levela==3:
        #     self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelAntarktika.png"), (40,40)).convert_alpha()
        # elif broj_levela==4:
        #     self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelEgipat.png"), (40,40)).convert_alpha()
        # elif broj_levela==5:
        #     self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelPariz.png"), (50,50)).convert_alpha()
        # elif broj_levela==6:
        #     self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelKina.png"), (50,50)).convert_alpha()
        # elif broj_levela==7:
        #     self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\novciclevelAustralija.png"), (40,40)).convert_alpha()
        
        self.novcic_rect=self.novcic_slika.get_rect(midtop= (randint(150, 450), -60))

        self.brzina_dropa=1

        self.specialbroj=0

    def update(self):
        self.novcic_rect.y += self.brzina_dropa

        

    def draw(self):
        screen.blit(self.novcic_slika, self.novcic_rect)


player=Pirat()
objekti=pygame.sprite.Group()
specials=pygame.sprite.Group()
pocetno_vrijeme=time.time()
zavrsno_vrijeme=0
vrijednost_novcica=1
pocetak=0
ukupno=0


def sudar_sprite(novcic_rect):
    if player.pirat_rect.colliderect(novcic_rect):
        return True
    else: 
        return False

def drop_novcici():
    global ukupno
    if len(objekti) == 0:
        novi_novcic = Novcic()
        objekti.add(novi_novcic)

    if ukupno>=1:
        if len(objekti) == 1:
            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 300:
                    novi_novcic = Novcic()
                    objekti.add(novi_novcic)

    if ukupno>=5:
        for objekt in objekti.sprites():
            objekt.brzina_dropa=1.2


    if ukupno>=10:
        if len(objekti) == 2:
            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 550:
                    novi_novcic = Novcic()
                    objekti.add(novi_novcic)
    
    if ukupno>=25:
        for objekt in objekti.sprites():
            objekt.brzina_dropa=1.4

    if ukupno>=30:
        if len(objekti) == 3:
            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 450:
                    novi_novcic = Novcic()
                    objekti.add(novi_novcic)
    if ukupno>=60:
            for objekt in objekti.sprites():
                objekt.brzina_dropa=1.8

    for objekt in objekti.sprites():
            if objekt.novcic_rect.bottom > 700:
                objekti.remove(objekt)
                ukupno+=1
  
        
def specials_drop():
    if len(specials) == 0:
        rendom=randint(1,5)
        
        if rendom == 1:
            special=Novcic()
            specials.add(special)
            special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\doublespecial.png"), (40,40)).convert_alpha()
            special.specialbroj=1


        elif rendom == 2:
            special=Novcic()
            specials.add(special)
            special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\freezespecial.png"), (40,40)).convert_alpha()
            special.specialbroj=2


        elif rendom == 3:
            special=Novcic()
            specials.add(special)
            special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\povecanjespecial.png"), (40,40)).convert_alpha()
            special.specialbroj=3


        elif rendom == 4:
            special=Novcic()
            specials.add(special)
            special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\smanjenjespecial.png"), (40, 40)).convert_alpha()
            special.specialbroj=4


        elif rendom == 5:
            special=Novcic()
            specials.add(special)
            special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike\\speedspecial.png"), (40, 40)).convert_alpha()
            special.specialbroj=5

        
def postotak():
    return(f"{(score/ukupno)*100}%")



def specials_radnja():
    global vrijednost_novcica
    for special in specials.sprites():
        if special.specialbroj== 1:
            vrijednost_novcica=2
        elif special.specialbroj == 2:
            player.brzina=0
            player.jump_height=0
            player.gravity=0
            player.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\freezelikpirata.png"), (110, 180)).convert_alpha()
        elif special.specialbroj == 3:
            player.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\likpirata.png"), (220, 360)).convert_alpha()
        elif special.specialbroj == 4:
            player.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\likpirata.png"), (55, 90)).convert_alpha()
        elif special.specialbroj == 5:
            player.brzina=3
            player.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\speedlikpirata.png"), (110, 180)).convert_alpha()



# player = pygame.sprite.GroupSingle()
# player.add(Pirat())

# objekt = pygame.sprite.GroupSingle()

while True:
    for event in pygame.event.get():
	    if event.type == pygame.QUIT:
		    pygame.quit()
		    exit()
    # odabir_pozadine(broj_levela)
    if aktivnost_igrice:
        screen.blit(background, (0,0))

        player.draw()
        player.update()
        
        drop_novcici()
        for novcic in objekti.sprites():
            novcic.draw()
            novcic.update()


            if sudar_sprite(novcic.novcic_rect)==True:
                if novcic in objekti.sprites():
                    score=score+vrijednost_novcica
                    aktivnost_igrice=True
                    ukupno+=1
                    objekti.remove(novcic)

    
        
        zavrsno_vrijeme=time.time()

        if zavrsno_vrijeme-pocetno_vrijeme>20:
            specials_drop()
            
        if len(specials)>0:
            for special in specials.sprites():
                special.draw()
                special.update()

            if sudar_sprite(special.novcic_rect)==True:
                specials_radnja()
            
                pocetak=time.time()
                pocetno_vrijeme=zavrsno_vrijeme
                zavrsno_vrijeme=0
                
                for special in specials.sprites():
                    specials.remove(special)



                                    
        for special in specials.sprites():
            if special.novcic_rect.bottom > 700:
                specials.remove(special)
                pocetno_vrijeme=zavrsno_vrijeme
                zavrsno_vrijeme=0
                


        if time.time()-pocetak>=6:
            vrijednost_novcica=1
            player.brzina=1
            player.jump_height=15
            player.gravity=5
            player.pirat_image=pygame.transform.scale(pygame.image.load("Slike\\likpirata.png"), (110, 180)).convert_alpha()
            pocetak=time.time()
        

        if ukupno>=100:
            aktivnost_igrice=False
            print(postotak())

    pygame.display.update()
    


        








