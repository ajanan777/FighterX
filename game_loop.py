import pygame
from character import character
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
c1 = character(200,320, 1, 0, 0, 0, 0, 0, 0)
#,               speed_stat, damage_stat, attack_cooldown_stat, dodge_cooldown_stat, attack_length_stat, bot_buffer):					
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
c2 = character(900,320, 2, 10, 10, 10, 10, 10, 100)
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

	hp_bar(c1.hp, 10, 30)
	hp_bar(c2.hp, 770, 30)

	c1.display_victory_text_method(screen, victory_text, swidth, sheight)
	c2.display_victory_text_method(screen, victory_text, swidth, sheight)

	#move and displaying characters

	c1.movement_attributes_method(c2)
	c1.update_character(screen, c2)
	c1.display_character_method(screen, idle_img_c1, punch_img_c1, dodge_img_c1, arrow_img_c1, kick_img_c1, victory_img_c1, c2, dead_img_c1, string_img_c1)
 
	c2.movement_attributes_method(c1)
	c2.update_character(screen, c1)
	c2.display_character_method(screen, idle_img_c2, punch_img_c2, dodge_img_c2, arrow_img_c2, kick_img_c2, victory_img_c2, c1, dead_img_c2, string_img_c2)

	pygame.display.update()
	#quit
	for event in pygame.event.get():

		if event.type == pygame.QUIT:
			pygame.quit()
			game_loop = False