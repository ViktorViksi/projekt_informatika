import pygame
import sys
from random import *



class Gumb: #Klasa koja omogućuje bolju verziju gumba
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

    def update(self,screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self,position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

#Još moram nadodati ulogiranje kao prvi pop up

pygame.init()
screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption("Menu")
menu_surface = pygame.image.load("Slike/Pozadina_menu.png").convert()
test_font = pygame.font.Font(None, 50) #Moram pronaći neki dobar Font/ napraviti
#S ostalima se dogovoriti za Logo

def main_menu(): #Iz ovoga dalje biramo druge "prozore". Moram napraviti animaciju i uskladiti dizajn s njom.
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(menu_surface, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_tekst = test_font.render("MAIN MENU",True, "Black")
        menu_rect = menu_tekst.get_rect(center = (300, 100))

        #Gumb(image, pos, text_input, font, base_color, hovering_color)
        PLAY_BUTTON =  Gumb(pygame.image.load("Slike/Pozadina_gumb.png").convert(), (300, 300), "PLAY", test_font,"Black", "White")
        OPTIONS_BUTTON = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300,400),"OPTIONS", test_font, "Black", "White")
        ACHIVMENT_BUTTON = Gumb(pygame.image.load("Slike/Pozadina_gumb3.png").convert(), (300,500),"ACHIVMENT", test_font, "Black", "White")
        QUIT_BUTTON = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 600), "QUIT", test_font, "Black", "White")

        screen.blit(menu_tekst,menu_rect)

        for gumb in [PLAY_BUTTON, OPTIONS_BUTTON, ACHIVMENT_BUTTON, QUIT_BUTTON]:
            gumb.changeColor(MENU_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if ACHIVMENT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    achivment()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def play(): #Ovdje vi nadodajete svoj dio za sami aspekt igrice. Tu se odvija radnja
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("White") #Najvjerojatnije ću kasnije probati sa clear
        map_surf = pygame.image.load("Slike/Mapa2.png").convert()
        map_rect = map_surf.get_rect(topleft = (0, 70))
        screen.blit(map_surf, map_rect)

        play_tekst = test_font.render("MAPA SVIJETA", False, "Black")
        play_rect = play_tekst.get_rect(center = (300,50))
        screen.blit(play_tekst, play_rect)

        PLAY_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb4.png").convert(),(300, 700), "Vrati se", test_font, "White", "Green")
        PLAY_IGRA = Gumb(pygame.image.load("Slike/Pozadina_gumb4.png").convert(),(300, 600), "IGRAJ", test_font, "White", "Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        PLAY_IGRA.changeColor(PLAY_MOUSE_POS)
        PLAY_IGRA.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if PLAY_IGRA.checkForInput(PLAY_MOUSE_POS):
                    igra()
        pygame.display.update()


def options(): #Moram nadodati za smanjivanje muzike i zvukova + možda i objašnjenje za kontrole/radnju
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Black")

        opcije_tekst = test_font.render("Ovdje su opcije",False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 300))
        screen.blit(opcije_tekst, opcije_rect)

        OPTIONS_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb5.png").convert(), (300, 500), "Vrati se", test_font, "White", "Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()
        pygame.display.update()


#Moramo se dogovoriti za achivmente koje da ovdje stavim. Za sada moram realizirati onu lijepu strukturu i logo za njih.
# + osmisliti način rada achivmenta s razvojnim programerom
def achivment(): 
    while True:
        ACHIVMENT_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Black")

        achivment_tekst = test_font.render("Ovdje su achivmenti",False, "White")
        achivment_rect = achivment_tekst.get_rect(center = (300, 300))
        screen.blit(achivment_tekst, achivment_rect)

        ACHIVMENT_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300, 500),"Vrati se", test_font, "White", "Green")

        ACHIVMENT_BACK.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACHIVMENT_BACK.checkForInput(ACHIVMENT_MOUSE_POS):
                    main_menu()
        pygame.display.update()

def igra():



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
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu()

        
        if aktivnost_igrice:
            screen.blit(background, (0,0))

            player.draw()
            player.update()
            OPTIONS_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb5.png").convert(), (500, 200), "Vrati se", test_font, "White", "Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(screen)


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





main_menu()
                


        