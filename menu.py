import pygame, sys
from button import Button
from character import character

#initate pygame
pygame.init()

#setup the screen
screen_menus = pygame.display.set_mode((1280, 720))

#add title in the window bar
pygame.display.set_caption("FIGHTER X")
#load background of the menu
background = pygame.image.load("assets/Background.png")
p1select = pygame.image.load("assets/p1selecting.png")
p1selectingmap = pygame.image.load("assets/P1selecting_map.png")
p2select = pygame.image.load("assets/P2selecting.png")
bg_default = pygame.image.load("assets/Bg1.png")
bg_vibrant = pygame.image.load("assets/background3.png")
bg_dark = pygame.image.load("assets/background2.png")



#main menu screen
def main_menu():
    #main menu loop/cycle
    while True:
        #every menu cycle the background gets displayed
        screen_menus.blit(background, (0, 0))
        #the current mouse position is always stored
        mouse_pos = pygame.mouse.get_pos()
                        
        #get the font then render the font, then blit the text on the screen           
        fighterx_text = pygame.font.Font("assets/font.ttf", 100).render("FIGHTER X", True, "White")
        screen_menus.blit(fighterx_text, (420,70))

        #create  the button instances
        b_play = Button(pygame.image.load("assets/play.png"), (640, 280), "PLAY", pygame.font.Font("assets/font.ttf", 65), "White", "#96FFB3")
        b_practice = Button(pygame.image.load("assets/practice.png"), (640, 420), "PRACTICE", pygame.font.Font("assets/font.ttf", 65), "White", "#96FFB3")
        b_quit = Button(pygame.image.load("assets/quit.png"), (640, 560), "QUIT", pygame.font.Font("assets/font.ttf", 65), "White", "#FF7777")



        #display buttons
        b_play.changeColor(mouse_pos)
        b_play.update(screen_menus)
       
        b_practice.changeColor(mouse_pos)
        b_practice.update(screen_menus)
     
        b_quit.changeColor(mouse_pos)
        b_quit.update(screen_menus)

        



        #pygame event updates
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_play.checkForInput(mouse_pos):
                    character_selection()
                if b_practice.checkForInput(mouse_pos):
                    practice()
                if b_quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()











