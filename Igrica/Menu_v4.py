import pygame
import sys


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


            
            
            
        
  



#Još moram nadodati ulogiranje kao prvi pop up

pygame.init()
screen = pygame.display.set_mode((600, 750))

pygame.display.set_caption("Login")
menu_surface = pygame.image.load("Slike/Pozadina_menu.png").convert()
test_font = pygame.font.Font(None, 50) #Moram pronaći neki dobar Font/ napraviti
naslov_font = pygame.font.Font(None, 150)
podnaslov_font = pygame.font.Font(None, 100)



#S ostalima se dogovoriti za Logo
zvuk = 0.5
zvuk2 = 0.5
bg_music = pygame.mixer.Sound("Audio/He's a Pirate.mp3")
bg_music.set_volume(zvuk)
bg_music.play(loops= -1)
click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
click_sound.set_volume(zvuk2)
stisnut = 0
stisnut2 = 0

def login():
    user_text = ""

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
                        print(user_text)
                        with open("login_podaci.txt",encoding="utf-8") as datoteka:
                            podaci = datoteka.readlines()
                            if len(podaci) == 0:
                                podaci.append(f"{user_text}")
                            else:
                                podaci.append(f"\n{user_text}")
                            podaci_text = "".join(podaci)
                        print(podaci)
                        with open("login_podaci.txt","wt") as datoteka:
                            datoteka.write(podaci_text)
                        main_menu()
                        



        screen.fill("White")

        LOGIN_MOUSE_POS = pygame.mouse.get_pos()


        LOGIN_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb7.png").convert(), (300, 400),"Prijavi se", test_font, "Black", "Gray")

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
        map_surf = pygame.image.load("Slike/Mapa2.png").convert()
        map_rect = map_surf.get_rect(topleft = (0, 70))
        screen.blit(map_surf, map_rect)

        play_tekst = test_font.render("MAPA SVIJETA", False, "Black")
        play_rect = play_tekst.get_rect(center = (300,50))
        screen.blit(play_tekst, play_rect)


        LEVEL_1 = Gumb(pygame.image.load("Slike/Pozadina_gumb3.png").convert(),(100, 200), "1.Level", test_font, "White", "Green")
        LEVEL_1.update(screen)
        LEVEL_2 = Gumb(pygame.image.load("Slike/Pozadina_gumb3.png").convert(),(400, 200), "2.Level", test_font, "White", "Green")
        LEVEL_2.update(screen)

        PLAY_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb4.png").convert(),(300, 700), "Vrati se", test_font, "White", "Green")
        
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
                    print("1.level")
                if LEVEL_2.checkForInput(PLAY_MOUSE_POS):
                    print("2.level")
        pygame.display.update()



def options(): #Moram nadodati za smanjivanje muzike i zvukova + možda i objašnjenje za kontrole/radnju
    while True:
        global zvuk
        global stisnut
        global zvuk2
        global stisnut2

        options_surface = pygame.image.load("Slike/Background_options.png").convert()
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

        OPTIONS_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb5.png").convert(), (100, 700), "Vrati se", test_font, "White", "Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)


        #"(self, image_line, pos_line, image_button, pos_button)"
        OPTIONS_SOUND = Scroll(pygame.image.load("Slike/Scol_linija1.png").convert(), (100, 300), pygame.image.load("Slike/Scrol_gumb.png").convert())
        
        OPTIONS_SOUND.update(screen)

        OPTIONS_SOUND2 = Scroll(pygame.image.load("Slike/Scol_linija1.png").convert(), (100, 500), pygame.image.load("Slike/Scrol_gumb.png").convert())
        
        OPTIONS_SOUND2.update(screen)

        if stisnut == 0:
            OPTIONS_MUSIC = Gumb(pygame.image.load("Slike/Unmute.png").convert(), (50, 300), "", test_font, "White", "Green")
            OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC.update(screen)
        else:
            OPTIONS_MUSIC = Gumb(pygame.image.load("Slike/Mute.png").convert(), (50, 300), "", test_font, "White", "Green")
            OPTIONS_MUSIC.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC.update(screen)

        if stisnut2 == 0:
            OPTIONS_MUSIC2 = Gumb(pygame.image.load("Slike/Unmute.png").convert(), (50, 500), "", test_font, "White", "Green")
            OPTIONS_MUSIC2.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_MUSIC2.update(screen)
        else:
            OPTIONS_MUSIC2 = Gumb(pygame.image.load("Slike/Mute.png").convert(), (50, 500), "", test_font, "White", "Green")
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


login()
                


        
