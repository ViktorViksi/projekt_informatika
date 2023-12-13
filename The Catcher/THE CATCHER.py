import pygame
import sys
from gumb import Gumb
from random import *
import time

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 750))

pygame.display.set_caption("Login")
menu_surface = pygame.image.load("Slike/Menu/Pozadina_menu.png").convert()
test_font = pygame.font.Font(None, 50) #Moram pronaći neki dobar Font/ napraviti
naslov_font = pygame.font.Font(None, 150)
podnaslov_font = pygame.font.Font(None, 100)


zvuk = 0.5
zvuk2 = 0.5
bg_music = pygame.mixer.Sound("Audio/He's a Pirate.mp3")
bg_music.set_volume(zvuk)
bg_music.play(loops= -1)
click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
click_sound.set_volume(zvuk2)
stisnut = 0
stisnut2 = 0

with open("login_podaci.txt", encoding="utf-8") as datoteka:
    podaci = datoteka.readlines()
    for i in range(len(podaci)):
        podaci[i].split(" ")

def login():
    user_text = ""
    
    global podaci
    global data
    
    input_rect = pygame.Rect(145,300,310,45)
    color_active = pygame.Color("lightskyblue3")  #može i rgb
    color_passive = pygame.Color("gray15")
    color = color_passive

    active = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_text =  user_text[0:-1]
                    else:
                        if len(user_text) <= 10:
                            user_text += event.unicode
                        
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if LOGIN_BACK.checkForInput(LOGIN_MOUSE_POS):
                        for i in range(len(podaci)):
                            if user_text.upper() == podaci[i][0]:
                                data = i
                                main_menu()
                        podaci.append([user_text.upper(), "0", "00llllll"]) #ovo ce bit nacin zapisivanja podataka al nije gotov
                        data = len(podaci)-1
                        main_menu()
                        



        screen.fill("White")

        LOGIN_MOUSE_POS = pygame.mouse.get_pos()


        LOGIN_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb7.png").convert(), (300, 400),"Prijavi se", test_font, "Black", "Gray")

        LOGIN_BACK.changeColor(LOGIN_MOUSE_POS)
        LOGIN_BACK.update(screen)    



        if active:
            color = color_active
        else:
            color = color_passive
        pygame.draw.rect(screen,color,input_rect, 2)

        text_srurface = test_font.render(user_text,True, "Green")
        
        screen.blit(text_srurface, (input_rect.x +5,input_rect.y +5))


        pygame.display.update()


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


class Scroll():
    def __init__(self, image_line, pos_line, image_button,):
        self.image_line = image_line
        self.x_pos_line = pos_line[0]
        self.y_pos_line = pos_line[1]
        self.image_button = image_button
        self.x_pos_button = self.x_pos_line
        self.y_pos_button = self.y_pos_line
        self.rect_line = self.image_line.get_rect(midleft = (self.x_pos_line, self.y_pos_line))
        self.rect_button = self.image_button.get_rect(center = (self.x_pos_button, self.y_pos_button))
        


    def update(self,screen):
        screen.blit(self.image_line, self.rect_line)

    def checkForInput1(self,position):
        if position[0] in range(self.rect_line.left +10, self.rect_line.right-9) and position[1] in range(self.rect_line.top, self.rect_line.bottom):
            return True
        return False


    def changeButtonPosition(self,position, screen, zvuk):
        self.jump_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
        self.jump_sound.set_volume(0.5)
        self.x_pos_button = int(position[0])
        self.rect_button = self.image_button.get_rect(center = (self.x_pos_button, self.y_pos_button))
        screen.blit(self.image_button, self.rect_button)
        if pygame.mouse.get_pressed()[0]:
            print(position)
            return True


