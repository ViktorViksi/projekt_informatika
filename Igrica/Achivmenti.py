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
    
    #def checkForInput2(self,position):
    #    if position[0] in range(self.rect_line.left, self.rect_line.right) and position[1] in range(self.rect_line.top, self.rect_line.bottom):
    #        return True
    #    return False


    def changeButtonPosition(self,position, screen, zvuk):
        self.click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
        self.click_sound.set_volume(0.5)
        self.x_pos_button = int(position[0])
        self.rect_button = self.image_button.get_rect(center = (self.x_pos_button, self.y_pos_button))
        screen.blit(self.image_button, self.rect_button)
        if pygame.mouse.get_pressed()[0]:
            print(position)
            #self.click_sound.play()
            return True

    #def changeSurfacePosition(self,position, screen):
    #    self.y_pos_button = int(position[1])
    #    self.rect_button = self.image_button.get_rect(center = (self.x_pos_button+10, self.y_pos_button))
    #    screen.blit(self.image_button, self.rect_button)
    #    if pygame.mouse.get_pressed()[0]:
    #        print(position)
    #        #self.click_sound.play()
    #        return True

            
            
            
        
  



#Još moram nadodati ulogiranje kao prvi pop up

pygame.init()
screen = pygame.display.set_mode((600, 750))

pygame.display.set_caption("Login")
menu_surface = pygame.image.load("Slike/Pozadina_menu.png").convert()
test_font = pygame.font.Font(None, 50) #Moram pronaći neki dobar Font/ napraviti
naslov_font = pygame.font.Font(None, 150)
podnaslov_font = pygame.font.Font(None, 100)
login_font = pygame.font.Font(None, 45)
achivment_font = pygame.font.Font(None, 55)

#S ostalima se dogovoriti za Logo
zvuk = 0.5
zvuk2 = 0.5
bg_music = pygame.mixer.Sound("Audio/He's a Pirate.mp3")
#bg_music.set_volume(zvuk)
#bg_music.play(loops= -1)
click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
click_sound.set_volume(zvuk2)
stisnut = 0
stisnut2 = 0
novo = 0

def main_menu(): #Iz ovoga dalje biramo druge "prozore". Moram napraviti animaciju i uskladiti dizajn s njom.
    pygame.display.set_caption("Menu")
    global novo

    while True:
        screen.blit(menu_surface, (0,0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        menu_tekst = test_font.render("MAIN MENU",True, "Black")
        menu_rect = menu_tekst.get_rect(center = (300, 100))

        #Gumb(image, pos, text_input, font, base_color, hovering_color)
        ACHIVMENT_BUTTON = Gumb(pygame.image.load("Slike/Pozadina_gumb3.png").convert(), (300,500),"ACHIVMENT", test_font, "Black", "White")
        ACHIVMENT_GET_BUTTON = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 600), "GET ACHIVMENT", test_font, "Black", "White")

        screen.blit(menu_tekst,menu_rect)

        for gumb in [ACHIVMENT_BUTTON, ACHIVMENT_GET_BUTTON]:
            gumb.changeColor(MENU_MOUSE_POS)
            gumb.update(screen)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if ACHIVMENT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    click_sound.play()
                    achivment()
                if ACHIVMENT_GET_BUTTON.checkForInput(MENU_MOUSE_POS):
                    novo += 1

        pygame.display.update()


