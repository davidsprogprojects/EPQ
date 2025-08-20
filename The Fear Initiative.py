import pygame
import time
import sys
import random
pygame.init()
def fonts():
    global menuBttns, introTxt, tutFont
    menuBttns = pygame.font.SysFont("Arial Black", 30)
    introTxt = pygame.font.SysFont("Arial Black", 20)
    helpTxt = pygame.font.SysFont("Arial Black", 50)
    tutFont = pygame.font.SysFont("Arial Black", 30)

def events():
    global keys, click, mouse
    keys = pygame.key.get_pressed()
    click = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()


def startGame(screen):
    global play_game, tutMap1
    if play_game == False:
        d = 0
        g = 0
        global draw_menu
        draw_menu = False
        introText(screen, devilA1, godA1, devilPos1, godPos1)
    elif play_game == True:
        tutorial(screen)
    

def tutorial(screen):
    if tutMap1 == True:
        tutorialMap1(screen)
    elif tutMap2 == True:
        tutorialMap2(screen)
    elif tutMap3 == True:
        tutorialMap3(screen)
    elif tutMap4 == True:
        tutorialMap4(screen)
    elif tutMap5 == True:
        tutorialMap5(screen)
    else:
        gameStart(screen)


def optionsSelect(screen):
    global choice
    if mouse[0] >= 230 and mouse[0] <= 470 and mouse[1] >= 80 and mouse[1] <= 157 and start_game == False:
        PlayGame = menuBttns.render("Play Game", True, (255,255,255))
        screen.blit(PlayGame, (265,95))
        pygame.display.update()
        if click[0] == 1:
            choice = "start game"
            startGame(screen)
            
    elif mouse[0] >= 230 and mouse[0] <= 470 and mouse[1] >= 162 and mouse[1] <= 239 and open_settings == False:
        Settings = menuBttns.render("Settings", True, (255,255,255))
        screen.blit(Settings, (280,175))
        pygame.display.update()
        if click[0] == 1:
            choice = "settings"

    elif mouse[0] >= 230 and mouse[0] <= 470 and mouse[1] >= 244 and mouse[1] <= 321 and quit_game == False:
        Quit = menuBttns.render("Quit", True, (255,255,255))
        screen.blit(Quit, (315,260))
        pygame.display.update()

def playerControl(screen):
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and playerPosTut[0] >= smallx:
        playerPosTut[0] = int(playerPosTut[0]) - 15
        #print(playerPosTut[0])
        pygame.display.update()
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and playerPosTut[0] <= bigx:
        playerPosTut[0] = int(playerPosTut[0]) + 15
        #print(playerPosTut[0])
        pygame.display.update()
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and playerPosTut[1] >= smallY:
        playerPosTut[1] = int(playerPosTut[1]) - 15
        #print(playerPosTut[1])
        pygame.display.update()
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and playerPosTut[1] <= bigY:
        playerPosTut[1] = int(playerPosTut[1]) + 15
        #print(playerPosTut[1])
        pygame.display.update()

def playerUpdate(screen):
    global Player, FacingLeft, FacingRight, FacingUp, FacingDown
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]):
        Player = pygame.image.load(r"Character\Main_Char_2.png")
        FacingLeft = True
        FacingRight = False
        FacingDown = False
        FacingUp = False

        pygame.display.update()
        

    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]):
        Player = pygame.image.load(r"Character\Main_Char_4.png")

        FacingLeft = False
        FacingRight = True
        FacingDown = False
        FacingUp = False
        pygame.display.update()

    if (keys[pygame.K_UP] or keys[pygame.K_w]):
        Player = pygame.image.load(r"Character\Main_Char_3.png")
        FacingLeft = False
        FacingRight = False
        FacingDown = False
        FacingUp = True
        pygame.display.update()

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]):
        Player = pygame.image.load(r"Character\Main_Char_1.png")
        FacingLeft = False
        FacingRight = False
        FacingDown = True
        FacingUp = False
        pygame.display.update()


        
def textFloat(screen):
    global TxCrd, floatDown
    if TxCrd < 40 and floatDown == True:
        TxCrd = TxCrd + 1
        if TxCrd == 40:
            floatDown = False
        
    else:
        TxCrd = TxCrd - 1
        if TxCrd == 30:
            floatDown = True



    
def talking(screen):
    global god_talking, devil_talking, devilA1, devilA2, godA1, godA2
    sub = godA1
    subs = devilA1
    if god_talking == True:
        pygame.time.delay(150)
        godA1 = godA2
        godA2 = sub

    else:
        godA1 = sub
        
    if devil_talking == True:
        pygame.time.delay(200)
        devilA1 = devilA2
        devilA2 = subs
        
    else:
        devilA1 = subs
        

    
    

def options(screen):
    PlayGame = menuBttns.render("Play Game", True, (0,255,0))
    screen.blit(PlayGame, (265,95))
    Settings = menuBttns.render("Settings", True, (0,255,0))
    screen.blit(Settings, (280,175))
    Quit = menuBttns.render("Quit", True, (0,255,0))
    screen.blit(Quit, (315,260))
    pygame.display.update()
    optionsSelect(screen)
    

def menu(screen):
    pygame.draw.rect(screen,(0,0,255), (225,75,250,250))
    pygame.draw.rect(screen,(255,0,0), (230,80,240,77))
    pygame.draw.rect(screen,(255,0,0), (230,162,240,77))
    pygame.draw.rect(screen,(255,0,0), (230,244,240,77))
    options(screen)

            
def tutorialText(screen):
    global up, down, left, right
    up = tutFont.render("Press W", True, (0,0,255))
    down = tutFont.render("Press S", True, (0,0,255))
    left = tutFont.render("Press A", True, (0,0,255))
    right = tutFont.render("Press D", True, (0,0,255))