#character selection 
def character_selection():
    selection1 = 0 #variable for player1's selections
    selection2 = 0 #variable for player2's selections

    #global variables are created and then used during the in game state, where the stats are set
    global speed1 #speed stat
    speed1 = 0
    global damage1 #damage stat
    damage1 = 0
    global attack_cooldown1 #attack cooldown stats
    attack_cooldown1 = 0
    global dodge_cooldown1 #dodge cooldown stat
    dodge_cooldown1 = 0
    global attack_length1 #length of attack stat
    attack_length1 = 0
    global bot_buffer1 #length of bot buffer(not needed for real players)
    bot_buffer1 = 0


    #stats for player 2
    global speed2  
    speed2 = 0
    global damage2
    damage2 = 0
    global attack_cooldown2
    attack_cooldown2 = 0
    global dodge_cooldown2
    dodge_cooldown2 = 0
    global attack_length2
    attack_length2 = 0
    global bot_buffer2
    bot_buffer2 = 0



    while True:
        #every menu cycle the background gets displayed
        screen_menus.blit(background, (0, 0))
        #the current mouse position is always stored
        mouse_pos = pygame.mouse.get_pos()

        #displaying which player should select
        player1_select = pygame.font.Font("assets/font.ttf", 100).render("PLAYER 1 SELECT", True, "White")
        player2_select = pygame.font.Font("assets/font.ttf", 100).render("PLAYER 2 SELECT", True, "White")
        #if player 1 hasnt selected, player 1 selection text is displayed
        if selection1 == 0:
            screen_menus.blit(player1_select, (295,70))
        else:
            screen_menus.blit(player2_select, (295,70))

        #setting the buttons
        b_back = Button(None, (1179, 683), "BACK", pygame.font.Font("assets/font.ttf", 50), "White", "Green")
        reselectbutton = Button(None, (639, 555), "re select", pygame.font.Font("assets/font.ttf", 40), "White", "Green")
        lockinbutton = Button(None, (632, 637), "LOCK IN", pygame.font.Font("assets/font.ttf", 60), "White", "Green") 


        #setting character buttons and images
        c1 = Button(pygame.image.load("assets/character1.png"), (310, 360), "x", pygame.font.Font("assets/font.ttf", 100), "White", "#96FFB3")
        c2 = Button(pygame.image.load("assets/character2.png"), (640, 360), "x", pygame.font.Font("assets/font.ttf", 100), "White", "#96FFB3")
        c3 = Button(pygame.image.load("assets/character3.png"), (970, 360), "x", pygame.font.Font("assets/font.ttf", 100), "White", "#96FFB3")
        #display buttons
        c1.changeColor(mouse_pos)
        c1.update(screen_menus)
        c2.changeColor(mouse_pos)
        c2.update(screen_menus)
        c3.changeColor(mouse_pos)
        c3.update(screen_menus)
        reselectbutton.changeColor(mouse_pos)
        reselectbutton.update(screen_menus)
        b_back.changeColor(mouse_pos)
        b_back.update(screen_menus)
        lockinbutton.changeColor(mouse_pos)
        lockinbutton.update(screen_menus)

        #depending what player 1/2 selects, the border of selection appears for the players
        if selection1==1:
            screen_menus.blit(p1select,(122, 135))
        elif selection1==2:
            screen_menus.blit(p1select,(452, 135))
        elif selection1==3:
            screen_menus.blit(p1select,(782, 135))
            
        if selection2==1:
            screen_menus.blit(p2select,(122, 135))
        elif selection2==2:
            screen_menus.blit(p2select,(452, 135))
        elif selection2==3:
            screen_menus.blit(p2select,(782, 135))


        #stats for each type of character
        if selection1 == 1: #damage character
            speed1 = 1                  #base:14 ,increase value increases speed
            damage1 = 4                 #base:10 ,increase value increases damage dealt
            attack_cooldown1 = 12       #base:30/40 ,increase value increases length of cooldown
            dodge_cooldown1 = 12        #base:80 ,increase value increases cooldown between dodges
            attack_length1 = 10         #base:10/20 ,increase value increases length of attack
            bot_buffer1 = 0             #base:0 ,increase value increases the time frame where the bot won't attack you


        if selection1 == 2: #balanced character
            speed1 = 5
            damage1 = 0
            attack_cooldown1 = 5
            dodge_cooldown1 = 4
            attack_length1 = 3
            bot_buffer1 = 0
 
        if selection1 == 3: #speed character
            speed1 = 8
            damage1 = -5
            attack_cooldown1 = 6
            dodge_cooldown1 = 7
            attack_length1 = 5
            bot_buffer1 = 0







        if selection2 ==1:
            speed2 = 0
            damage2 = 5
            attack_cooldown2 = 15
            dodge_cooldown2 = 15
            attack_length2 = 10
            bot_buffer2 = 0

        if selection2 ==2:
            speed2 = 5
            damage2 = 0
            attack_cooldown2 = 10
            dodge_cooldown2 = 0
            attack_length2 = 5
            bot_buffer2 = 0

        if selection2 ==3:
            speed2 = 10
            damage2 = -5
            attack_cooldown2 = 10
            dodge_cooldown2 = 5
            attack_length2 = 0
            bot_buffer2 = 0




            #checks inputs for each button, if player 1 hasn't selected then it takes the selection first
            #else player 2 selection is made
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reselectbutton.checkForInput(mouse_pos):
                    selection1 = 0
                    selection2 = 0
                if c1.checkForInput(mouse_pos):
                    if selection1 == 0:
                        selection1 = 1
                    elif selection2 == 0:
                        selection2 = 1
                if c2.checkForInput(mouse_pos):
                    if selection1 == 0:
                        selection1 = 2
                    elif selection2 == 0:
                        selection2 = 2
                if c3.checkForInput(mouse_pos):
                    if selection1 == 0:
                        selection1 = 3
                    elif selection2 == 0:
                        selection2 = 3
                if lockinbutton.checkForInput(mouse_pos):
                    if selection1 !=0 and selection2!=0:
                        map_selection()
                if b_back.checkForInput(mouse_pos):
                    main_menu()
                # print(selection1, selection2)

        pygame.display.update()

