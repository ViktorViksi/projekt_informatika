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
login_font = pygame.font.Font(None, 45)
achivment_font = pygame.font.Font(None, 40)

zvuk = 0.5
zvuk2 = 0.5
bg_music = pygame.mixer.Sound("Audio/He's a Pirate.mp3")
bg_music.set_volume(zvuk)
bg_music.play(loops= -1)
click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
click_sound.set_volume(zvuk2)
stisnut = 0
stisnut2 = 0
novo = 0
achivment_skok = 0
achivment_gubitak = 0
achivment_1pobjeda = 0
achivment_3zvez = 0
achivment_sve3zvez = 0
achivment_high_score = 0


with open("login_podaci.txt", encoding="utf-8") as datoteka:
    podaci = datoteka.readlines()
    for i in range(len(podaci)):
        podaci[i] = podaci[i].split(" ")
        podaci[i][2] = podaci[i][2].strip().split("_")
        podaci[i][3] = podaci[i][3].strip().split("_")


def login():
    user_text = ""
    
    global podaci
    global data
    global high_score
    
    input_rect = pygame.Rect(140,300,315,40)
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
                            if len(user_text) == 0:
                                user_text = "privremeno"
                            if user_text.upper() == podaci[i][0]:
                                data = i
                                high_score = int(podaci[data][1])
                                vrati_achivment(int(podaci[data][3][0]), int(podaci[data][3][1]), int(podaci[data][3][2]), int(podaci[data][3][3]), int(podaci[data][3][4]), int(podaci[data][3][5]),)

                                main_menu()
                            else:
                                podaci.append([user_text.upper(), "0", ["0", "0", "l", "l", "l", "l", "l", "l",], ["0", "0", "0", "0", "0", "0"], "\n"])
                                data = len(podaci)-1
                                high_score = int(podaci[data][1])
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

        text_srurface = login_font.render(user_text,True, "Green")
        
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


def pause_options(scrn, score):
    test_font = pygame.font.Font(None, 50)
    naslov_font = pygame.font.Font(None, 150)
    podnaslov_font = pygame.font.Font(None, 100)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(170)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))
    
    natrag = False
    
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
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    natrag = True
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
        
        if natrag:
            scrn.blit(oldScreen, (0,0))
            pygame.display.update()
            break


def level_options(scrn, score):
    test_font = pygame.font.Font(None, 50)
    naslov_font = pygame.font.Font(None, 150)
    podnaslov_font = pygame.font.Font(None, 100)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(170)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))
    
    natrag = False
    
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
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    click_sound.play()
                    natrag = True
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
        
        if natrag:
            scrn.blit(oldScreen, (0,0))
            pygame.display.update()
            break

    
def ispis(lista):
    if lista[data][0] != "PRIVREMENO":
        lista[data][1] = str(high_score)
        for i in range(len(lista)):
            string1 = "_".join(lista[i][2])
            lista[i][2] = string1
            string2 = "_".join(lista[i][3])
            lista[i][3] = string2
            lista[i] = " ".join(lista[i])

        with open("login_podaci.txt", "wt" ,encoding="utf-8") as datoteka:
            datoteka.writelines(lista)