def introText(screen, devilA1, godA1, devilPos, godPos):
    x = 0
    for line in godS1:
        GTemp.append(line)
        x = x + 1
    x = 0
    for line in devilS1:
        DTemp.append(line)
        x = x + 1
    for i in range(0,x):
        script_complete = False
        textArrayG = introTxt.render(GTemp[i], True, (0,255,0))
        textArrayD = introTxt.render(DTemp[i], True, (255,0,0))
        gIntroText.append(textArrayG)
        dIntroText.append(textArrayD)

    intro(screen, devilA1, godA1, devilPos, godPos)

def intro(surface, devilA1, godA1, devilPos, godPos):
    global play_game
    #surface.fill((0,0,0))
    #pygame.draw.rect(surface, (0,255,0), (godPos[0], godPos[1], 100, 100))
    #surface.blit(devil, (devilPos[0], devilPos[1]))               
    #pygame.draw.rect(surface, (0,0,255), (mePos[0], mePos[1], 50, 50))

    if j >=11:
        pygame.draw.rect(surface, (0,0,0), (mePos[0], mePos[1], 50, 50))
    if j <= 12:
        script(surface, devilA1, godA1, devilPos, godPos)
    else:
        play_game = True
        j == 13




    
def script(screen, devilA1, godA1, devilPos, godPos):
    global j, enter, value, g, d, h
    value = pygame.key.get_pressed()


    if g == 1 and j == 0:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 1 and j == 0:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 2 and j == 1:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 2 and j == 1:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 3 and j == 2:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 3 and j == 2:
        badText(screen, devilA1, godA1, devilPos, godPos)
  

    elif g == 4 and j == 3:
        
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 4 and j == 3:
        h = 9
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 5 and j == 4:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 5 and j == 4:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 6 and j == 5:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 6 and j == 5:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 7 and j == 6:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 7 and j == 6:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 8 and j == 7:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 8 and j == 7:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 9 and j == 8:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 9 and j == 8:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 10 and j == 9:
        goodText(screen, devilA1, godA1, devilPos, godPos)

    elif d == 10 and j == 9:
        badText(screen, devilA1, godA1, devilPos, godPos)

    elif g == 11 and j == 10:
        goodText(screen, devilA1, godA1, devilPos, godPos)
        h = 10

    elif d == 11 and j == 10:
        badText(screen, devilA1, godA1, devilPos, godPos)
        h = 10

    elif g == 12 and j == 11:
        goodText(screen, devilA1, godA1, devilPos, godPos)
        h = 10

    elif d == 12 and j == 11:
        badText(screen, devilA1, godA1, devilPos, godPos)
        h = 10

    elif g == 13 and j == 12:
        goodText(screen, devilA1, godA1, devilPos, godPos)
        h = 10

    elif d == 13 and j == 12:
        badText(screen, devilA1, godA1, devilPos, godPos)
        



