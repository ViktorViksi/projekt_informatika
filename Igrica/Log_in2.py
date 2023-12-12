import pygame
import sys

class Gumb:
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


pygame.init()
screen = pygame.display.set_mode((600, 750))
pygame.display.set_caption("Menu")
test_font = pygame.font.Font(None, 50) 
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
                    with open("login_podaci.txt", encoding="utf-8") as datoteka:
                        podaci = datoteka.readlines()
                        if len(podaci) == 0:
                            podaci.append(f"{user_text}")
                        else:
                            podaci.append(f"\n{user_text}")
                        podaci_text = "".join(podaci)
                    print(podaci)
                    print(podaci_text)
                    with open("login_podaci.txt","wt",-1,encoding="utf-8") as datoteka:
                        datoteka.write(podaci_text)
                    



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
    