def pause_options(scrn, oldScreen):
    test_font = pygame.font.Font(None, 50)
    naslov_font = pygame.font.Font(None, 150)
    podnaslov_font = pygame.font.Font(None, 100)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(128)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))
    while True:
        global zvuk
        global stisnut
        global zvuk2
        global stisnut2

        scrn.blit(s, (20,20))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        

        opcije_tekst = naslov_font.render("Opcije" ,False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 60))
        screen.blit(opcije_tekst, opcije_rect)


        muzika_tekst = podnaslov_font.render("Muzika" ,False, "Gray")
        muzika_rect = muzika_tekst.get_rect(center = (200, 230))
        screen.blit(muzika_tekst, muzika_rect)

        racun = round(zvuk,2)*100
        zvuk_tekst = test_font.render(f"{round(racun)}%",False, "Black")
        zvuk_rect = zvuk_tekst.get_rect(center = (500, 300))
        pygame.draw.rect(screen, "White", zvuk_rect)
        pygame.draw.rect(screen, "Brown", zvuk_rect,2)
        screen.blit(zvuk_tekst, zvuk_rect)


        efekt_tekst = podnaslov_font.render("Zvučni efekti" ,False, "Gray")
        efekt_rect = efekt_tekst.get_rect(center = (270, 430))
        screen.blit(efekt_tekst, efekt_rect)


        racun2 = round(zvuk2,2)*100
        zvuk2_tekst = test_font.render(f"{round(racun2)}%",False, "Black")
        zvuk2_rect = zvuk2_tekst.get_rect(center = (500, 500))
        pygame.draw.rect(screen, "White", zvuk2_rect)
        pygame.draw.rect(screen, "Brown", zvuk2_rect,2)
        screen.blit(zvuk2_tekst, zvuk2_rect)

        OPTIONS_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb5.png").convert(), (100, 700), "Vrati se", test_font, "White", "Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

        OPTIONS_SOUND = Scroll(pygame.image.load("Slike/Menu/Scol_linija1.png").convert(), (100, 300), pygame.image.load("Slike/Menu/Scrol_gumb.png").convert())
        
        OPTIONS_SOUND.update(screen)

        OPTIONS_SOUND2 = Scroll(pygame.image.load("Slike/Menu/Scol_linija1.png").convert(), (100, 500), pygame.image.load("Slike/Menu/Scrol_gumb.png").convert())
        
        OPTIONS_SOUND2.update(screen)

        if stisnut == 0:
            OPTIONS_MUSIC = Gumb(pygame.image.load("Slike/Menu/Unmute.png").convert(), (50, 300), "", test_font, "White", "Green")
            OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC.update(screen)
        else:
            OPTIONS_MUSIC = Gumb(pygame.image.load("Slike/Menu/Mute.png").convert(), (50, 300), "", test_font, "White", "Green")
            OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC.update(screen)

        if stisnut2 == 0:
            OPTIONS_MUSIC2 = Gumb(pygame.image.load("Slike/Menu/Unmute.png").convert(), (50, 500), "", test_font, "White", "Green")
            OPTIONS_MUSIC2.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC2.update(screen)
        else:
            OPTIONS_MUSIC2 = Gumb(pygame.image.load("Slike/Menu/Mute.png").convert(), (50, 500), "", test_font, "White", "Green")
            OPTIONS_MUSIC2.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC2.update(screen)


        if OPTIONS_SOUND.checkForInput1(OPTIONS_MOUSE_POS):  
            if OPTIONS_SOUND.changeButtonPosition(OPTIONS_MOUSE_POS, screen, zvuk):
                zvuk = (OPTIONS_MOUSE_POS[0]- 110)/280
                bg_music.set_volume(zvuk)
                pygame.mixer.unpause()
                stisnut = 0

        if OPTIONS_SOUND2.checkForInput1(OPTIONS_MOUSE_POS):  
            if OPTIONS_SOUND2.changeButtonPosition(OPTIONS_MOUSE_POS, screen, zvuk):
                zvuk2 = (OPTIONS_MOUSE_POS[0]- 110)/280
                print(racun2)
                click_sound.set_volume(zvuk2)
                stisnut2 = 0





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    scrn.blit(oldScreen, (0,0))
                    pause_menu()
                if OPTIONS_MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                    if zvuk == 0:
                        zvuk = 0.5
                        pygame.mixer.unpause()
                        bg_music.set_volume(zvuk)
                        stisnut = 0
                    else:
                        zvuk = 0
                        pygame.mixer.pause()
                        stisnut = 1
                if OPTIONS_MUSIC2.checkForInput(OPTIONS_MOUSE_POS):
                    if zvuk2 == 0:
                        zvuk2 = 0.5
                        click_sound.set_volume(zvuk2)
                        print(zvuk2)
                        stisnut2 = 0
                    else:
                        zvuk2 = 0
                        click_sound.set_volume(zvuk2)
                        print(zvuk2)
                        stisnut2 = 1

        pygame.display.update()
    
    
