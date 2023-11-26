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

        screen.fill("Black") #Najvjerojatnije ću kasnije probati sa clear

        play_tekst = test_font.render("Ovdje je igrica", False, "White")
        play_rect = play_tekst.get_rect(center = (300, 300))
        screen.blit(play_tekst, play_rect)

        PLAY_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb4.png").convert(),(300, 500), "Vrati se", test_font, "White", "Green")
        
        PLAY_BACK.changeColor(PLAY_MOUSE_POS)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    main_menu()
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



main_menu()
                


        