def achivment(): 
    while True:
        #global novo
        print(novo) 

        achivment_surface = pygame.image.load("Slike/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))
        ACHIVMENT_MOUSE_POS = pygame.mouse.get_pos()

        achivment_tekst =achivment_font.render( "Skoči 50 puta" ,False, "White")
        achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 510 ))
        

        achivment_surface = pygame.image.load("Slike/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))

        achivment_table = pygame.image.load("Slike/Table_achivment.jpg").convert()
        achivment_table_rect = achivment_table.get_rect(midleft = (10, 520))
        screen.blit(achivment_table, achivment_table_rect)
        achivment_table = pygame.image.load("Slike/Table_achivment.jpg").convert()
        achivment_table_rect = achivment_table.get_rect(midleft = (10, 370))
        screen.blit(achivment_table, achivment_table_rect)
        achivment_table = pygame.image.load("Slike/Table_achivment.jpg").convert()
        achivment_table_rect = achivment_table.get_rect(midleft = (10, 220))
        screen.blit(achivment_table, achivment_table_rect)


        if novo >= 1:
            screen.blit(achivment_tekst, achivment_tekst_rect)
        if novo >= 2:
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y -150))
        if novo >= 3:
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y -300))



        
        opcije_tekst = naslov_font.render("Postignuća" ,False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 60 ))
        screen.blit(opcije_tekst, opcije_rect)
        
        ACHIVMENT_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300, 700),"Vrati se", test_font, "White", "Green")

        ACHIVMENT_BACK.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_BACK.update(screen)


        #ACHIVMENT_MOVE = Scroll(pygame.image.load("Slike/Scol_linija2.png").convert(), (300, 400), pygame.image.load("Slike/Scrol_gumb.png").convert())
        
        #ACHIVMENT_MOVE.update(screen)

        #if ACHIVMENT_MOVE.checkForInput2(ACHIVMENT_MOUSE_POS):  
        #    if ACHIVMENT_MOVE.changeSurfacePosition(ACHIVMENT_MOUSE_POS, screen):
        #        novo = ACHIVMENT_MOUSE_POS[1]


        ACHIVMENT_RIGHT = Gumb(pygame.image.load("Slike/Strelica.png"), (500, 690),"", test_font, "White", "Green")

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

        achivment_surface = pygame.image.load("Slike/Background_achivment.png").convert()
        screen.blit(achivment_surface, (0,0))
        ACHIVMENT_MOUSE_POS = pygame.mouse.get_pos()

        
        achivment_tekst =achivment_font.render( "Skoči 50 puta" ,False, "White")
        achivment_tekst_rect = achivment_tekst.get_rect(center = (350, 510 ))

        achivment_table = pygame.image.load("Slike/Table_achivment.jpg").convert()
        achivment_table_rect = achivment_table.get_rect(midleft = (10, 520))
        screen.blit(achivment_table, achivment_table_rect)
        achivment_table = pygame.image.load("Slike/Table_achivment.jpg").convert()
        achivment_table_rect = achivment_table.get_rect(midleft = (10, 370))
        screen.blit(achivment_table, achivment_table_rect)
        achivment_table = pygame.image.load("Slike/Table_achivment.jpg").convert()
        achivment_table_rect = achivment_table.get_rect(midleft = (10, 220))
        screen.blit(achivment_table, achivment_table_rect)
        
        if novo >= 4:
            screen.blit(achivment_tekst, achivment_tekst_rect)
        if novo >= 5:
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y -150))
        if novo >= 6:
            screen.blit(achivment_tekst, (achivment_tekst_rect.x , achivment_tekst_rect.y -300))

        

        
        opcije_tekst = naslov_font.render("2" ,False, "White")
        opcije_rect = opcije_tekst.get_rect(center = (300, 60 ))
        screen.blit(opcije_tekst, opcije_rect)
        
        ACHIVMENT_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300, 700),"Vrati se", test_font, "White", "Green")

        ACHIVMENT_BACK.changeColor(ACHIVMENT_MOUSE_POS)
        ACHIVMENT_BACK.update(screen)


        #ACHIVMENT_MOVE = Scroll(pygame.image.load("Slike/Scol_linija2.png").convert(), (300, 400), pygame.image.load("Slike/Scrol_gumb.png").convert())
        
        #ACHIVMENT_MOVE.update(screen)

        #if ACHIVMENT_MOVE.checkForInput2(ACHIVMENT_MOUSE_POS):  
        #    if ACHIVMENT_MOVE.changeSurfacePosition(ACHIVMENT_MOUSE_POS, screen):
        #        novo = ACHIVMENT_MOUSE_POS[1]


        ACHIVMENT_RIGHT = Gumb(pygame.image.load("Slike/Strelica2.png"), (100, 690),"", test_font, "White", "Green")

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


main_menu()
                


