import pygame
import sys
from gumb import Gumb
from level import level
from endless import endless
from menu import Scroll, main_menu

screen = pygame.display.set_mode((600, 750))

zvuk = 0.5
zvuk2 = 0.5
bg_music = pygame.mixer.Sound("Audio/He's a Pirate.mp3")
bg_music.set_volume(zvuk)
bg_music.play(loops= -1)
click_sound  = pygame.mixer.Sound("Audio/Bonk Sound Effect.mp3")
click_sound.set_volume(zvuk2)
stisnut = 0
stisnut2 = 0

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

        OPTIONS_BACK = Gumb(pygame.image.load("Slike/Pozadina_gumb5.png").convert(), (100, 700), "Vrati se", test_font, "White", "Green")

        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(screen)

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
    

def pause_menu(scrn, score, podaci, data):
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
        
        NASTAVI = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300,400),"NASTAVI", test_font, "Black", "White")
        OPTIONS = Gumb(pygame.image.load("Slike/Pozadina_gumb3.png").convert(), (300,500),"OPTIONS", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

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
                    main_menu(podaci, data)
                    
        pygame.display.update()
        
        if nastavi:
            break
    
    pygame.time.delay(1000)
    scrn.blit(oldScreen, (0,0))

def level_pause(scrn, score, podaci, data):
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
        
        NASTAVI = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300,400),"NASTAVI", test_font, "Black", "White")
        OPTIONS = Gumb(pygame.image.load("Slike/Pozadina_gumb3.png").convert(), (300,500),"OPTIONS", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

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
                    main_menu(podaci, data)
                    
        pygame.display.update()
        
        if nastavi:
            break
    
    pygame.time.delay(1000)
    scrn.blit(oldScreen, (0,0))

def game_over(scrn, score, hscore, podaci, data):
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
        
        PONOVO = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300,500),"IGRAJ PONOVO", test_font, "Black", "White")
        MENU = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 600), "MENU", test_font, "Black", "White")
        PAUSE_BACK = Gumb(pygame.transform.scale(pygame.image.load("Slike/Pauza_gumb.png").convert(), (40, 40)), (560, 40), "", test_font, "White", "Green")

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
                    main_menu(podaci, data)
                    
        pygame.display.update()

def level_start(scrn, brojLevela, type, podaci, data):
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
    
    if locked:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            intro_tekst = test_font.render(tekst,True, "Black")
            intro_rect = intro_tekst.get_rect(center = (300, 100))
            
            msg_tekst = test_font.render(f"Level je zaključan",True, "Black")
            msg_rect = msg_tekst.get_rect(center = (300, 200))
            
            NATRAG = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 550, "NATRAG", test_font, "Black", "White"))

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
                        scrn.blit(oldScreen, (0,0))
                        
            pygame.display.update()
    else:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()

            intro_tekst = test_font.render(tekst,True, "Black")
            intro_rect = intro_tekst.get_rect(center = (300, 100))
            
            IGRAJ = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300,450),"IGRAJ", test_font, "Black", "White")
            NATRAG = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 550), "NATRAG", test_font, "Black", "White")

            scrn.blit(intro_tekst,intro_rect)
            
            if type == 0:
                image = pygame.image.load("Slike/Menu/stars_0.png")
                scrn.blit(image.get_rect(center = (300, 200)))
            elif type == 1:
                image = pygame.image.load("Slike/Menu/stars_1.png")
                scrn.blit(image.get_rect(center = (300, 200)))
            elif type == 2:
                image = pygame.image.load("Slike/Menu/stars_2.png")
                scrn.blit(image.get_rect(center = (300, 200)))
            elif type == 3:
                image = pygame.image.load("Slike/Menu/stars_3.png")
                scrn.blit(image.get_rect(center = (300, 200)))

            for gumb in [IGRAJ, NATRAG]:
                gumb.changeColor(MENU_MOUSE_POS)
                gumb.update(scrn)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if IGRAJ.checkForInput(MENU_MOUSE_POS):
                        level(brojLevela, podaci, data)
                    if NATRAG.checkForInput(MENU_MOUSE_POS):
                        scrn.blit(oldScreen, (0,0))
                        
            pygame.display.update()

def level_end(scrn, brojLevela, type, podaci, data):
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
            
        PONOVO = Gumb(pygame.image.load("Slike/Pozadina_gumb2.png").convert(), (300,450),"PONOVO", test_font, "Black", "White")
        NATRAG = Gumb(pygame.image.load("Slike/Pozadina_gumb6.png").convert(), (300, 550), "NATRAG", test_font, "Black", "White")

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
                    level(brojLevela, podaci, data)
                if NATRAG.checkForInput(MENU_MOUSE_POS):
                    main_menu(podaci, data)
                        
            pygame.display.update()