def pause_menu(scrn, score):
    test_font = pygame.font.Font(None, 50)
    oldScreen = pygame.Surface.copy(scrn)
    s = pygame.Surface((560, 710))
    s.set_alpha(170)
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
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NASTAVI.checkForInput(PAUSE_MOUSE_POS) or PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    nastavi = True
                if OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    pause_options(scrn, oldScreen)
                    scrn.blit(oldScreen, (0,0))
                    pause_menu(scrn, score)
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
    s.set_alpha(170)
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
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if NASTAVI.checkForInput(PAUSE_MOUSE_POS) or PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    nastavi = True
                if OPTIONS.checkForInput(PAUSE_MOUSE_POS):
                    level_options(scrn, score)
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
    s.set_alpha(170)
    s.fill((55, 71, 79))
    
    scrn.blit(s, (20,20))

    while True:
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        pause_tekst = test_font.render("GAME OVER",True, "Black")
        pause_rect = pause_tekst.get_rect(center = (300, 100))

        score_tekst = test_font.render(f"Current Score: {score}",True, "Black")
        score_rect = score_tekst.get_rect(center = (300, 200))
        
        hscore_tekst = test_font.render(f"High Score: {hscore}",True, "Black")
        hscore_rect = hscore_tekst.get_rect(center = (300, 300))
        
        PONOVO = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,500),"PONOVO", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Menu/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

        scrn.blit(pause_tekst,pause_rect)
        scrn.blit(score_tekst, score_rect)
        scrn.blit(hscore_tekst, hscore_rect)

        for gumb in [PONOVO, MENU, PAUSE_BACK]:
            gumb.changeColor(PAUSE_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ispis(podaci)
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
    s.set_alpha(170)
    s.fill((55, 71, 79))
    
    if type == "l":
        locked = True
    else:
        locked = False
    
    scrn.blit(s, (20,20))
    
    if brojLevela == 1:
        tekst = "LEVEL 1 - NEW YORK"
    elif brojLevela == 2:
        tekst = "LEVEL 2 - BRAZIL"
    elif brojLevela == 3:
        tekst = "LEVEL 3 - ANTARCTICA"
    elif brojLevela == 4:
        tekst = "LEVEL 4 - EGYPT"
    elif brojLevela == 5:
        tekst = "LEVEL 5 - PARIS"
    elif brojLevela == 6:
        tekst = "LEVEL 6 - CHINA"
    elif brojLevela == 7:
        tekst = "LEVEL 7 - AUSTRALIA"
    
    natrag = False
    
    if locked:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            intro_tekst = test_font.render(tekst,True, "Black")
            intro_rect = intro_tekst.get_rect(center = (300, 100))
            
            msg_tekst = test_font.render(f"Level je zaključan",True, "Black")
            msg_rect = msg_tekst.get_rect(center = (300, 200))
            
            NATRAG = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 550), "NATRAG", test_font, "Black", "White")

            scrn.blit(intro_tekst,intro_rect)
            scrn.blit(msg_tekst, msg_rect)

            for gumb in [NATRAG]:
                gumb.changeColor(MENU_MOUSE_POS)
                gumb.update(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ispis(podaci)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NATRAG.checkForInput(MENU_MOUSE_POS):
                        natrag = True
            
            pygame.display.update()
            
            if natrag:
                break
        scrn.blit(oldScreen, (0,0))
        
    else:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            intro_tekst = test_font.render(tekst,True, "Black")
            intro_rect = intro_tekst.get_rect(center = (300, 100))
            
            IGRAJ = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300,450),"IGRAJ", test_font, "Black", "White")
            NATRAG = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (300, 550), "NATRAG", test_font, "Black", "White")

            scrn.blit(intro_tekst,intro_rect)
            
            if type == "0":
                image = pygame.image.load("Slike/Menu/stars_0.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)
            elif type == "1":
                image = pygame.image.load("Slike/Menu/stars_1.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)
            elif type == "2":
                image = pygame.image.load("Slike/Menu/stars_2.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)
            elif type == "3":
                image = pygame.image.load("Slike/Menu/stars_3.png")
                image_rect = image.get_rect(center=(300,200))
                scrn.blit(image, image_rect)

            for gumb in [IGRAJ, NATRAG]:
                gumb.changeColor(MENU_MOUSE_POS)
                gumb.update(scrn)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    ispis(podaci)
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if IGRAJ.checkForInput(MENU_MOUSE_POS):
                        vrati_achivment(0,0,1,0,0,0)
                        level(brojLevela)
                    if NATRAG.checkForInput(MENU_MOUSE_POS):
                        natrag = True
                        
            pygame.display.update()
            
            if natrag:
                break
        scrn.blit(oldScreen, (0,0))


def level_end(scrn, brojLevela, type):
    global podaci
    test_font = pygame.font.Font(None, 50)
    s = pygame.Surface((560, 710))
    s.set_alpha(170)
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
            image_rect = image.get_rect(center=(300,200))
            scrn.blit(image, image_rect)
            vrati_achivment(0,1,0,0,0,0)
        elif type >= 50 and type < 70:
            image = pygame.image.load("Slike/Menu/stars_1.png")
            image_rect = image.get_rect(center=(300,200))
            scrn.blit(image, image_rect)
            if podaci[data][2][brojLevela] == "0":
                podaci[data][2][brojLevela] == "1"
                try:
                    if podaci[data][2][brojLevela+1] == "l":
                        podaci[data][2][brojLevela+1] = "0"
                except:
                    continue
                
        elif type >= 70 and type < 90:
            image = pygame.image.load("Slike/Menu/stars_2.png")
            image_rect = image.get_rect(center=(300,200))
            scrn.blit(image, image_rect)
            if podaci[data][2][brojLevela] == "0" or podaci[data][2][brojLevela] == "1":
                podaci[data][2][brojLevela] == "2"
                try:
                    if podaci[data][2][brojLevela+1] == "l":
                        podaci[data][2][brojLevela+1] = "0"
                except:
                    continue
                
        elif type >= 90:
            image = pygame.image.load("Slike/Menu/stars_3.png")
            image_rect = image.get_rect(center=(300,200))
            scrn.blit(image, image_rect)
            podaci[data][2][brojLevela] = "3"
            try:
                if podaci[data][2][brojLevela+1] == "l":
                    podaci[data][2][brojLevela+1] = "0"
            except:
                continue


        for gumb in [PONOVO, NATRAG]:
            gumb.changeColor(MENU_MOUSE_POS)
            gumb.update(scrn)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PONOVO.checkForInput(MENU_MOUSE_POS):
                    level(brojLevela)
                if NATRAG.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                        
            pygame.display.update()


def level(broj_levela):
    pygame.init()
    pygame.display.set_caption("TheCatcher: Worldwide Thievery Thrust")
    
    screen=pygame.display.set_mode((600,750))


    aktivnost_igrice=True
    score=0
            

    class Pirat():
        def __init__(self):
            self.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (120, 120)).convert_alpha()
            self.pirat_rect=self.pirat_image.get_rect(midbottom= (300, 700))
            

            self.kretanje_desno=False
            self.kretanje_lijevo=False
            self.jump=False

            self.brzina= 30
            self.gravity= 5
            self.jump_height= 15
            self.skok = 0


        def kretanje_komande(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.kretanje_desno = True
            if keys[pygame.K_LEFT]:
                self.kretanje_lijevo = True
            if keys[pygame.K_SPACE]:
                self.jump = True
                self.skok += 1
                if self.skok >= 10:
                    vrati_achivment(1,0,0,0,0,0)
        
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
            if broj_levela==1:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 1/novcic.png"), (30,30)).convert_alpha()
            elif broj_levela==2:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 2/novcic.png"), (30,30)).convert_alpha()
            elif broj_levela==3:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 3/novcic.png"), (30,30)).convert_alpha()
            elif broj_levela==4:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 4/novcic.png"), (30,30)).convert_alpha()
            elif broj_levela==5:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 5/novcic.png"), (30,30)).convert_alpha()
            elif broj_levela==6:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 6/novcic.png"), (30,30)).convert_alpha()
            elif broj_levela==7:
                self.novcic_slika=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 7/novcic.png"), (30,30)).convert_alpha()
            
            self.novcic_rect=self.novcic_slika.get_rect(midtop= (randint(150, 450), -50))

            self.brzina_dropa=30

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

    def drop_novcici(broj_levela):
        global background
        if broj_levela>=1:
            background= pygame.image.load("Slike/Levels/Level 1/background.png").convert()
            if len(objekti) == 0:
                novi_novcic = Novcic()
                objekti.add(novi_novcic)

        if broj_levela>=2:
            background= pygame.image.load("Slike/Levels/Level 2/background.png").convert()
            if score>=5:
                if len(objekti) == 1:
                    for objekt in objekti.sprites():
                        if objekt.novcic_rect.bottom > 300:
                            novi_novcic = Novcic()
                            objekti.add(novi_novcic)

        if broj_levela>=3:
            background= pygame.image.load("Slike/Levels/Level 3/background.png").convert()
            if score>=10:
                for objekt in objekti.sprites():
                    objekt.brzina_dropa=1.2

        if broj_levela>=4:
            background= pygame.image.load("Slike/Levels/Level 4/background.png").convert()
            if score>=15:
                if len(objekti) == 2:
                    for objekt in objekti.sprites():
                        if objekt.novcic_rect.bottom > 550:
                            novi_novcic = Novcic()
                            objekti.add(novi_novcic)
        
        if broj_levela>=5:
            background= pygame.image.load("Slike/Levels/Level 5/background.png").convert()
            if score>=20:
                for objekt in objekti.sprites():
                    objekt.brzina_dropa=1.4

        if broj_levela>=6:
            background= pygame.image.load("Slike/Levels/Level 6/background.png").convert()
            if score>=25:
                if len(objekti) == 3:
                    for objekt in objekti.sprites():
                        if objekt.novcic_rect.bottom > 450:
                            novi_novcic = Novcic()
                            objekti.add(novi_novcic)

        if broj_levela>=7:
            background= pygame.image.load("Slike/Levels/Level 7/background.png").convert()
            if score>=30:
                for objekt in objekti.sprites():
                    objekt.brzina_dropa=1.8



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
        return((score/ukupno)*100)

    while True:
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Levels/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")
        PAUSE_MOUSE_POS = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PAUSE_BACK.checkForInput(PAUSE_MOUSE_POS):
                    level_pause(screen, score)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            level_pause(screen, score)

        if aktivnost_igrice:
            if broj_levela == 1:
                background = pygame.image.load("Slike/Levels/Level 1/background.png").convert()
                player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/Level 1/pirateskrilima.png"), (120,120)).convert_alpha()
            elif broj_levela == 2:
                background = pygame.image.load("Slike/Levels/Level 2/background.png").convert()
            elif broj_levela == 3:
                background = pygame.image.load("Slike/Levels/Level 3/background.png").convert()
            elif broj_levela == 4:
                background = pygame.image.load("Slike/Levels/Level 4/background.png").convert()
            elif broj_levela == 5:
                background = pygame.image.load("Slike/Levels/Level 5/background.png").convert()
            elif broj_levela == 6:
                background = pygame.image.load("Slike/Levels/Level 6/background.png").convert()
            elif broj_levela == 7:
                background = pygame.image.load("Slike/Levels/Level 7/background.png").convert()
            
            screen.blit(background, (0,0))

            player.draw()
            player.update()
            
            drop_novcici(broj_levela)
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
                if objekt.novcic_rect.bottom > 700:
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
                        player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/freezelikpirata.png"), (120, 120)).convert_alpha()
                    elif special.specialbroj == 3:
                        player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (240, 240)).convert_alpha()
                    elif special.specialbroj == 4:
                        player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/likpirata.png"), (90, 90)).convert_alpha()
                    elif special.specialbroj == 5:
                        player.brzina=3
                        player.pirat_image=pygame.transform.scale(pygame.image.load("Slike/Levels/speedlikpirata.png"), (120, 120)).convert_alpha()

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
                level_end(screen, broj_levela, postotak())

        pygame.display.update()
    

def endless():
    pygame.init()
    pygame.display.set_caption("TheCatcher: Worldwide Thievery Thrust")

    screen=pygame.display.set_mode((600,750))
    background= pygame.image.load("Slike/Endless/background.png").convert()
    test_font = pygame.font.Font(None, 50)

    aktivnost_igrice=True
    score=0
    lives=3
    global high_score
            

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
            self.srce_slika = pygame.transform.scale(pygame.image.load("Slike/Endless/srce.png").convert_alpha(), (40, 40))
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
                ispis(podaci)
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
                            if high_score >= 100:
                                vrati_achivment(0,0,0,0,0,1)
                            game_over(screen, score, high_score)
                        else:
                            aktivnost_igrice=True
        
        pygame.display.update()


def main_menu(): #Iz ovoga dalje biramo druge "prozore". Moram napraviti animaciju i uskladiti dizajn s njom.
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(menu_surface, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_tekst = test_font.render("THE CATCHER",True, "Black")
        menu_rect = menu_tekst.get_rect(center = (300, 100))

        #Gumb(image, pos, text_input, font, base_color, hovering_color)
        PLAY_BUTTON =  Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb.png").convert(), (450, 300), "PLAY", test_font,"Black", "White")
        OPTIONS_BUTTON = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (450,400),"OPTIONS", test_font, "Black", "White")
        ACHIVMENT_BUTTON = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb3.png").convert(), (450,500),"ACHIVMENT", test_font, "Black", "White")
        QUIT_BUTTON = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb6.png").convert(), (450, 600), "QUIT", test_font, "Black", "White")

        screen.blit(menu_tekst,menu_rect)

        for gumb in [PLAY_BUTTON, OPTIONS_BUTTON, ACHIVMENT_BUTTON, QUIT_BUTTON]:
            gumb.changeColor(MENU_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ispis(podaci)
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
                    ispis(podaci)
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play():
    biranje()

def biranje():
    while True:
        BIRANJE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((196, 179, 179)) #Najvjerojatnije ću kasnije probati sa clear



        CAMPAIGN = Gumb(pygame.image.load("Slike/Menu/Campaign_slika.png").convert(),(300, 180), "", test_font, "White", "Green")
        CAMPAIGN.update(screen)
        ENDLESS= Gumb(pygame.image.load("Slike/Menu/Endless_slika.png").convert(),(300, 500), "", test_font, "White", "Green")
        ENDLESS.update(screen)

        BIRANJE_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb4.png").convert(),(300, 700), "Vrati se", test_font, "White", "Green")
        
        BIRANJE_BACK.changeColor(BIRANJE_MOUSE_POS)
        BIRANJE_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BIRANJE_BACK.checkForInput(BIRANJE_MOUSE_POS):
                    main_menu()
                if CAMPAIGN.checkForInput(BIRANJE_MOUSE_POS):
                    map()
                if ENDLESS.checkForInput(BIRANJE_MOUSE_POS):
                    endless()
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
                ispis(podaci)
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
        #global novo
        #print(novo)

        achivment_surface = pygame.image.load("Slike/Menu/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))
        ACHIVMENT_MOUSE_POS = pygame.mouse.get_pos()

        achivment_tekst = achivment_font.render( "Skoči izrazito puno puta" ,False, "White")
        achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 510 ))

        achivment_tekst3 = achivment_font.render( "Skoči izrazito puno puta" ,False, "White")
        achivment_tekst_rect3 = achivment_tekst3.get_rect(center = (350, 510 ))
        

        achivment_surface = pygame.image.load("Slike/Menu/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))

        achivment_table = pygame.image.load("Slike/Menu/Table_achivment.jpg").convert()
        achivment_table_locked = pygame.image.load("Slike/Menu/Table_achivment_locked.jpg").convert()
        achivment_table_rect_locked = achivment_table_locked.get_rect(midleft = (10, 520))
        screen.blit(achivment_table_locked, achivment_table_rect_locked)
        achivment_table_rect_locked = achivment_table_locked.get_rect(midleft = (10, 370))
        screen.blit(achivment_table_locked, achivment_table_rect_locked)
        achivment_table_rect_locked = achivment_table_locked.get_rect(midleft = (10, 220))
        screen.blit(achivment_table_locked, achivment_table_rect_locked)



        if achivment_1pobjeda == 1:
            achivment_table_rect = achivment_table.get_rect(midleft = (10, 220))
            screen.blit(achivment_table, achivment_table_rect) 
            achivment_tekst =achivment_font.render( "Odigraj prvu igru" ,False, "Black")
            achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 210 ))
            screen.blit(achivment_tekst, achivment_tekst_rect)
        if achivment_gubitak == 1:
            achivment_table_rect = achivment_table.get_rect(midleft = (10, 370))
            screen.blit(achivment_table, achivment_table_rect)
            achivment_tekst =achivment_font.render( "Prvi puta izgubi" ,False, "Black")
            achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 360 ))
            screen.blit(achivment_tekst, achivment_tekst_rect)
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y))
        if achivment_skok == 1:
            achivment_table_rect = achivment_table.get_rect(midleft = (10, 520))
            screen.blit(achivment_table, achivment_table_rect)
            achivment_tekst =achivment_font.render( "Skoči jako puno puta" ,False, "Black")
            achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 510 ))
            screen.blit(achivment_tekst, achivment_tekst_rect)
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y))
        

        
        opcije_tekst = naslov_font.render("Postignuća" ,False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 60 ))
        screen.blit(opcije_tekst, opcije_rect)
        
        ACHIVMENT_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300, 700),"Vrati se", test_font, "White", "Green")

        ACHIVMENT_BACK.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_BACK.update(screen)


        #ACHIVMENT_MOVE = Scroll(pygame.image.load("Slike/Scol_linija2.png").convert(), (300, 400), pygame.image.load("Slike/Scrol_gumb.png").convert())
        
        #ACHIVMENT_MOVE.update(screen)

        #if ACHIVMENT_MOVE.checkForInput2(ACHIVMENT_MOUSE_POS):  
        #    if ACHIVMENT_MOVE.changeSurfacePosition(ACHIVMENT_MOUSE_POS, screen):
        #        novo = ACHIVMENT_MOUSE_POS[1]


        ACHIVMENT_RIGHT = Gumb(pygame.image.load("Slike/Menu/Strelica.png"), (500, 690),"", test_font, "White", "Green")

        ACHIVMENT_RIGHT.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_RIGHT.update(screen)




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACHIVMENT_BACK.checkForInput(ACHIVMENT_MOUSE_POS):
                    main_menu()
                if ACHIVMENT_RIGHT.checkForInput(ACHIVMENT_MOUSE_POS):
                    achivment2()
        pygame.display.update()