def map_selection(): #selecting the map
    selection = 0
    global which_bg
    which_bg = 0


    while True:
        #print(which_bg)
        #every menu cycle the background gets displayed
        screen_menus.blit(background, (0, 0))
        #the current mouse position is always stored
        mouse_pos = pygame.mouse.get_pos()


        map_select = pygame.font.Font("assets/font.ttf", 100).render("SELECT A MAP", True, "White")
        screen_menus.blit(map_select, (325,70))


        b_back = Button(None, (1179, 683), "BACK", pygame.font.Font("assets/font.ttf", 50), "White", "Green")
        reselectbutton = Button(None, (639, 555), "re select", pygame.font.Font("assets/font.ttf", 40), "White", "Green")
        lockinbutton = Button(None, (632, 637), "LOCK IN", pygame.font.Font("assets/font.ttf", 60), "White", "Green") 



        m1 = Button(pygame.image.load("assets/m1.png"), (310, 360), "x", pygame.font.Font("assets/font.ttf", 110), "White", "#96FFB3")
        m2 = Button(pygame.image.load("assets/m2.png"), (640, 360), "x", pygame.font.Font("assets/font.ttf", 110), "White", "#96FFB3")
        m3 = Button(pygame.image.load("assets/m3.png"), (970, 360), "x", pygame.font.Font("assets/font.ttf", 110), "White", "#96FFB3")
        #display buttons
        m1.changeColor(mouse_pos)
        m1.update(screen_menus)
        m2.changeColor(mouse_pos)
        m2.update(screen_menus)
        m3.changeColor(mouse_pos)
        m3.update(screen_menus)
        reselectbutton.changeColor(mouse_pos)
        reselectbutton.update(screen_menus)
        b_back.changeColor(mouse_pos)
        b_back.update(screen_menus)
        lockinbutton.changeColor(mouse_pos)
        lockinbutton.update(screen_menus)

        if selection==1:
            screen_menus.blit(p1selectingmap,(-190,-140))
        elif selection==2:
            screen_menus.blit(p1selectingmap,(140,-140))
        elif selection==3:
            screen_menus.blit(p1selectingmap,(470,-140))




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reselectbutton.checkForInput(mouse_pos):
                    selection = 0
                if m1.checkForInput(mouse_pos):
                    if selection == 0:
                        selection = 1
                        which_bg = 1
                if m2.checkForInput(mouse_pos):
                    if selection == 0:
                        selection = 2
                        which_bg = 2
                if m3.checkForInput(mouse_pos):
                    if selection == 0:
                        selection = 3
                        which_bg = 3
                if lockinbutton.checkForInput(mouse_pos) and selection != 0:
                    game_loop_state()
                if b_back.checkForInput(mouse_pos):
                    main_menu()
                # print(selection)

        pygame.display.update()    