def goodText(screen, devilA1, godA1, devilPos, godPos):
    global j, g, d, god_talking, h, asleepR1, asleepR2, asleepR3, asleepR4, asleepR5, asleepR5, asleepR6, asleepR7, asleepR8, asleepR9
    screen.fill((0,0,0))
    screen.blit(godA1, (godPos[0], godPos[1]))
    screen.blit(devilA1, (devilPos[0], devilPos[1]))
    if h == 0:
        screen.blit(asleepR1, (mePos[0], mePos[1]))
    elif h >= 1:
        if h <= 9:
            time.sleep(0.05)
            if h == 1:
                screen.blit(asleepR1, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 2:
                
                screen.blit(asleepR2, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 3:
                screen.blit(asleepR3, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 4:
                screen.blit(asleepR4, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 5:
                screen.blit(asleepR5, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 6:
                screen.blit(asleepR6, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 7:
                screen.blit(asleepR7, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 8:
                screen.blit(asleepR8, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 9:
                screen.blit(asleepR9, (mePos[0], mePos[1]))
    elif h == 9:
        screen.blit(asleepR9, (mePos[0], mePos[1]))
    elif h == 10:
        h = 10
            
    boxes(screen)
    god_talking = True
    if len(GTemp[j]) >= 55:
        new = GTemp[j].split(".")
        it = introTxt.render(new[0], True, (0,255,0))
        gIntroText[j] = it
    screen.blit(gIntroText[j], (20,300))
    if len(GTemp[j]) >= 55:
        it = introTxt.render(new[1],True, (0,255,0))
        gIntroText[j] = it
        screen.blit(gIntroText[j], (20,320))
    if len(GTemp[j]) >= 65:
        it = introTxt.render(new[2],True, (0,255,0))
        gIntroText[j] = it
        screen.blit(gIntroText[j], (20,340))
    if len(GTemp[j]) >= 75:
        it = introTxt.render(new[3],True, (0,255,0))
        gIntroText[j] = it
        screen.blit(gIntroText[j], (20,360))
    pygame.display.update()        
        
    
    #time.sleep(0.5)
    if enter == False:
        god_talking = False
        d = d + 1
        g = g + 1

        
        intro(screen, devilA1, godA1, devilPos, godPos)

def badText(screen, devilA1, godA1, devilPos, godPos):
    global j, g, d, devil_talking, h, asleepR1, asleepR9
    screen.fill((0,0,0))
    screen.blit(godA1, (godPos[0], godPos[1]))
    screen.blit(devilA1, (devilPos[0], devilPos[1]))               
    if h == 0:
        screen.blit(asleepR1, (mePos[0], mePos[1]))
    elif h >= 1:
        if h <= 9:
            time.sleep(0.05)
            if h == 1:
                screen.blit(asleepR1, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 2:
                
                screen.blit(asleepR2, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 3:
                screen.blit(asleepR3, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 4:
                screen.blit(asleepR4, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 5:
                screen.blit(asleepR5, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 6:
                screen.blit(asleepR6, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 7:
                screen.blit(asleepR7, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 8:
                screen.blit(asleepR8, (mePos[0], mePos[1]))
                h = h + 1
            elif h == 9:
                screen.blit(asleepR9, (mePos[0], mePos[1]))
    elif h == 9:
        screen.blit(asleepR9, (mePos[0], mePos[1]))
            
    boxes(screen)
    
    devil_talking = True
    if len(DTemp[j]) >= 55:
        new = DTemp[j].split(".")
        it = introTxt.render(new[0], True, (255,0,0))
        dIntroText[j] = it
    screen.blit(dIntroText[j], (20,300))
    if len(DTemp[j]) >= 55:
        it = introTxt.render(new[1], True, (255,0,0))
        dIntroText[j] = it
        screen.blit(dIntroText[j], (20,320))
    if len(DTemp[j]) >= 65:
        it = introTxt.render(new[2],True, (255,0,0))
        dIntroText[j] = it
        screen.blit(dIntroText[j], (20,340))
    if len(DTemp[j]) >= 75:
        it = introTxt.render(new[3],True, (255,0,0))
        dIntroText[j] = it
        screen.blit(dIntroText[j], (20,360))
    pygame.display.update()


            
    #time.sleep(0.5)
    if enter == True:
        j = j + 1
        devil_talking = False
        if j == 2:
            h = 1
        intro(screen, devilA1, godA1, devilPos, godPos)

def boxes(screen):
    text_border = [5, 290]
    text = [10, 295]
    pygame.draw.rect(screen, (255,255,255), (text_border[0], text_border[1], 690, 105))
    pygame.draw.rect(screen, (0,0,0), (text[0], text[1], 680, 95))
    pygame.display.update()


def char():
    global mePos, playerPosTut, asleepR1, asleepR2, asleepR3, asleepR4, asleepR5, asleepR5, asleepR6, asleepR7, asleepR8, asleepR9
    mePos = [260,125]
    asleep1 = pygame.image.load(r"Character\Asleep_1.png")
    asleep2 = pygame.image.load(r"Character\Asleep_2.png")
    asleep3 = pygame.image.load(r"Character\Asleep_3.png")
    asleep4 = pygame.image.load(r"Character\Asleep_4.png")
    asleep5 = pygame.image.load(r"Character\Asleep_5.png")
    asleep6 = pygame.image.load(r"Character\Asleep_6.png")
    asleep7 = pygame.image.load(r"Character\Asleep_7.png")
    asleep8 = pygame.image.load(r"Character\Asleep_8.png")
    asleep9 = pygame.image.load(r"Character\Asleep_9.png")

    asleepR1 = pygame.transform.scale(asleep1, (150,130))
    asleepR2 = pygame.transform.scale(asleep2, (150,130))
    asleepR3 = pygame.transform.scale(asleep3, (150,130))
    asleepR4 = pygame.transform.scale(asleep4, (150,130))
    asleepR5 = pygame.transform.scale(asleep5, (150,130))
    asleepR6 = pygame.transform.scale(asleep6, (150,130))
    asleepR7 = pygame.transform.scale(asleep7, (150,130))
    asleepR8 = pygame.transform.scale(asleep8, (150,130))
    asleepR9 = pygame.transform.scale(asleep9, (150,130))

    playerPosTut = [225,100]

def god():
    global godS1, godPos1, godA1, godA2, GTemp, gIntroText
    godS1 = open("God1.txt","r")
    godPos1 = [470, 40]
    god = pygame.image.load(r"God\God_1.png")
    godA1 = pygame.transform.scale(god, (200,200))
    god2 = pygame.image.load(r"God\God_2.png")
    godA2 = pygame.transform.scale(god2, (200,200))
    GTemp = []
    gIntroText= []
    

def devil():
    global devilS1, devilPos1, devilA1, devilA2, DTemp, dIntroText
    devilS1 = open("Devil1.txt","r")
    devilPos1 = [0, 0]
    devil = pygame.image.load(r"Devil\Devil_1.png")
    devilA1 = pygame.transform.scale(devil, (250, 250))
    devil2 = pygame.image.load(r"Devil\Devil_2.png")
    devilA2 = pygame.transform.scale(devil2, (250, 250))
    DTemp = []
    dIntroText = []
    

def tutorialMap1(screen):
    global tutMap1, tutMap2, bigx, smallx, bigY, smallY
    bigx = 295
    smallx = 155
    bigY = 180
    smallY = -90
    tutorialmap = pygame.image.load(r"Map\Tutorial1.png")
    tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
    screen.blit(tutorialmap, (0,0))
    player(screen)
    screen.blit(up, (285, TxCrd))
    if playerPosTut[1] == -80:
        tutMap1 = False
        tutMap2 = True
        playerPosTut[1] = 250


def tutorialMap2(screen):
    global tutMap2, tutMap3, bigx, smallx
    bigx = 295
    smallx = 155
    tutorialmap = pygame.image.load(r"Map\Tutorial2.png")
    tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
    screen.blit(tutorialmap, (0,0))
    player(screen)
    screen.blit(up, (285, TxCrd))
    if playerPosTut[1] == -80:
        tutMap2 = False
        tutMap3 = True
        playerPosTut[1] = 250


def tutorialMap3(screen):
    global tutMap3, tutMap4, rock, bigx, smallx, bigY, smallY
    bigx = 295
    smallx = 155
    if rock == False:
        tutorialmap = pygame.image.load(r"Map\Tutorial3.png")
        tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
        screen.blit(tutorialmap, (0,0))
        player(screen)
        screen.blit(up, (285, TxCrd))
    elif rock == True:
        tutorialmap = pygame.image.load(r"Map\Tutorial3_1.png")
        tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
        screen.blit(tutorialmap, (0,0))
        player(screen)
        screen.blit(down, (285, TxCrd))
    if playerPosTut[1] == 100:
        rock = True
        smallY = 50
        bigY = 10000000
    if rock == True and playerPosTut[1] == 250:
        playerPosTut[1] = -125
        rock = False
        tutMap3 = False
        tutMap4 = True

def tutorialMap4(screen):
    global tutMap4, tutMap5, rock, bigx, smallx, bigY, smallY
    bigx = 295
    smallx = 155
    if rock == False:
        tutorialmap = pygame.image.load(r"Map\Tutorial4.png")
        tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
        screen.blit(tutorialmap, (0,0))
        player(screen)
        screen.blit(down, (285, TxCrd))
        if playerPosTut[0] >= 315:
            bigY = 50
            smallY = -40
    elif rock == True:
        tutorialmap = pygame.image.load(r"Map\Tutorial4_1.png")
        tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
        screen.blit(tutorialmap, (0,0))
        player(screen)
        screen.blit(right, (285, TxCrd))
        if playerPosTut[0] >= 315:
            bigY = 50
            smallY = -10
        else:
            bigY = 55
            smallY = -35
        if playerPosTut[1] > -40:
            bigx = 100000
            smallx = 125
        
    if playerPosTut[1] == -50:
        rock = True
    if rock == True and playerPosTut[0] == 585:
        playerPosTut[0] = -130
        rock = False
        tutMap4 = False
        tutMap5 = True

def tutorialMap5(screen):
    global pMap1, tutMap5, rock, bigx, smallx, bigY, smallY
    bigx = 330
    smallx = -90
    bigY = 50
    smallY = -30
    if rock == False:
        tutorialmap = pygame.image.load(r"Map\Tutorial4.png")
        tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
        screen.blit(tutorialmap, (0,0))
        player(screen)
        screen.blit(right, (285, TxCrd))

    elif rock == True:
        tutorialmap = pygame.image.load(r"Map\Tutorial4_2.png")
        tutorialmap = pygame.transform.scale(tutorialmap, (700,400))
        screen.blit(tutorialmap, (0,0))
        player(screen)
        screen.blit(left, (285, TxCrd))

        
        if playerPosTut[0] > 130 and playerPosTut[0] <= 310:
            smallY = -35
            bigY = 65

            
        elif playerPosTut[0] < 130:
            bigY = 50
            smallY = -10            
        if playerPosTut[1] < -35:
            bigx = 290
            smallx = 155
            smally = -35

            
        else:
            bigx = 335
            
    if playerPosTut[0] == 125:
        rock = True

    if rock == True and playerPosTut[0] <= -90:
        playerPosTut[0] = 585
        rock = False
        tutMap5 = False
        pMap1 = True

def gameStart(screen):
    global enter

    
    
    if pMap1 == True:
        PuzzleMap1(screen)
    elif pMap2 == True:
        PuzzleMap2(screen)
    elif pMap3 == True:
        PuzzleMap3(screen)
    elif pMap4 == True:
        PuzzleMap4(screen)
    elif pMap4_1 == True:
        PuzzleMap4_1(screen)
    elif pMap4_2 == True:
        PuzzleMap4_2(screen)
    elif pMap4_3 == True:
        PuzzleMap4_3(screen)
    elif pMap5 == True:
        LightsOff = False
        PuzzleMap5(screen)
    elif Page1 == True:
        instructions(screen)
    elif pMap5_1 == True:
        PuzzleMap5_1(screen)
    elif pMap5_2 == True:
        PuzzleMap5_2(screen)
    elif pMap5_3 == True:
        PuzzleMap5_3(screen)
    elif pMap6 == True:
        PuzzleMap6(screen)
    elif pMap6_1 == True:
        PuzzleMap6_1(screen)
    elif pMap6_2 == True:
        PuzzleMap6_2(screen)
    elif pMap6_3 == True:
        PuzzleMap6_3(screen)
    elif pMap7 == True:
        PuzzleMap7(screen)
    elif pMap7_1 == True:
        PuzzleMap7_1(screen)
    elif pMap7_2 == True:
        PuzzleMap7_2(screen)
    elif WIP == True:
        thanks(screen)




def PuzzleMap1(screen):
    global smallx, bigx, smallY, bigY, pMap1, pMap2
    smallx = 180
    bigx = 570
    gamemap = pygame.image.load(r"Map\Map1.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    player(screen)
    if playerPosTut[0] < 315:
        smallY = -500000
    if playerPosTut[1] < -30:
        bigx = 295
    if playerPosTut[1] == -80:
        playerPosTut[1] = 250
        pMap1 = False
        pMap2 = True

    
def PuzzleMap2(screen):
    global smallx, bigx, smallY, bigY, pMap2, pMap3
    smallx = 180
    bigx = 295
    smallY = -90
    bigY = 180
    gamemap = pygame.image.load(r"Map\Map2.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    player(screen)
    if playerPosTut[1] == -80:
        playerPosTut[1] = 250
        pMap2 = False
        pMap3 = True
        
def PuzzleMap3(screen):
    global smallx, bigx, smallY, bigY, pMap3, pMap4, Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Exit
    smallx = 180
    bigx = 295
    smallY = -90
    bigY = 180
    smallY = -100000
    smallX = 1000000
    gamemap = pygame.image.load(r"Map\Map3.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    player(screen)
    if playerPosTut[1] == -80:
        playerPosTut[1] = 250
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Button5 = False
        Button6 = False
        Button7 = False
        Button8 = False
        Exit = False
        pMap3 = False
        pMap4 = True
def PuzzleMap4(screen):
    global smallx, bigx, smallY, bigY, pMap4, pMap4_1, enter
    bigx = 555
    smallx = -90
    smallY = -90
    bigY = 250
    gamemap = pygame.image.load(r"Map\Map4.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    player(screen)
    if playerPosTut[1] == -50 and FacingDown == True and playerPosTut[0] <= 265 and playerPosTut[0] >=185:
        pMap4 = False
        pMap4_1 = True


    

def PuzzleMap4_1(screen):
    global smallx, bigx, smallY, bigY, pMap4_2, pMap4_1, enter
    bigx = 555
    smallx = -90
    smallY = -90
    bigY = 250
    gamemap = pygame.image.load(r"Map\Map4_1.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    player(screen)
    if playerPosTut[1] > -50 and playerPosTut[1] <= 40 and playerPosTut[0] <=265 and playerPosTut[0] >=185:
        playerPosTut[1] = -120
        pMap4_1 = False
        pMap4_2 = True

def PuzzleMap4_2(screen):
    global smallx, bigx, smallY, bigY, pMap4_3, pMap4_2, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    screen.fill((0,0,0))

    if playerPosTut[1] <= 300:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:
        playerPosTut[1] = -120
        pMap4_2 = False
        pMap4_3 = True
    
def PuzzleMap4_3(screen):
    global smallx, bigx, smallY, bigY, pMap4_3, pMap5, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    gamemap = pygame.image.load(r"Map\Puzzle1.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    pygame.draw.rect(screen, (0,49,82), (40,100,100,100))
    pygame.draw.rect(screen, (0,49,82), (560,100,100,100))
    pygame.draw.rect(screen, (0,49,82), (40,250,100,100))
    pygame.draw.rect(screen, (0,49,82), (560,250,100,100))

    if playerPosTut[1] <= 0:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:

        enter = False
        pMap4_3 = False
        pMap5 = True    
    
def PuzzleMap5(screen):
    global smallx, bigx, smallY, bigY, pMap5, pMap5_1, pMap5_2, Page1, LightsOff, Button1, Button2, Button3, Button4, Exit, enter
    bigx = 555
    smallx = -90
    smallY = -50
    bigY = 250
    if playerPosTut[1] == -60 and (playerPosTut[0] == 135 or playerPosTut[0] ==  150) and FacingUp == True and enter == True:
        enter = False
        bigx = 0
        smallx = 100000
        smallY = 100000
        bigY = 0
        pMap5 = False
        Page1 = True
    if playerPosTut[1] == -60 and (playerPosTut[0] == 285 or playerPosTut[0] ==  300) and FacingUp == True and enter == True:
        enter = False
        LightsOff = True
        pMap5_1 = True
        pMap5 = False
    if LightsOff == False:
        gamemap = pygame.image.load(r"Map\Puzzle1.png")
        gamemap = pygame.transform.scale(gamemap, (700,400))
        screen.blit(gamemap, (0,0))
        pygame.draw.rect(screen, (0,49,82), (40,100,100,100))
        pygame.draw.rect(screen, (0,49,82), (560,100,100,100))
        pygame.draw.rect(screen, (0,49,82), (40,250,100,100))
        pygame.draw.rect(screen, (0,49,82), (560,250,100,100))
        Buttons(screen)
        player(screen)
    if playerPosTut[0] >= -75 and playerPosTut[1] >= -65 and playerPosTut[0] <= 0 and playerPosTut[1] <= 10:
        Button1 = True
        player(screen)
    if playerPosTut[0] >= -75 and playerPosTut[1] >= 70 and playerPosTut[0] <= 0 and playerPosTut[1] <= 160:
        Button2 = True
        player(screen)
    if playerPosTut[0] >= 450 and playerPosTut[1] >= -65 and playerPosTut[0] <= 525 and playerPosTut[1] <= 10:
        Button3 = True
        player(screen)
    if playerPosTut[0] >= 450 and playerPosTut[1] >= 70 and playerPosTut[0] <= 525 and playerPosTut[1] <= 160:
        Button4 = True
        player(screen)
    if Button1 == True and Button2 == False and Button3 == False and Button4 == True:
        Exit = True
        player(screen)
    if playerPosTut[0] >= 180 and playerPosTut[0] <= 270 and playerPosTut[1] >= -20 and playerPosTut[1] <= 55 and Exit == True:
        playerPosTut[1] = -120
        enter = False
        LightsOff = False
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Button5 = False
        Button6 = False
        Exit = False
        pMap5_2 = True
        pMap5_1 = False
        pMap5 = False
        
def PuzzleMap5_1(screen):
    global smallx, bigx, smallY, bigY, pMap5, pMap5_1, Page1, LightsOff, Button1, Button2, Button3, Button4, Exit, enter
    gamemap1 = pygame.image.load(r"Map\Puzzle1_1.png")
    gamemap1 = pygame.transform.scale(gamemap1, (700,400))
    screen.blit(gamemap1, (0,0))
    bigx = -100000
    smallx = 100000
    bigY = -1000000
    smallY = 10000000
    pygame.draw.rect(screen, (255,255,255), (40,100,100,100))
    pygame.draw.rect(screen, (255,255,255), (560,250,100,100))
    player(screen)
    
    if playerPosTut[1] == -60 and (playerPosTut[0] == 285 or playerPosTut[0] ==  300) and FacingUp == True and enter == True and LightsOff == True:
        LightsOff = False
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Exit = False
        pMap5 = True
        pMap5_1 = False
        enter = False

def PuzzleMap5_2(screen):
    global smallx, bigx, smallY, bigY, pMap5_2, pMap5_3, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    screen.fill((0,0,0))

    if playerPosTut[1] <= 300:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:
        playerPosTut[1] = -210
        
        pMap5_2 = False
        pMap5_3 = True

def PuzzleMap5_3(screen):
    global smallx, bigx, smallY, bigY, pMap5_3, pMap6, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    gamemap = pygame.image.load(r"Map\Puzzle1_Level2+.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    pygame.draw.rect(screen, (0,49,82), (40,100,100,100))
    pygame.draw.rect(screen, (0,49,82), (560,100,100,100))
    pygame.draw.rect(screen, (0,49,82), (190,100,100,100))
    pygame.draw.rect(screen, (0,49,82), (410,100,100,100))
    pygame.draw.rect(screen, (0,49,82), (40,250,100,100))
    pygame.draw.rect(screen, (0,49,82), (560,250,100,100))

    if playerPosTut[1] <= 0:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:
        enter = False
        pMap5_3 = False
        pMap6 = True
        
def PuzzleMap6(screen):
    global smallx, bigx, smallY, bigY, pMap6, pMap6_1, pMap6_2, Page1, LightsOff, Button1, Button2, Button3, Button4, Button5, Button6, Exit, enter
    bigx = 555
    smallx = -90
    smallY = -50
    bigY = 250
    #if playerPosTut[1] == -60 and (playerPosTut[0] == 135 or playerPosTut[0] ==  150) and FacingUp == True:
     #   Page1 = True
    if playerPosTut[1] == -60 and (playerPosTut[0] == 285 or playerPosTut[0] ==  300) and FacingUp == True and enter == True:
        enter = False
        LightsOff = True
        pMap6_1 = True
        pMap6 = False
    if LightsOff == False:
        gamemap = pygame.image.load(r"Map\Puzzle1_Level2+.png")
        gamemap = pygame.transform.scale(gamemap, (700,400))
        screen.blit(gamemap, (0,0))
        pygame.draw.rect(screen, (0,49,82), (40,100,100,100))
        pygame.draw.rect(screen, (0,49,82), (560,100,100,100))
        pygame.draw.rect(screen, (0,49,82), (190,100,100,100))
        pygame.draw.rect(screen, (0,49,82), (410,100,100,100))
        pygame.draw.rect(screen, (0,49,82), (40,250,100,100))
        pygame.draw.rect(screen, (0,49,82), (560,250,100,100))
        Buttons(screen)
        player(screen)
    if playerPosTut[0] >= -75 and playerPosTut[1] >= -65 and playerPosTut[0] <= 0 and playerPosTut[1] <= 10:
        Button1 = True
        player(screen)
    if playerPosTut[0] >= -75 and playerPosTut[1] >= 70 and playerPosTut[0] <= 0 and playerPosTut[1] <= 160:
        Button2 = True
        player(screen)
    if playerPosTut[0] >= 450 and playerPosTut[1] >= -65 and playerPosTut[0] <= 525 and playerPosTut[1] <= 10:
        Button3 = True
        player(screen)
    if playerPosTut[0] >= 450 and playerPosTut[1] >= 70 and playerPosTut[0] <= 525 and playerPosTut[1] <= 160:
        Button4 = True
        player(screen)
    if playerPosTut[0] >= 300 and playerPosTut[1] >= -60 and playerPosTut[0] <= 375 and playerPosTut[1] <= 15:
        Button5 = True
        player(screen)
    if playerPosTut[0] >= 75 and playerPosTut[1] >= -60 and playerPosTut[0] <= 165 and playerPosTut[1] <= 15:
        Button6 = True
        player(screen)
    if Button1 == False and Button2 == True and Button3 == False and Button4 == True and Button5 == False and Button6 == True:
        Exit = True
        player(screen)
    if playerPosTut[0] >= 180 and playerPosTut[0] <= 270 and playerPosTut[1] >= -20 and playerPosTut[1] <= 55 and Exit == True:
        playerPosTut[1] = -120
        enter = False
        LightsOff = False
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Button5 = False
        Button6 = False
        Button7 = False
        Button8 = False
        Exit = False
        pMap6_2 = True
        pMap6_1 = False
        pMap6 = False
def PuzzleMap6_1(screen):
    global smallx, bigx, smallY, bigY, pMap6, pMap6_1, Page1, LightsOff, Button1, Button2, Button3, Button4, Button5, Button6, Exit, enter
    gamemap1 = pygame.image.load(r"Map\Puzzle1_Level2+_1.png")
    gamemap1 = pygame.transform.scale(gamemap1, (700,400))
    screen.blit(gamemap1, (0,0))
    bigx = -100000
    smallx = 100000
    bigY = -1000000
    smallY = 10000000
    pygame.draw.rect(screen, (255,255,255), (190,100,100,100))#6
    pygame.draw.rect(screen, (255,255,255), (40,250,100,100))#2
    pygame.draw.rect(screen, (255,255,255), (560,250,100,100))#4

    player(screen)
    
    if playerPosTut[1] == -60 and (playerPosTut[0] == 285 or playerPosTut[0] ==  300) and FacingUp == True and enter == True and LightsOff == True:
        enter = False
        LightsOff = False
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Button5 = False
        Button6 = False
        Exit = False
        pMap6 = True
        pMap6_1 = False

def PuzzleMap6_2(screen):
    global smallx, bigx, smallY, bigY, pMap6_2, pMap6_3, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    screen.fill((0,0,0))

    if playerPosTut[1] <= 300:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:
        playerPosTut[1] = -210
        pMap6_2 = False
        pMap6_3 = True

def PuzzleMap6_3(screen):
    global smallx, bigx, smallY, bigY, pMap6_3, pMap7, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    gamemap = pygame.image.load(r"Map\Puzzle1_Level2+.png")
    gamemap = pygame.transform.scale(gamemap, (700,400))
    screen.blit(gamemap, (0,0))
    pygame.draw.rect(screen, (0,49,82), (40,100,100,100)) #1
    pygame.draw.rect(screen, (0,49,82), (560,100,100,100)) #3
    pygame.draw.rect(screen, (0,49,82), (190,100,100,100)) #6
    pygame.draw.rect(screen, (0,49,82), (410,100,100,100)) #5
    pygame.draw.rect(screen, (0,49,82), (40,250,100,100)) #2
    pygame.draw.rect(screen, (0,49,82), (560,250,100,100)) #4
    pygame.draw.rect(screen, (0,49,82), (190,250,100,100)) #7
    pygame.draw.rect(screen, (0,49,82), (410,250,100,100)) #8

    if playerPosTut[1] <= 0:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:
        enter = False
        pMap6_3 = False
        pMap7 = True

def PuzzleMap7(screen):
    global smallx, bigx, smallY, bigY, pMap7, pMap7_1, pMap7_2, Page1, LightsOff, Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Exit, enter
    bigx = 555
    smallx = -90
    smallY = -50
    bigY = 250
    #if playerPosTut[1] == -60 and (playerPosTut[0] == 135 or playerPosTut[0] ==  150) and FacingUp == True:
     #   Page1 = True
    if playerPosTut[1] == -60 and (playerPosTut[0] == 285 or playerPosTut[0] ==  300) and FacingUp == True and enter == True:
        enter = False
        LightsOff = True
        pMap7_1 = True
        pMap7 = False
    if LightsOff == False:
        gamemap = pygame.image.load(r"Map\Puzzle1_Level2+.png")
        gamemap = pygame.transform.scale(gamemap, (700,400))
        screen.blit(gamemap, (0,0))
        pygame.draw.rect(screen, (0,49,82), (40,100,100,100)) #1 
        pygame.draw.rect(screen, (0,49,82), (560,100,100,100)) #3 -
        pygame.draw.rect(screen, (0,49,82), (190,100,100,100)) #6 
        pygame.draw.rect(screen, (0,49,82), (410,100,100,100)) #5 -
        pygame.draw.rect(screen, (0,49,82), (40,250,100,100)) #2 
        pygame.draw.rect(screen, (0,49,82), (560,250,100,100)) #4
        pygame.draw.rect(screen, (0,49,82), (190,250,100,100)) #7 -
        pygame.draw.rect(screen, (0,49,82), (410,250,100,100)) #8 -
        Buttons(screen)
        player(screen)
    if playerPosTut[0] >= -75 and playerPosTut[1] >= -65 and playerPosTut[0] <= 0 and playerPosTut[1] <= 10:
        Button1 = True
        player(screen)
    if playerPosTut[0] >= -75 and playerPosTut[1] >= 70 and playerPosTut[0] <= 0 and playerPosTut[1] <= 160:
        Button2 = True
        player(screen)
    if playerPosTut[0] >= 450 and playerPosTut[1] >= -65 and playerPosTut[0] <= 525 and playerPosTut[1] <= 10:
        Button3 = True
        player(screen)
    if playerPosTut[0] >= 450 and playerPosTut[1] >= 70 and playerPosTut[0] <= 525 and playerPosTut[1] <= 160:
        Button4 = True
        player(screen)
    if playerPosTut[0] >= 300 and playerPosTut[1] >= -60 and playerPosTut[0] <= 375 and playerPosTut[1] <= 15:
        Button5 = True
        player(screen)
    if playerPosTut[0] >= 75 and playerPosTut[1] >= -60 and playerPosTut[0] <= 165 and playerPosTut[1] <= 15:
        Button6 = True
        player(screen)
    if playerPosTut[0] >= 75 and playerPosTut[1] >= 70 and playerPosTut[0] <= 165 and playerPosTut[1] <= 160:
        Button7 = True
        player(screen)
    if playerPosTut[0] >= 300 and playerPosTut[1] >= 70 and playerPosTut[0] <= 375 and playerPosTut[1] <= 160:
        Button8 = True
        player(screen)
    if Button1 == False and Button2 == True and Button3 == False and Button4 == False and Button5 == True and Button6 == False and Button7 == True and Button8 == True:
        Exit = True
        player(screen)
    if playerPosTut[0] >= 180 and playerPosTut[0] <= 270 and playerPosTut[1] >= -20 and playerPosTut[1] <= 55 and Exit == True:
        playerPosTut[1] = -120
        enter = False
        LightsOff = False
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Button5 = False
        Button6 = False
        Button7 = False
        Button8 = False
        Exit = False
        pMap7_2 = True
        pMap7_1 = False
        pMap7 = False
        
def PuzzleMap7_1(screen):
    global smallx, bigx, smallY, bigY, pMap7, pMap7_1, Page1, LightsOff, Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Exit, enter
    gamemap1 = pygame.image.load(r"Map\Puzzle1_Level2+_1.png")
    gamemap1 = pygame.transform.scale(gamemap1, (700,400))
    screen.blit(gamemap1, (0,0))
    bigx = -100000
    smallx = 100000
    bigY = -1000000
    smallY = 10000000
    pygame.draw.rect(screen, (255,255,255), (40,250,100,100))#2
    pygame.draw.rect(screen, (255,255,255), (410,100,100,100))#5
    pygame.draw.rect(screen, (255,255,255), (190,250,100,100))#7
    pygame.draw.rect(screen, (255,255,255), (410,250,100,100))#8


    player(screen)
    
    if playerPosTut[1] == -60 and (playerPosTut[0] == 285 or playerPosTut[0] ==  300) and FacingUp == True and enter == True and LightsOff == True:
        enter = False
        LightsOff = False
        Button1 = False
        Button2 = False
        Button3 = False
        Button4 = False
        Button5 = False
        Button6 = False
        Button7 = False
        Button8 = False
        Exit = False
        pMap7 = True
        pMap7_1 = False
        
def PuzzleMap7_2(screen):
    global smallx, bigx, smallY, bigY, pMap7_2, WIP, enter
    smallx = 1000000
    bigx = -100000
    smallY = 10000000
    bigY = -10000000
    screen.fill((0,0,0))

    if playerPosTut[1] <= 300:
        playerPosTut[1] = playerPosTut[1] + 30
        player(screen)

    else:
        playerPosTut[1] = -210
        pMap7_2 = False
        WIP = True



def thanks(screen):
        screen.fill((0,0,0))
        Thanks = menuBttns.render("Thanks for playing", True, (255,0,0))
        Quit = menuBttns.render("Quit", True, (255,0,0))
        screen.blit(Quit, (315,260))
        screen.blit(Thanks, (215,300))
        pygame.display.update()
        if mouse[0] >= 230 and mouse[0] <= 470 and mouse[1] >= 244 and mouse[1] <= 321 and quit_game == False:
            Quit = menuBttns.render("Quit", True, (255,255,255))
            screen.blit(Quit, (315,260))
            pygame.display.update()
            if click[0] == 1:
                pygame.quit(); sys.exit()
            


def Buttons(screen):
    global Button1, Button2, Button3, Button4, Button5, Button6, Button7, Button8, Exit
    if Button1 == True:
        pygame.draw.rect(screen, (255,255,255), (40,100,100,100))
    if Button2 == True:
        pygame.draw.rect(screen, (255,255,255), (40,250,100,100))
    if Button3 == True:
        pygame.draw.rect(screen, (255,255,255), (560,100,100,100))
    if Button4 == True:
        pygame.draw.rect(screen, (255,255,255), (560,250,100,100))
    if Button5 == True:
        pygame.draw.rect(screen, (255,255,255), (410,100,100,100))
    if Button6 == True:
        pygame.draw.rect(screen, (255,255,255), (190,100,100,100))
    if Button7 == True:
        pygame.draw.rect(screen, (255,255,255), (190,250,100,100))
    if Button8 == True:
        pygame.draw.rect(screen, (255,255,255), (410,250,100,100)) 
    if Exit == True:
        pygame.draw.rect(screen, (0,0,0), (300,150,100,100))
        pygame.draw.rect(screen, (21,27,31), (325,200,50,50))
    
def instructions(screen):
        global enter, Page1, pMap5
        HelpTemp = []
        InstructText = []
    
        gamemap = pygame.image.load(r"Map\wall.png")
        gamemap = pygame.transform.scale(gamemap, (700,400))
        screen.blit(gamemap, (0,0))
        x = 0
        Help = open(r"Script\Help.txt","r")
        for line in Help:
            HelpTemp.append(line)
            x = x + 1

        for i in range(0,x):
            script_complete = False
            textArrayH = introTxt.render(HelpTemp[i], True, (0,0,0))
            InstructText.append(textArrayH)

        
        screen.blit(InstructText[0], (30, 100))
        screen.blit(InstructText[1], (30, 250))
        
        if playerPosTut[1] == -60 and (playerPosTut[0] == 135 or playerPosTut[0] ==  150) and FacingUp == True and enter == True and Page1 == True:
            enter = False
            Page1 = False
            pMap5 = True


    

def player(screen):
    global Player

    Player = pygame.transform.scale(Player, (250,250))
    screen.blit(Player, (playerPosTut[0],playerPosTut[1]))

def Pages():
    if Page1 == True:
        bigx = -10000
        smallx = 100000
        smallY = 10000
        bigY = -10000
        
        

            
    
def redrawWindow(surface):
    #surface.fill((0,0,0))
    
    if draw_menu == True:
        menu(surface)
        pygame.display.update()
    elif choice == "start game":
        startGame(surface)
        pygame.display.update()


def main():
    global Player, width, height, Page1, god_talking, devil_talking, clock, LightsOff, start_game, floatDown, h, open_settings, quit_game, draw_menu, enter, j, d, g, tutorialComplete,pMap1, play_game, TxCrd, tutMap1, rock, bigY, smallY, bigx, smallx
    width = 700
    height = 400
    screen = pygame.display.set_mode((width,height))
    clock = pygame.time.Clock()
    stage_one_incomplete = True
    draw_menu = True
    game_over = False
    start_game = False
    open_settings = False
    quit_game = False
    tutorialComplete = False
    play_game = False
    tutMap1 = True
    pMap1 = False
    rock = False
    floatDown = True
    Page1 = False
    LightsOff = False
    enter = True
    god_talking = False
    devil_talking = False
    bigx = 0
    smallx = 400
    bigY = 0
    smallY = 100000
    j = 0
    g = 1
    d = 0
    h = 0
    TxCrd = 30
    Player = pygame.image.load(r"Character\Main_Char_1.png")
    god()
    devil()
    char()

    while not game_over:
        pygame.time.delay(50)
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (quit_game == True and start_game == False and open_settings == False):
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    enter = not enter

                    



        fonts()
        textFloat(screen)
        talking(screen)
        tutorialText(screen)
        events()
        Pages()
        playerUpdate(screen)
        playerControl(screen)
        redrawWindow(screen)


    
main()

   