def ispis(lista):
    with open("login_podaci.txt", "wt" ,encoding="utf-8") as datoteka:
        datoteka.writelines(lista)


def pause_menu(scrn, score):
    test_font = pygame.font.Font(None, 50)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(128)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))
    
    nastavi = False

    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        pause_tekst = test_font.render("PAUZIRANO",True, "Black")
        pause_rect = pause_tekst.get_rect(center = (300, 100))

        score_tekst = test_font.render(f"Current Score: {score}",True, "Black")
        score_rect = pause_tekst.get_rect(center = (285, 200))
        
        NASTAVI = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,400),"NASTAVI", test_font, "Black", "White")
        OPTIONS = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb3.png").convert(), (300,500),"OPTIONS", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Menu/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

        scrn.blit(pause_tekst,pause_rect)
        scrn.blit(score_tekst, score_rect)

        for gumb in [NASTAVI, OPTIONS, MENU, PAUSE_BACK]:
            gumb.changeColor(PAUSE_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NASTAVI.checkForInput(PAUSE_MOUSE_POS) or PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    nastavi = True
                if OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    pause_options(scrn, oldScreen)
                if MENU.checkForInput(PAUSE_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()
        
        if nastavi:
            break
    
    pygame.time.delay(1000)
    scrn.blit(oldScreen, (0,0))


def level_pause(scrn, score):
    test_font = pygame.font.Font(None, 50)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(128)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))
    
    nastavi = False

    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        pause_tekst = test_font.render("PAUZIRANO",True, "Black")
        pause_rect = pause_tekst.get_rect(center = (300, 100))

        score_tekst = test_font.render(f"Current Score: {score}",True, "Black")
        score_rect = pause_tekst.get_rect(center = (285, 200))
        
        NASTAVI = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,400),"NASTAVI", test_font, "Black", "White")
        OPTIONS = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb3.png").convert(), (300,500),"OPTIONS", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Menu/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

        scrn.blit(pause_tekst,pause_rect)
        scrn.blit(score_tekst, score_rect)

        for gumb in [NASTAVI, OPTIONS, MENU, PAUSE_BACK]:
            gumb.changeColor(PAUSE_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NASTAVI.checkForInput(PAUSE_MOUSE_POS) or PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    nastavi = True
                if OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    pause_options(scrn, oldScreen)
                if MENU.checkForInput(PAUSE_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()
        
        if nastavi:
            break
    
    pygame.time.delay(1000)
    scrn.blit(oldScreen, (0,0))


def game_over(scrn, score, hscore):
    test_font = pygame.font.Font(None, 50)
    s = pygame.Surface((560, 710))
    s.set_alpha(128)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))

    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        pause_tekst = test_font.render("GAME OVER",True, "Black")
        pause_rect = pause_tekst.get_rect(center = (300, 100))

        score_tekst = test_font.render(f"Current Score: {score}",True, "Black")
        score_rect = hscore_tekst.get_rect(center = (300, 200))
        
        hscore_tekst = test_font.render(f"Current Score: {hscore}",True, "Black")
        hscore_rect = hscore_tekst.get_rect(center = (300, 300))
        
        PONOVO = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,500),"IGRAJ PONOVO", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Menu/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

        scrn.blit(pause_tekst,pause_rect)
        scrn.blit(score_tekst, score_rect)

        for gumb in [PONOVO, MENU, PAUSE_BACK]:
            gumb.changeColor(PAUSE_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PONOVO.checkForInput(PAUSE_MOUSE_POS) or PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    endless()
                if MENU.checkForInput(PAUSE_MOUSE_POS):
                    main_menu()
                    
        pygame.display.update()


def level_start(scrn, brojLevela, type):
    test_font = pygame.font.Font(None, 50)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(128)
    s.fill((55, 71, 79))
    
    if type == "l":
        locked = True
    else:
        locked = False
    
    scrn.blit(s, (20,20))
    
    if brojLevela == 1:
        tekst = "LEVEL 1 - NEW YORK"
    elif brojLevela == 2:
        tekst = "LEVEL 2 - BUENOS AIRES"
    elif brojLevela == 3:
        tekst = "LEVEL 3 - PARIS"
    elif brojLevela == 4:
        tekst = "LEVEL 4 - SAHARA"
    elif brojLevela == 5:
        tekst = "LEVEL 5 - THE GREAT WALL"
    elif brojLevela == 6:
        tekst = "LEVEL 6 - AUSTRALIA"
    elif brojLevela == 7:
        tekst = "LEVEL 7 - ANTARCTICA"
    elif brojLevela == 8:
        tekst = "LEVEL BONUS - DALMACIJA"
    
    natrag = False
    
    if locked:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            intro_tekst = test_font.render(tekst,True, "Black")
            intro_rect = intro_tekst.get_rect(center = (300, 100))
            
            msg_tekst = test_font.render(f"Level je zaključan",True, "Black")
            msg_rect = msg_tekst.get_rect(center = (300, 200))
            
            NATRAG = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 550, "NATRAG", test_font, "Black", "White"))

            scrn.blit(intro_tekst,intro_rect)
            scrn.blit(msg_tekst, msg_rect)

            for gumb in [IGRAJ, NATRAG]:
                gumb.changeColor(MENU_MOUSE_POS)
                gumb.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NATRAG.checkForInput(MENU_MOUSE_POS):
                        natrag = True
            
            pygame.display.update()
            
            if natrag:
                break
        scrn.blit(oldScreen)
        
    else:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            intro_tekst = test_font.render(tekst,True, "Black")
            intro_rect = intro_tekst.get_rect(center = (300, 100))
            
            IGRAJ = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,450),"IGRAJ", test_font, "Black", "White")
            NATRAG = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 550), "NATRAG", test_font, "Black", "White")

            scrn.blit(intro_tekst,intro_rect)
            
            if type == 0:
                image = pygame.image.load("Slike/Menu/stars_0.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)
            elif type == 1:
                image = pygame.image.load("Slike/Menu/stars_1.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)
            elif type == 2:
                image = pygame.image.load("Slike/Menu/stars_2.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)
            elif type == 3:
                image = pygame.image.load("Slike/Menu/stars_3.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)

            for gumb in [IGRAJ, NATRAG]:
                gumb.changeColor(MENU_MOUSE_POS)
                gumb.update(scrn)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if IGRAJ.checkForInput(MENU_MOUSE_POS):
                        level(brojLevela)
                    if NATRAG.checkForInput(MENU_MOUSE_POS):
                        natrag = True
                        
            pygame.display.update()
            
            if natrag:
                break
        scrn.blit(oldScreen)


def level_end(scrn, brojLevela, type):
    test_font = pygame.font.Font(None, 50)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(128)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))
        
    while True:
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        intro_tekst = test_font.render("LEVEL ZAVRŠEN",True, "Black")
        intro_rect = intro_tekst.get_rect(center = (300, 100))
            
        PONOVO = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,450),"PONOVO", test_font, "Black", "White")
        NATRAG = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 550), "NATRAG", test_font, "Black", "White")

        scrn.blit(intro_tekst,intro_rect)
        
        if type < 50:
            image = pygame.image.load("Slike/Menu/stars_0.png")
            scrn.blit(image.get_rect(center = (300, 200)))
        elif type >= 50 and type < 70:
            image = pygame.image.load("Slike/Menu/stars_1.png")
            scrn.blit(image.get_rect(center = (300, 200)))
        elif type >= 70 and type < 90:
            image = pygame.image.load("Slike/Menu/stars_2.png")
            scrn.blit(image.get_rect(center = (300, 200)))
        elif type >= 90:
            image = pygame.image.load("Slike/Menu/stars_3.png")
            scrn.blit(image.get_rect(center = (300, 200)))

        for gumb in [PONOVO, NATRAG]:
            gumb.changeColor(MENU_MOUSE_POS)
            gumb.update(scrn)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PONOVO.checkForInput(MENU_MOUSE_POS):
                    level(brojLevela)
                if NATRAG.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                        
            pygame.display.update()