def practice(): # bot difficulty selection
    difficulty_selection = 0
    global bot_speed
    bot_speed = 0
    global bot_damage
    bot_damage = 0
    global bot_attack_cooldown
    bot_attack_cooldown = 0
    global bot_dodge_cooldown
    bot_dodge_cooldown = 0
    global bot_attack_length
    bot_attack_length = 0
    global bot_bot_buffer
    bot_bot_buffer = 0

    while True:
        #every menu cycle the background gets displayed
        screen_menus.blit(background, (0, 0))
        #the current mouse position is always stored
        mouse_pos = pygame.mouse.get_pos()


        map_select = pygame.font.Font("assets/font.ttf", 100).render("SELECT   A    DIFFICULTY", True, "White")
        screen_menus.blit(map_select, (190,70))


        b_back = Button(None, (1179, 683), "BACK", pygame.font.Font("assets/font.ttf", 50), "White", "Green")
        reselectbutton = Button(None, (639, 555), "re select", pygame.font.Font("assets/font.ttf", 40), "White", "Green")
        lockinbutton = Button(None, (632, 637), "LOCK IN", pygame.font.Font("assets/font.ttf", 60), "White", "Green") 



        d1 = Button(pygame.image.load("assets/character1e.png"), (310, 360), "easy", pygame.font.Font("assets/font.ttf", 40), "Black", "#96FFB3")
        d2 = Button(pygame.image.load("assets/character1e.png"), (640, 360), "medium", pygame.font.Font("assets/font.ttf", 30), "Black", "#96FFB3")
        d3 = Button(pygame.image.load("assets/character1e.png"), (970, 360), "hard", pygame.font.Font("assets/font.ttf", 40), "Black", "#96FFB3")
        #display buttons
        d1.changeColor(mouse_pos)
        d1.update(screen_menus)
        d2.changeColor(mouse_pos)
        d2.update(screen_menus)
        d3.changeColor(mouse_pos)
        d3.update(screen_menus)
        reselectbutton.changeColor(mouse_pos)
        reselectbutton.update(screen_menus)
        b_back.changeColor(mouse_pos)
        b_back.update(screen_menus)
        lockinbutton.changeColor(mouse_pos)
        lockinbutton.update(screen_menus)

        if difficulty_selection==1:
            screen_menus.blit(p1selectingmap,(-190,-140))
            bot_speed = -12                 #base:14 ,increase value increases speed
            bot_damage = -9                 #base:10 ,increase value increases damage dealt
            bot_attack_cooldown = 100       #base:30/40 ,increase value increases length of cooldown
            bot_dodge_cooldown = 100        #base:80 ,increase value increases cooldown between dodges
            bot_attack_length = 200         #base:10/20 ,increase value increases length of attack
            bot_bot_buffer = 300            #base:0 ,increase value increases the time frame where the bot won't attack you


        elif difficulty_selection==2:
            screen_menus.blit(p1selectingmap,(140,-140))
            bot_speed = 0
            bot_damage = 0
            bot_attack_cooldown = 0
            bot_dodge_cooldown = 0
            bot_attack_length = 0
            bot_bot_buffer = 100



        elif difficulty_selection==3:
            screen_menus.blit(p1selectingmap,(470,-140))
            bot_speed = 30
            bot_damage = 20
            bot_attack_cooldown = 10
            bot_dodge_cooldown = 10
            bot_attack_length = 20
            bot_bot_buffer = 0





        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if reselectbutton.checkForInput(mouse_pos):
                    difficulty_selection = 0
                if d1.checkForInput(mouse_pos):
                    if difficulty_selection == 0:
                        difficulty_selection = 1
                if d2.checkForInput(mouse_pos):
                    if difficulty_selection == 0:
                        difficulty_selection = 2
                if d3.checkForInput(mouse_pos):
                    if difficulty_selection == 0:
                        difficulty_selection = 3
                if lockinbutton.checkForInput(mouse_pos):
                    bot_fight()
                if b_back.checkForInput(mouse_pos):
                    main_menu()
                # print(difficulty_selection)

        pygame.display.update()    