def achivment2(): 
    while True:
        #global novo
        #novo = 0
        global podaci
        brojac = 0

        for i in range(1,len(podaci[data][2])):
            if podaci[data][2][i] == "3":
                vrati_achivment(0,0,0,1,0,0)
                brojac +=1
        
        if brojac == 7:
            vrati_achivment(0,0,0,0,1,0)

        achivment_surface = pygame.image.load("Slike/Menu/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))
        ACHIVMENT_MOUSE_POS = pygame.mouse.get_pos()

        
        achivment_tekst = achivment_font.render( "Skoči izrazito puno puta" ,False, "White")
        achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 510 ))

        achivment_tekst3 = achivment_font.render( "Skoči izrazito puno puta" ,False, "White")
        achivment_tekst_rect3 = achivment_tekst3.get_rect(center = (350, 510 ))
        

        achivment_surface = pygame.image.load("Slike/Menu/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))

        achivment_table = pygame.image.load("Slike/Menu/Table_achivment.jpg").convert()
        achivment_table_locked = pygame.image.load("Slike/Menu/Table_achivment_locked.jpg").convert()
        achivment_table_rect_locked = achivment_table_locked.get_rect(midleft = (10, 520))
        screen.blit(achivment_table_locked, achivment_table_rect_locked)
        achivment_table_rect_locked = achivment_table_locked.get_rect(midleft = (10, 370))
        screen.blit(achivment_table_locked, achivment_table_rect_locked)
        achivment_table_rect_locked = achivment_table_locked.get_rect(midleft = (10, 220))
        screen.blit(achivment_table_locked, achivment_table_rect_locked)



        if achivment_3zvez == 1:
            achivment_table_rect = achivment_table.get_rect(midleft = (10, 220))
            screen.blit(achivment_table, achivment_table_rect) 
            achivment_tekst =achivment_font.render( "Pobijedi s 3 zvijezde" ,False, "Black")
            achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 210 ))
            screen.blit(achivment_tekst, achivment_tekst_rect)
        if achivment_sve3zvez == 1:
            achivment_table_rect = achivment_table.get_rect(midleft = (10, 370))
            screen.blit(achivment_table, achivment_table_rect)
            achivment_tekst =achivment_font.render( "Sve pobijedi s 3 zvijezde" ,False, "Black")
            achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 360 ))
            screen.blit(achivment_tekst, achivment_tekst_rect)
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y))
        if achivment_high_score == 1:
            achivment_table_rect = achivment_table.get_rect(midleft = (10, 520))
            screen.blit(achivment_table, achivment_table_rect)
            achivment_tekst =achivment_font.render( "Postigni novi high score" ,False, "Black")
            achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 510 ))
            screen.blit(achivment_tekst, achivment_tekst_rect)
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y))

        

        
        opcije_tekst = naslov_font.render("Postignuća" ,False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 60 ))
        screen.blit(opcije_tekst, opcije_rect)
        
        ACHIVMENT_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb2.png").convert(), (300, 700),"Vrati se", test_font, "White", "Green")

        ACHIVMENT_BACK.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_BACK.update(screen)


        #ACHIVMENT_MOVE = Scroll(pygame.image.load("Slike/Scol_linija2.png").convert(), (300, 400), pygame.image.load("Slike/Scrol_gumb.png").convert())
        
        #ACHIVMENT_MOVE.update(screen)

        #if ACHIVMENT_MOVE.checkForInput2(ACHIVMENT_MOUSE_POS):  
        #    if ACHIVMENT_MOVE.changeSurfacePosition(ACHIVMENT_MOUSE_POS, screen):
        #        novo = ACHIVMENT_MOUSE_POS[1]


        ACHIVMENT_RIGHT = Gumb(pygame.image.load("Slike/Menu/Strelica2.png"), (100, 690),"", test_font, "White", "Green")

        ACHIVMENT_RIGHT.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_RIGHT.update(screen)

        


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACHIVMENT_BACK.checkForInput(ACHIVMENT_MOUSE_POS):
                    main_menu()
                if ACHIVMENT_RIGHT.checkForInput(ACHIVMENT_MOUSE_POS):
                    achivment()
        pygame.display.update()