def level(brojLevela):
    pygame.init()
    pygame.display.set_caption("TheCatcher: Worldwide Thievery Thrust")

    if brojLevela == 1:
        background = pygame.image.load("Slike/Levels/Level 1/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 1/novcic.png").convert_alpha()
    elif brojLevela == 2:
        background = pygame.image.load("Slike/Levels/Level 2/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 2/novcic.png").convert_alpha()
    elif brojLevela == 3:
        background = pygame.image.load("Slike/Levels/Level 3/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 3/novcic.png").convert_alpha()
    elif brojLevela == 4:
        background = pygame.image.load("Slike/Levels/Level 4/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 4/novcic.png").convert_alpha()
    elif brojLevela == 5:
        background = pygame.image.load("Slike/Levels/Level 5/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 5/novcic.png").convert_alpha()
    elif brojLevela == 6:
        background = pygame.image.load("Slike/Levels/Level 6/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 6/novcic.png").convert_alpha()
    elif brojLevela == 7:
        background = pygame.image.load("Slike/Levels/Level 7/background.png").convert()
        slika_novcic = pygame.image.load("Slike/Levels/Level 7/novcic.png").convert_alpha()
        
    
    screen=pygame.display.set_mode((600,750))
    test_font = pygame.font.Font(None, 50)


    aktivnost_igrice=True
    score=0
            

    class Pirat():
        def __init__(self):
            self.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (120, 120)).convert_alpha()
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
            self.novcic_slika = slika_novcic
            self.novcic_rect=self.novcic_slika.get_rect(midtop= (randint(150, 450), -50))

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
        if len(objekti) == 0:
            novi_novcic = Novcic()
            objekti.add(novi_novcic)

        if score>=10:
            if len(objekti) == 1:
                for objekt in objekti.sprites():
                    if objekt.novcic_rect.bottom > 300:
                        novi_novcic = Novcic()
                        objekti.add(novi_novcic)

    def specials_drop():
        if len(specials) == 0:
            rendom=randint(1,5)
            
            if rendom == 1:
                special=Novcic()
                specials.add(special)
                special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/doublespecial.png"), (30,30)).convert_alpha()
                special.specialbroj=1


            elif rendom == 2:
                special=Novcic()
                specials.add(special)
                special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/freezespecial.png"), (30,30)).convert_alpha()
                special.specialbroj=2


            elif rendom == 3:
                special=Novcic()
                specials.add(special)
                special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/povecanjespecial.png"), (30,30)).convert_alpha()
                special.specialbroj=3


            elif rendom == 4:
                special=Novcic()
                specials.add(special)
                special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/smanjenjespecial.png"), (30, 30)).convert_alpha()
                special.specialbroj=4


            elif rendom == 5:
                special=Novcic()
                specials.add(special)
                special.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/speedspecial.png"), (30, 30)).convert_alpha()
                special.specialbroj=5

            


    def postotak():
        return ((score/ukupno)*100)

    while True:
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Levels/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    level_pause(screen, score)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            level_pause(screen, score)

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

            for objekt in objekti.sprites():
                if objekt.novcic_rect.bottom > 660:
                    objekti.remove(objekt)
                    ukupno+=1
            
            zavrsno_vrijeme=time.time()

            if zavrsno_vrijeme-pocetno_vrijeme>20:
                specials_drop()
                
            if len(specials)>0:
                for special in specials.sprites():
                    special.draw()
                    special.update()
                
                if sudar_sprite(special.novcic_rect)==True:
                    if special.specialbroj== 1:
                        vrijednost_novcica=2
                    elif special.specialbroj == 2:
                        player.brzina=0
                        player.jump_height=0
                        player.gravity=0
                    elif special.specialbroj == 3:
                        player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (240, 240)).convert_alpha()
                    elif special.specialbroj == 4:
                        player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (90, 90)).convert_alpha()
                    elif special.specialbroj == 5:
                        player.brzina=3

                    pocetak=time.time()
                    pocetno_vrijeme=zavrsno_vrijeme
                    zavrsno_vrijeme=0
                    for special in specials.sprites():
                        specials.remove(special)



                                        
            for special in specials.sprites():
                if special.novcic_rect.bottom > 660:
                    specials.remove(special)


            if time.time()-pocetak>=6:
                vrijednost_novcica=1
                player.brzina=1
                player.jump_height=15
                player.gravity=5
                player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (120, 120)).convert_alpha()
                pocetak=time.time()
            
            if ukupno>=50:
                aktivnost_igrice=False
                level_end(screen, brojLevela, postotak())

        pygame.display.update()