#GAME LOOP INTEGRATION
def game_loop_state():

    pygame.font.init() # sound initation
    pygame.mixer.init()# sound initation
    attack = pygame.mixer.Sound('assets/attack.wav') # setting the attack sound

    pygame.init() #initating pygame

    clock = pygame.time.Clock() #setting the clock variable
    swidth = 1280 # screen width
    sheight = 720 #screen height
    screen = pygame.display.set_mode((swidth, sheight)) #setting the screen
    background1 = pygame.image.load("assets/bg1.png").convert_alpha() #loading the background
    victory_text = pygame.image.load("assets/victorytext.png") #loading the victory text


    #characters loading
    c1 = character(200,320, 1, speed1, damage1, attack_cooldown1, dodge_cooldown1, attack_length1, 0) #loading the character,
    #this takes global variable arguments such as speed, damage... these are set in the character selection state and are
    # variable depending on the selected character

    idle_img_c1 = pygame.image.load("assets/idle1_c1.png") #loading idle image
    punch_img_c1 = pygame.image.load("assets/punch1_c1.png")#loading punch image
    dodge_img_c1 = pygame.image.load("assets/dodge_c1.png")#loading dodge image
    arrow_img_c1 = pygame.image.load("assets/arrow_c1.png")#loading arrow image
    kick_img_c1 = pygame.image.load("assets/kick_c1.png")#loading kick image
    victory_img_c1 = pygame.image.load("assets/victory_c1.png")#loading victory pose image
    dead_img_c1 = pygame.image.load("assets/dead_c1.png")#loading death image
    string_img_c1 = pygame.image.load("assets/string_c1.png")#loading string attack image

    c2 = character(900,320, 2, speed2, damage2, attack_cooldown2, dodge_cooldown2, attack_length2, 0) #same as before but loads character2
    idle_img_c2 = pygame.image.load("assets/idle1_c2.png")
    punch_img_c2 = pygame.image.load("assets/punch1_c2.png")
    dodge_img_c2 = pygame.image.load("assets/dodge_c2.png")
    arrow_img_c2 = pygame.image.load("assets/arrow_c2.png")
    kick_img_c2 = pygame.image.load("assets/kick_c2.png")
    victory_img_c2 = pygame.image.load("assets/victory_c2.png")
    dead_img_c2 = pygame.image.load("assets/dead_c2.png")
    string_img_c2 = pygame.image.load("assets/string_c2.png")


    def hp_bar(hp, x, y): #drawing of the hp bar function
        pygame.draw.rect(screen, "Red", (x , y, 500, 50))
        pygame.draw.rect(screen, "Green", (x , y, 500* (hp/100), 50))


    game_loop = True # game loop is set to true so the game loop can occur
    while game_loop:

        clock.tick(60) #clock is set to 60fps

        #load bg
        if which_bg == 1: #loads the background depending what the which_bg global variable is set to 
            screen.blit(background1,(0,0)) #displaying the background on the screen
        elif which_bg == 2:
            screen.blit(bg_dark,(0,0))
        else:
            screen.blit(bg_vibrant,(0,0))

        hp_bar(c1.hp, 10, 30) #drawing the hp bar for player 1
        hp_bar(c2.hp, 770, 30)#drawing the hp bar for player 2

        if c1.end_game_buffer == 0: #if the end game buffer is complete then the end game state occurs, the buffer
                                    #is set to 200 so after a player dies the game pauses for 200 cycles and then
                                    #switches game states
            end_game(2) #this takes the argument of which player has died(in this case it is player 2)
        if c2.end_game_buffer == 0:
            end_game(1)


        c1.display_victory_text_method(screen, victory_text, swidth, sheight)#This displays the victory text
        c2.display_victory_text_method(screen, victory_text, swidth, sheight)

        #move and displaying characters

        c1.movement_attributes_method(c2) #this updates all the movements of the character
        c1.update_character(screen, c2) #this calculates all the updates of the charcter, such as health going down
        c1.display_character_method(screen, idle_img_c1, punch_img_c1, dodge_img_c1, arrow_img_c1, kick_img_c1, victory_img_c1, c2, dead_img_c1, string_img_c1)
        #this displays the images, it takes in all the types of images for player 1


        c2.movement_attributes_method(c1)#repeated code but for player 2
        c2.update_character(screen, c1)
        c2.display_character_method(screen, idle_img_c2, punch_img_c2, dodge_img_c2, arrow_img_c2, kick_img_c2, victory_img_c2, c1, dead_img_c2, string_img_c2)

        pygame.display.update() #updates the screen
        #quit
        for event in pygame.event.get(): # if a player presses the quit button the game ends

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                game_loop = False