def vrati_achivment(skok, gubitak, Pigra, Tzvez, SveTzvez, high): #omogućuje da se postigne achivment. Radi tako da se na stavi potrebna mjesta (npr. funkicju za skokove) i onda ona to ovdje vraća i mijenja achivmente u točne
    global achivment_skok
    global achivment_gubitak
    global achivment_1pobjeda
    global achivment_3zvez
    global achivment_sve3zvez
    global achivment_high_score
    global high_score
    global podaci
    if skok == 1:
        achivment_skok = 1
        podaci[data][3][0] = "1"
    if gubitak == 1:
        achivment_gubitak = 1
        podaci[data][3][1] = "1"
    if Pigra == 1:
        achivment_1pobjeda = 1
        podaci[data][3][2] = "1"
    if Tzvez == 1:
        achivment_3zvez = 1
        podaci[data][3][3] = "1"
    if SveTzvez == 1:
        achivment_sve3zvez = 1
        podaci[data][3][4] = "1"
    if high == 1:
        achivment_high_score = 1
        podaci[data][3][5] = "1"


def map():
    while True:
        PLAY_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill("White")
        map_surf = pygame.transform.scale(pygame.image.load("Slike/Menu/map 3.jpg").convert(), (600, 750))
        map_rect = map_surf.get_rect(topleft = (0,0))
        screen.blit(map_surf, map_rect)

        LEVEL_1 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(),(148, 297), "", test_font, "White", "Green")
        LEVEL_2 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(), (199, 430), "", test_font, "White", "Green")
        LEVEL_3 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(), (273, 592), "", test_font, "White", "Green")
        LEVEL_4 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(), (318, 311), "", test_font, "White", "Green")
        LEVEL_5 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(), (279, 273), "", test_font, "White", "Green")
        LEVEL_6 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(), (431, 289), "", test_font, "White", "Green")
        LEVEL_7 = Gumb(pygame.image.load("Slike/Menu/x.png").convert_alpha(), (508, 448), "", test_font, "White", "Green")

        PLAY_BACK = Gumb(pygame.image.load("Slike/Menu/Pozadina_gumb4.png").convert(),(300, 700), "Vrati se", test_font, "White", "Green")
        
        for gumb in [LEVEL_1, LEVEL_2, LEVEL_3, LEVEL_4, LEVEL_5, LEVEL_6, LEVEL_7, PLAY_BACK]:
            gumb.changeColor(PLAY_MOUSE_POS)
            gumb.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ispis(podaci)
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
                if LEVEL_1.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 1, podaci[data][2][1])
                if LEVEL_2.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 2, podaci[data][2][2])
                if LEVEL_3.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 3, podaci[data][2][3])
                if LEVEL_4.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 4, podaci[data][2][4])
                if LEVEL_5.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 5, podaci[data][2][5])
                if LEVEL_6.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 6, podaci[data][2][6])
                if LEVEL_7.checkForInput(PLAY_MOUSE_POS):
                    level_start(screen, 7, podaci[data][2][7])
        pygame.display.update()
    

login()