def endless():
    pygame.init()
    pygame.display.set_caption("TheCatcher: Worldwide Thievery Thrust")

    screen=pygame.display.set_mode((600,750))
    background= pygame.image.load("Slike/Endless/pozadina_igrica.jpg").convert()
    test_font = pygame.font.Font(None, 50)

    aktivnost_igrice=True
    score=0
    lives=3
    high_score = 0
            

    class Pirat():
        def __init__(self):
            self.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Endless/likpirata.png"), (120, 120)).convert_alpha()
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
            self.novcic_slika=pygame.image.load("Slike/Endless/slikacoin.png").convert_alpha()
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


       
    class Srce(pygame.sprite.Sprite):
        def __init__(self, x):
            super().__init__()
            self.srce_slika = pygame.transform.scale(pygame.image.load("Slike/Endless/srce.png").convert(), (40, 40))
            self.novcic_rect = self.srce_slika.get_rect(center=(10+(x*50),40))

        def draw(self):
            screen.blit(self.srce_slika, self.novcic_rect)
            
        
    srca = pygame.sprite.Group()
    srce1 = Srce(1)
    srce2 = Srce(2)
    srce3 = Srce(3)
    srca.add(srce1, srce2, srce3)

    while True:
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Endless/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    pause_menu(screen, score)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pause_menu(screen, score)

        
        if aktivnost_igrice:
            screen.blit(background, (0,0))

            player.draw()
            player.update()

            PAUSE_BACK.changeColor(PAUSE_MOUSE_POS)
            PAUSE_BACK.update(screen)
            
            for srce in srca.sprites():
                srce.draw()
            
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
                        if lives == 2:
                            srca.remove(srce3)
                        elif lives == 1:
                            srca.remove(srce2)
                        if lives==0:
                            srca.remove(srce1)
                            aktivnost_igrice=False
                            if score > high_score:
                                high_score = score
                            game_over(screen, score, high_score)
                        else:
                            aktivnost_igrice=True
        
        pygame.display.update()




        


    def update(self,screen):
        #self.image_line = pygame.transform.rotozoom(self.image_line,0,2)
        screen.blit(self.image_line, self.rect_line)
        #screen.blit(self.image_button, self.rect_button)

    def checkForInput1(self,position):
        if position[0] in range(self.rect_line.left +10, self.rect_line.right-9) and position[1] in range(self.rect_line.top, self.rect_line.bottom):
            return True
        return False


    def changeButtonPosition(self,position, screen, zvuk):
        self.jump_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
        self.jump_sound.set_volume(0.5)
        self.x_pos_button = int(position[0])
        self.rect_button = self.image_button.get_rect(center = (self.x_pos_button, self.y_pos_button))
        screen.blit(self.image_button, self.rect_button)
        if pygame.mouse.get_pressed()[0]:
            print(position)
            #self.jump_sound.play()
            return True