#bot fight integration
def bot_fight():
    pygame.font.init()
    pygame.mixer.init()
    attack = pygame.mixer.Sound('assets/attack.wav')

    pygame.init()

    clock = pygame.time.Clock()
    swidth = 1280
    sheight = 720
    screen = pygame.display.set_mode((swidth, sheight))
    background1 = pygame.image.load("assets/bg1.png").convert_alpha()
    victory_text = pygame.image.load("assets/victorytext.png")


    #characters loading
    c1 = character(200,320, 1, 5, 0, 10, 0, 5, 0)
    # c1 = character(200,320, 1, 10, 10, 10, 10, 10)
    idle_img_c1 = pygame.image.load("assets/idle1_c1.png")
    punch_img_c1 = pygame.image.load("assets/punch1_c1.png")
    dodge_img_c1 = pygame.image.load("assets/dodge_c1.png")
    arrow_img_c1 = pygame.image.load("assets/arrow_c1.png")
    kick_img_c1 = pygame.image.load("assets/kick_c1.png")
    victory_img_c1 = pygame.image.load("assets/victory_c1.png")
    dead_img_c1 = pygame.image.load("assets/dead_c1.png")
    string_img_c1 = pygame.image.load("assets/string_c1.png")

    #c2 = character(920,320, 2, 100, 100, 100, 100, 100)
    c2 = character(900,320, 3, bot_speed, bot_damage, bot_attack_cooldown, bot_dodge_cooldown, bot_attack_length, bot_bot_buffer)


    idle_img_c2 = pygame.image.load("assets/idle1_c2.png")
    punch_img_c2 = pygame.image.load("assets/punch1_c2.png")
    dodge_img_c2 = pygame.image.load("assets/dodge_c2.png")
    arrow_img_c2 = pygame.image.load("assets/arrow_c2.png")
    kick_img_c2 = pygame.image.load("assets/kick_c2.png")
    victory_img_c2 = pygame.image.load("assets/victory_c2.png")
    dead_img_c2 = pygame.image.load("assets/dead_c2.png")
    string_img_c2 = pygame.image.load("assets/string_c2.png")


    def hp_bar(hp, x, y):
        pygame.draw.rect(screen, "Red", (x , y, 500, 50))
        pygame.draw.rect(screen, "Green", (x , y, 500* (hp/100), 50))


    game_loop = True
    while game_loop:


        clock.tick(60)

        #load bg
        screen.blit(background1,(0,0))
        screen.blit(background1,(0,0))

        if c1.end_game_buffer == 0:                         #END GAME BUFFER COMPLETE SO THIS WHERE TO SENF TO END GAME STATE.
            end_game_bot_fight()
        if c2.end_game_buffer == 0:
            end_game_bot_fight()




        hp_bar(c1.hp, 10, 30)
        hp_bar(c2.hp, 770, 30)

        c1.display_victory_text_method(screen, victory_text, swidth, sheight)
        c2.display_victory_text_method(screen, victory_text, swidth, sheight)

        #move and displaying characters
        if c1.start_buffer ==0 and c2.start_buffer ==0:

            c1.movement_attributes_method(c2)
            c2.movement_attributes_method(c1)
        elif c1.start_buffer > 150 :
            screen_menus.blit(pygame.font.Font("assets/font.ttf", 100).render("READY", True, "Black"), (530,90))
        elif c1.start_buffer < 150 and c1.start_buffer > 50 :
            screen_menus.blit(pygame.font.Font("assets/font.ttf", 100).render("SET", True, "Black"), (530,90))
        elif c1.start_buffer < 50 and c1.start_buffer > 0 :
            screen_menus.blit(pygame.font.Font("assets/font.ttf", 100).render("FIGHT", True, "Red"), (530,90))


        c1.update_character(screen, c2)
        c1.display_character_method(screen, idle_img_c1, punch_img_c1, dodge_img_c1, arrow_img_c1, kick_img_c1, victory_img_c1, c2, dead_img_c1, string_img_c1)
     
        c2.update_character(screen, c1)
        c2.display_character_method(screen, idle_img_c2, punch_img_c2, dodge_img_c2, arrow_img_c2, kick_img_c2, victory_img_c2, c1, dead_img_c2, string_img_c2)

        pygame.display.update()
        #quit
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                game_loop = False




