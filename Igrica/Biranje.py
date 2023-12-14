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
        screen.blit(self.image_line, self.rect_line)

    def checkForInput1(self,position):
        if position[0] in range(self.rect_line.left +10, self.rect_line.right-9) and position[1] in range(self.rect_line.top, self.rect_line.bottom):
            return True
        return False


    def changeButtonPosition(self,position, screen):
        self.x_pos_button = int(position[0])
        self.rect_button = self.image_button.get_rect(center = (self.x_pos_button, self.y_pos_button))
        screen.blit(self.image_button, self.rect_button)
        if pygame.mouse.get_pressed()[0]:
            print(position)
            return True



pygame.init()
screen = pygame.display.set_mode((600, 750))

pygame.display.set_caption("Login")
menu_surface = pygame.image.load("Slike/Pozadina_menu.png").convert()
test_font = pygame.font.Font(None, 50) #Moram pronaći neki dobar Font/ napraviti
naslov_font = pygame.font.Font(None, 150)
podnaslov_font = pygame.font.Font(None, 100)
login_font =  pygame.font.Font(None, 45)
achivment_font = pygame.font.Font(None, 55)

#S ostalima se dogovoriti za Logo
zvuk = 0
zvuk2 = 0.5
bg_music = pygame.mixer.Sound("Audio/He's a Pirate.mp3")
bg_music.set_volume(zvuk)
bg_music.play(loops= -1)
click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
click_sound.set_volume(zvuk2)
stisnut = 0
stisnut2 = 0
novo = 0 #Gdjegod da raste tamo treba stajati global novo (no bit će za svaki achivment zasebno)



def main_menu(): #Iz ovoga dalje biramo druge "prozore". Moram napraviti animaciju i uskladiti dizajn s njom.
    pygame.display.set_caption("Menu")

    while True:
        screen.blit(menu_surface, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_tekst = test_font.render("MAIN MENU",True, "Black")
        menu_rect = menu_tekst.get_rect(center = (300, 100))

        #Gumb(image, pos, text_input, font, base_color, hovering_color)
        PLAY_BUTTON =  Gumb(pygame.image.load("Slike/Pozadina_gumb.png").convert(), (300, 300), "PLAY", test_font,"Black", "White")

        screen.blit(menu_tekst,menu_rect)

        for gumb in [PLAY_BUTTON]:
            gumb.changeColor(MENU_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    biranje()

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

def biranje():
    while True:
        BIRANJE_MOUSE_POS = pygame.mouse.get_pos()

        screen.fill((196, 179, 179)) #Najvjerojatnije ću kasnije probati sa clear



        CAMPAIGN = Gumb(pygame.image.load("Slike/Campaign_slika.png").convert(),(300, 180), "", test_font, "White", "Green")
        CAMPAIGN.update(screen)
        ENDLESS= Gumb(pygame.image.load("Slike/Endless_slika.png").convert(),(300, 500), "", test_font, "White", "Green")
        ENDLESS.update(screen)

        BIRANJE_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb4.png").convert(),(300, 700), "Vrati se", test_font, "White", "Green")
        
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
                    play()
                if ENDLESS.checkForInput(BIRANJE_MOUSE_POS):
                    print("Endless")
        pygame.display.update()







main_menu()