def main_menu(): #Iz ovoga dalje biramo druge "prozore". Moram napraviti animaciju i uskladiti dizajn s njom.
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(menu_surface, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_tekst = test_font.render("MAIN MENU",True, "Black")
        menu_rect = menu_tekst.get_rect(center = (300, 100))

        #Gumb(image, pos, text_input, font, base_color, hovering_color)
        PLAY_BUTTON =  Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb.png").convert(), (300, 300), "PLAY", test_font,"Black", "White")
        OPTIONS_BUTTON = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,400),"OPTIONS", test_font, "Black", "White")
        ACHIVMENT_BUTTON = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb3.png").convert(), (300,500),"ACHIVMENT", test_font, "Black", "White")
        QUIT_BUTTON = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 600), "QUIT", test_font, "Black", "White")

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
                    click_sound.play()
                    achivment()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play(): #Ovdje vi nadodajete svoj dio za sami aspekt igrice. Tu se odvija radnja
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("White") #Najvjerojatnije ću kasnije probati sa clear
        map_surf = pygame.image.load("Slike/Menu/Mapa2.png").convert()
        map_rect = map_surf.get_rect(topleft = (0, 70))
        screen.blit(map_surf, map_rect)

        play_tekst = test_font.render("MAPA SVIJETA", False, "Black")
        play_rect = play_tekst.get_rect(center = (300,50))
        screen.blit(play_tekst, play_rect)


        LEVEL_1 = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb3.png").convert(),(100, 200), "1.Level", test_font, "White", "Green")
        LEVEL_1.update(screen)
        LEVEL_2 = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb3.png").convert(),(400, 200), "2.Level", test_font, "White", "Green")
        LEVEL_2.update(screen)

        PLAY_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb4.png").convert(),(300, 700), "Vrati se", test_font, "White", "Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if LEVEL_1.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 1, 1)
                if LEVEL_2.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 2, 2)
        pygame.display.update()