def end_game(winner):
    #main menu loop/cycle
    while True:
        #every menu cycle the background gets displayed
        screen_menus.blit(background, (0, 0))
        #the current mouse position is always stored
        mouse_pos = pygame.mouse.get_pos()
                        
        #get the font then render the font, then blit the text on the screen  
        if winner == 1:
            fighterx_text = pygame.font.Font("assets/font.ttf", 100).render("PLAYER 1 WINS", True, "White")
        else:
            fighterx_text = pygame.font.Font("assets/font.ttf", 100).render("PLAYER 2 WINS", True, "White")

        screen_menus.blit(fighterx_text, (320,70))


        b_play = Button(pygame.image.load("assets/play.png"), (640, 280), "MAIN MENU", pygame.font.Font("assets/font.ttf", 65), "White", "#96FFB3")
        b_practice = Button(pygame.image.load("assets/practice.png"), (640, 420), "REMATCH", pygame.font.Font("assets/font.ttf", 65), "White", "#96FFB3")
        b_quit = Button(pygame.image.load("assets/quit.png"), (640, 560), "QUIT", pygame.font.Font("assets/font.ttf", 65), "White", "#FF7777")



        #display buttons
        b_play.changeColor(mouse_pos)
        b_play.update(screen_menus)
       
        b_practice.changeColor(mouse_pos)
        b_practice.update(screen_menus)
     
        b_quit.changeColor(mouse_pos)
        b_quit.update(screen_menus)

        




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_play.checkForInput(mouse_pos):
                    main_menu()
                if b_practice.checkForInput(mouse_pos):
                    character_selection()
                if b_quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def end_game_bot_fight():
    #main menu loop/cycle
    while True:
        #every menu cycle the background gets displayed
        screen_menus.blit(background, (0, 0))
        #the current mouse position is always stored
        mouse_pos = pygame.mouse.get_pos()
                        
        #get the font then render the font, then blit the text on the screen  



        b_play = Button(pygame.image.load("assets/play.png"), (640, 280), "MAIN MENU", pygame.font.Font("assets/font.ttf", 65), "White", "#96FFB3")
        b_practice = Button(pygame.image.load("assets/practice.png"), (640, 420), "REMATCH", pygame.font.Font("assets/font.ttf", 65), "White", "#96FFB3")
        b_quit = Button(pygame.image.load("assets/quit.png"), (640, 560), "QUIT", pygame.font.Font("assets/font.ttf", 65), "White", "#FF7777")



        #display buttons
        b_play.changeColor(mouse_pos)
        b_play.update(screen_menus)
       
        b_practice.changeColor(mouse_pos)
        b_practice.update(screen_menus)
     
        b_quit.changeColor(mouse_pos)
        b_quit.update(screen_menus)

        




        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_play.checkForInput(mouse_pos):
                    main_menu()
                if b_practice.checkForInput(mouse_pos):
                    practice()
                if b_quit.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()



main_menu()











































