def options(): #Moram nadodati za smanjivanje muzike i zvukova + možda i objašnjenje za kontrole/radnju
    while True:
        global zvuk
        global stisnut
        global zvuk2
        global stisnut2

        options_surface = pygame.image.load("Slike/Menu/Background_options.png").convert()
        screen.blit(options_surface, (0,0))
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        
        

        opcije_tekst = naslov_font.render("Opcije" ,False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 60))
        screen.blit(opcije_tekst, opcije_rect)


        muzika_tekst = podnaslov_font.render("Muzika" ,False, "Gray")
        muzika_rect = muzika_tekst.get_rect(center = (200, 230))
        screen.blit(muzika_tekst, muzika_rect)

        racun = round(zvuk,2)*100
        zvuk_tekst = test_font.render(f"{round(racun)}%",False, "Black")
        zvuk_rect = zvuk_tekst.get_rect(center = (500, 300))
        pygame.draw.rect(screen, "White", zvuk_rect)
        pygame.draw.rect(screen, "Brown", zvuk_rect,2)
        screen.blit(zvuk_tekst, zvuk_rect)


        efekt_tekst = podnaslov_font.render("Zvučni efekti" ,False, "Gray")
        efekt_rect = efekt_tekst.get_rect(center = (270, 430))
        screen.blit(efekt_tekst, efekt_rect)


        racun2 = round(zvuk2,2)*100
        zvuk2_tekst = test_font.render(f"{round(racun2)}%",False, "Black")
        zvuk2_rect = zvuk2_tekst.get_rect(center = (500, 500))
        pygame.draw.rect(screen, "White", zvuk2_rect)
        pygame.draw.rect(screen, "Brown", zvuk2_rect,2)
        screen.blit(zvuk2_tekst, zvuk2_rect)

        OPTIONS_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb5.png").convert(), (100, 700), "Vrati se", test_font, "White", "Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)


        #"(self, image_line, pos_line, image_button, pos_button)"
        OPTIONS_SOUND = Scroll(pygame.image.load("Slike/Menu/Scol_linija1.png").convert(), (100, 300), pygame.image.load("Slike/Menu/Scrol_gumb.png").convert())
        
        OPTIONS_SOUND.update(screen)

        OPTIONS_SOUND2 = Scroll(pygame.image.load("Slike/Menu/Scol_linija1.png").convert(), (100, 500), pygame.image.load("Slike/Menu/Scrol_gumb.png").convert())
        
        OPTIONS_SOUND2.update(screen)

        if stisnut == 0:
            OPTIONS_MUSIC = Gumb(pygame.image.load("Slike/Menu/Unmute.png").convert(), (50, 300), "", test_font, "White", "Green")
            OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC.update(screen)
        else:
            OPTIONS_MUSIC = Gumb(pygame.image.load("Slike/Menu/Mute.png").convert(), (50, 300), "", test_font, "White", "Green")
            OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC.update(screen)

        if stisnut2 == 0:
            OPTIONS_MUSIC2 = Gumb(pygame.image.load("Slike/Menu/Unmute.png").convert(), (50, 500), "", test_font, "White", "Green")
            OPTIONS_MUSIC2.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC2.update(screen)
        else:
            OPTIONS_MUSIC2 = Gumb(pygame.image.load("Slike/Menu/Mute.png").convert(), (50, 500), "", test_font, "White", "Green")
            OPTIONS_MUSIC2.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC2.update(screen)


        if OPTIONS_SOUND.checkForInput1(OPTIONS_MOUSE_POS):  
            if OPTIONS_SOUND.changeButtonPosition(OPTIONS_MOUSE_POS, screen, zvuk):
                zvuk = (OPTIONS_MOUSE_POS[0]- 110)/280 #Promijeni kad postaviš na drugo mjesto
                #print(zvuk)
                #print(racun)
                bg_music.set_volume(zvuk)
                pygame.mixer.unpause()
                stisnut = 0

        if OPTIONS_SOUND2.checkForInput1(OPTIONS_MOUSE_POS):  
            if OPTIONS_SOUND2.changeButtonPosition(OPTIONS_MOUSE_POS, screen, zvuk):
                zvuk2 = (OPTIONS_MOUSE_POS[0]- 110)/280 #Promijeni kad postaviš na drugo mjesto
                #print(zvuk)
                print(racun2)
                click_sound.set_volume(zvuk2)
                stisnut2 = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    main_menu()
                if OPTIONS_MUSIC.checkForInput(OPTIONS_MOUSE_POS):
                    if zvuk == 0:
                        zvuk = 0.5
                        pygame.mixer.unpause()
                        bg_music.set_volume(zvuk)
                        #print("1")
                        stisnut = 0
                    else:
                        zvuk = 0
                        pygame.mixer.pause()
                        #print("2")
                        stisnut = 1
                if OPTIONS_MUSIC2.checkForInput(OPTIONS_MOUSE_POS):
                    if zvuk2 == 0:
                        zvuk2 = 0.5
                        click_sound.set_volume(zvuk2)
                        print(zvuk2)
                        stisnut2 = 0
                    else:
                        zvuk2 = 0
                        click_sound.set_volume(zvuk2)
                        print(zvuk2)
                        stisnut2 = 1

        pygame.display.update()


def achivment(): 
    while True:
        ACHIVMENT_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("Black")

        achivment_tekst = test_font.render("Ovdje su achivmenti",False, "White")
        achivment_rect = achivment_tekst.get_rect(center = (300, 300))
        screen.blit(achivment_tekst, achivment_rect)

        ACHIVMENT_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300, 500),"Vrati se", test_font, "White", "Green")

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


login()
