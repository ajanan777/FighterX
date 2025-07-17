import pygame
pygame.font.init()
pygame.mixer.init()

class character():
	

	def __init__(self, x, y, which_character, speed_stat, damage_stat, attack_cooldown_stat, dodge_cooldown_stat, attack_length_stat, bot_buffer):
		self.fall = 0 #is the character falling 1=yes 0=no
		self.currently_jumping = False #is the character in air
		self.jump_action = False #is the character pressing jump
		self.currently_attacking = False#is the character attacking
		self.attack_length = 0 #what is the attack length
		self.attack_cooldown = 0 #what is the attack cooldown
		self.attack_type = 0 #1=punch 2=up 3=down
		self.dodge_length = 0 #length of dodge
		self.dodge_cooldown = 0 #length of cooldown
		self.rect = pygame.Rect(x, y, 135, 290) #hitbox
		self.flipped = 0 #0=facing right 1=facing left
		self.hp = 100 #hp set to 100
		self.dead = False #is player alive
		self.which_character = which_character #1=character1 2=character2
		self.currently_dodging = False ##is the character dodging
		self.bot_buffer = bot_buffer #bot buffer value
		self.bot_buffer_amount = 0 #variable of bot buffer
		self.speed_stat = speed_stat
		self.damage_stat = damage_stat
		self.attack_cooldown_stat = attack_cooldown_stat
		self.dodge_cooldown_stat = dodge_cooldown_stat
		self.attack_length_stat = attack_length_stat
		self.hit = False #has player been hit
		self.end_game_buffer = 200
		self.start_buffer = 200 #inital cooldown set



	def alive(self): #function to see whether player is alive or not
		if self.hp <= 0:
			self.dead = True


	def display_victory_text_method(self, surface, image, width , height): #function to detect whether the victory text should display
		if self.dead == True:
			temp = pygame.transform.scale(image, (320,183))
			surface.blit(temp, ((width/2)-173,(height/2)-300))


	#display the character on the screen
	def display_character_method(self, surface, idle_img_which, punch1_img, dodge_img, arrow_img, kick_img, victory_img, enemy, dead_img, string_img):
		#pygame.draw.rect(surface, (255,255,0), self.rect)
		if self.dead == True:
			surface.blit(dead_img,(self.rect.x - 25, self.rect.y - 15))

		if enemy.dead == True:
			surface.blit(victory_img,(self.rect.x - 25, self.rect.y - 200))

		elif self.dodge_length != 0:
			if self.flipped == 0:
				surface.blit(dodge_img,(self.rect.x, self.rect.y))
			else:
				surface.blit(pygame.transform.flip(dodge_img, True, False), (self.rect.x, self.rect.y))

		elif self.currently_attacking == True and self.dead == False:
		#PUNCHING
			if self.attack_type == 1:
				if self.flipped == 0:
					surface.blit(punch1_img,(self.rect.x, self.rect.y))
				else:
					surface.blit(pygame.transform.flip(punch1_img, True, False), (self.rect.x - 84 - 100, self.rect.y))
		#ARROW ATTACK / UP ATTACK
			if self.attack_type == 2:
				if self.flipped == 0:
					surface.blit(arrow_img,(self.rect.x, self.rect.y - 60))
				else:
					surface.blit(pygame.transform.flip(arrow_img, True, False), (self.rect.x - 84 - 100, self.rect.y - 60))
		#KICK ATTACK / DOWN ATTACK
			if self.attack_type == 3:
				if self.flipped == 0:
					surface.blit(kick_img,(self.rect.x - 25, self.rect.y - 15))
				else:
					surface.blit(pygame.transform.flip(kick_img, True, False), (self.rect.x - 84 - 100 - 25, self.rect.y - 15))
		#string attack/type 4
			if self.attack_type == 4 or self.attack_type == 5:
				if self.flipped == 0:
					surface.blit(string_img,(self.rect.x, self.rect.y))
				else:
					surface.blit(pygame.transform.flip(string_img, True, False), (self.rect.x - 84 - 100, self.rect.y))


		elif self.flipped == 0 and self.dead == False:
				surface.blit(idle_img_which,(self.rect.x, self.rect.y))
		elif self.dead == False:
			surface.blit(pygame.transform.flip(idle_img_which, True, False), (self.rect.x, self.rect.y))







	def update_character(self, surface, enemy): #this handles all updates to a character, such as hp going down or cooldowns being ticked down and hitboxes being created
		self.alive()
		if self.dead == True and self.end_game_buffer !=0 :
			self.end_game_buffer = self.end_game_buffer - 1

		if self.start_buffer !=0:
			self.start_buffer = self.start_buffer - 1
			
		if self.dead == False:
			# print(self.attack_type)
			# print(self.attack_cooldown)
			attack_hitbox = pygame.Rect(self.rect.centerx - (0.7*self.rect.width*self.flipped), 0, 0, 0)
			if self.currently_attacking == True:
				if self.attack_length != 0:
					self.attack_length -= 1
					if self.attack_type == 1:
						attack_hitbox = pygame.Rect(self.rect.centerx - (1.35*self.rect.width*self.flipped), self.rect.centery - 105, 165, 40)
					elif self.attack_type == 2:
						attack_hitbox = pygame.Rect(self.rect.centerx - (0.7*self.rect.width*self.flipped), self.rect.centery - 210, 120, 60)
					elif self.attack_type == 3:
						attack_hitbox = pygame.Rect(self.rect.centerx - (0.7*self.rect.width*self.flipped), self.rect.centery + 150, 150, 60)
					elif self.attack_type == 4:
						attack_hitbox = pygame.Rect(self.rect.centerx - (1.35*self.rect.width*self.flipped), self.rect.centery - 50, 200, 40)


					#pygame.draw.rect(surface, (255,0,0), attack_hitbox)
					if attack_hitbox.colliderect(enemy.rect) and self.attack_length == (9 or 2 or 5) and enemy.dodge_length == 0:
						if self.attack_type == (4 or 5):
							self.attack_cooldown = 20
						enemy.hp = enemy.hp - (10+self.damage_stat)
						


				else:
					self.currently_attacking = False
			#cooldown between attack inputs
			if self.attack_cooldown != 0:
				if self.attack_cooldown != 0 and self.attack_type !=4:
					self.attack_cooldown -=1
				if self.attack_cooldown != 0 and self.attack_type == 4 :
					self.attack_cooldown -=0.5
				if self.attack_cooldown != 0 and self.attack_type == 5 :
					self.attack_cooldown -=0.5
				if self.attack_cooldown != 0.0 and self.attack_type == 5 :
					self.attack_cooldown -=0.5
			else: self.attack_cooldown = False

			#dodging
			if self.currently_dodging == True:
				if self.dodge_length !=0:
					self.dodge_length -=1


			#cooldown between dodge inputs
			if self.dodge_cooldown != 0:
				self.dodge_cooldown -=1
			else: 
				self.currently_dodging = False
#		else:
			# print(self.which_character, "dead")






	#how the player moves
	def movement_attributes_method(self, enemy): #this is where inputs for characters are taken
#PLAYER 1 CONTROLS
		self.alive()
		play_sound = False

		if self.dead == False and enemy.dead== False:
			if self.which_character == 1:
				step = 14 + self.speed_stat
				change_x = 0
				change_y = 0
				input = pygame.key.get_pressed()
				#controls
				if self.currently_attacking == False:
					if input[pygame.K_f] and self.dodge_length == 0 and self.currently_dodging == False:
						self.dodge_cooldown = 80 + self.dodge_cooldown_stat
						self.dodge_length = 20
						self.currently_dodging = True
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/dodge.wav'))



				if input[pygame.K_d]:
					if self.flipped == 1:
						self.flipped = 0
					change_x = step
				if input[pygame.K_a]:
					if self.flipped == 0:
						self.flipped = 1
					change_x = -step
				#y axis controls
				if input[pygame.K_SPACE] and self.currently_jumping == False:
					pygame.mixer.Sound.play(pygame.mixer.Sound('assets/jump.mp3'))
					self.fall = -60
					self.currently_jumping = True

				#attacking controls
				if self.currently_attacking == False and self.attack_cooldown == 0 and self.dodge_length == 0 and self.dead == False:
					if input[pygame.K_g]:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
						self.attack_type = 1
						self.attack_cooldown = 30 + self.attack_cooldown_stat
						self.attack_length = 10 + self.attack_length_stat
						self.currently_attacking = True
					if input[pygame.K_w]:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/arrow.wav'))
						self.attack_type = 2
						self.attack_cooldown = 40 + self.attack_cooldown_stat
						self.attack_length = 20 + self.attack_length_stat
						self.currently_attacking = True
					if input[pygame.K_s]:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
						self.attack_type = 3
						self.attack_cooldown = 40 + self.attack_cooldown_stat
						self.attack_length = 20 + self.attack_length_stat
						self.currently_attacking = True			

				elif self.currently_attacking == True and self.attack_cooldown !=0 and self.attack_length == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10) and self.dodge_length == 0 and self.dead == False and self.attack_type != 5:
					if input[pygame.K_g] and self.attack_type !=4:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
						self.attack_type = 4
						self.attack_cooldown = 30 + self.attack_cooldown_stat
						self.attack_length = 10 + self.attack_length_stat
						self.currently_attacking = True



















	#PLAYER 2 CONTROLS
			if self.which_character == 2:
				step = 14 + self.speed_stat
				change_x = 0
				change_y = 0
				input = pygame.key.get_pressed()
				#controls
				if self.currently_attacking == False:
					if input[pygame.K_u] and self.dodge_length == 0 and self.currently_dodging == False:
						self.dodge_cooldown = 80 + self.dodge_cooldown_stat
						self.dodge_length = 20
						self.currently_dodging = True
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/dodge.wav'))


				if input[pygame.K_RIGHT]:
					if self.flipped == 1:
						self.flipped = 0
					change_x = step
				if input[pygame.K_LEFT]:
					if self.flipped == 0:
						self.flipped = 1
					change_x = -step
				#y axis controls
				if input[pygame.K_p] and self.currently_jumping == False:
					pygame.mixer.Sound.play(pygame.mixer.Sound('assets/jump.mp3'))
					self.fall = -60
					self.currently_jumping = True
				#attacking controls
				if self.currently_attacking == False and self.attack_cooldown == 0 and self.dodge_length == 0:
					if input[pygame.K_i]:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
						self.attack_type = 1
						self.attack_cooldown = 30 + self.attack_cooldown_stat
						self.attack_length = 10 + self.attack_length_stat
						self.currently_attacking = True
					if input[pygame.K_UP]:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/arrow.wav'))
						self.attack_type = 2
						self.attack_cooldown = 40 + self.attack_cooldown_stat
						self.attack_length = 20 + self.attack_length_stat
						self.currently_attacking = True
					if input[pygame.K_DOWN]:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
						self.attack_type = 3
						self.attack_cooldown = 40 + self.attack_cooldown_stat
						self.attack_length = 20 + self.attack_length_stat
						self.currently_attacking = True


				elif self.currently_attacking == True and self.attack_cooldown !=0 and self.attack_length == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10) and self.dodge_length == 0 and self.dead == False and self.attack_type != 5:
					if input[pygame.K_i] and self.attack_type !=4:
						pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
						self.attack_type = 4
						self.attack_cooldown = 30 + self.attack_cooldown_stat
						self.attack_length = 10 + self.attack_length_stat
						self.currently_attacking = True



						

	#PLAYER 3 CONTROLS BOT
			if self.which_character == 3:
				step = 14 + self.speed_stat
				change_x = 0
				change_y = 0
				input = pygame.key.get_pressed()
				#controls
				if self.currently_attacking == False:
					if input[pygame.K_u] and self.dodge_length == 0 and self.currently_dodging == False:
						self.dodge_cooldown = 80 + self.dodge_cooldown_stat
						self.dodge_length = 20
						self.currently_dodging = True


				if enemy.rect.left > self.rect.right and self.currently_attacking == False:
					if self.flipped == 1:
						self.flipped = 0
					change_x = step
				if enemy.rect.right < self.rect.left and self.currently_attacking == False:
					if self.flipped == 0:
						self.flipped = 1
					change_x = -step
				#y axis controls
				if input[pygame.K_p] and self.currently_jumping == False:
					pygame.mixer.Sound.play(pygame.mixer.Sound('assets/jump.mp3'))
					self.fall = -60
					self.currently_jumping = True
				#attacking controls
				if self.bot_buffer_amount == 0:
					if self.currently_attacking == False and self.attack_cooldown == 0 and self.dodge_length == 0:
						if abs(enemy.rect.centerx - self.rect.centerx) <= 231 and enemy.rect.bottom == 610:
							pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
							self.attack_type = 1
							self.attack_cooldown = 0
							# self.attack_cooldown = 30 + self.attack_cooldown_stat
							self.attack_length = 10 + self.attack_length_stat
							self.currently_attacking = True
							self.bot_buffer_amount = self.bot_buffer
						if abs(enemy.rect.centerx - self.rect.centerx) <= 185 and enemy.rect.bottom != 610:
							pygame.mixer.Sound.play(pygame.mixer.Sound('assets/arrow.wav'))
							self.attack_type = 2
							self.attack_cooldown = 40 + self.attack_cooldown_stat
							self.attack_length = 20 + self.attack_length_stat
							self.currently_attacking = True
							self.bot_buffer_amount = self.bot_buffer
						if input[pygame.K_DOWN]:
							pygame.mixer.Sound.play(pygame.mixer.Sound('assets/attack.wav'))
							self.attack_type = 3
							self.attack_cooldown = 40 + self.attack_cooldown_stat
							self.attack_length = 20 + self.attack_length_stat
							self.currently_attacking = True
							self.bot_buffer_amount = self.bot_buffer
				else: self.bot_buffer_amount -= 1






			self.fall = self.fall +5
			change_y = change_y + self.fall






			#arena borders
			if self.rect.left < 14:
				if change_x == -14 - self.speed_stat:
					change_x = 14
			if self.rect.right > 1280:
				if change_x == 14 + self.speed_stat:
					change_x = -14

			if self.rect.bottom +change_y > 610:
				self.currently_jumping = False
				change_y = 610- self.rect.bottom

			#character moves
			self.rect.x = change_x + self.rect.x
			self.rect.y = change_y + self.rect.y
		# else:
		# 	print(self.which_character, "dead")	








	# def attack_method(self, surface):
	# 	# while self.attack_length != 0:
	# 	# 	attack_hitbox = pygame.Rect(self.rect.centerx, self.rect.centery - 60, 250, 40)
	# 	# 	pygame.draw.rect(surface, (255,0,0), attack_hitbox)
	# 	attack_hitbox = pygame.Rect(self.rect.centerx, self.rect.centery - 60, 250, 40)
	# 	pygame.draw.rect(surface, (255,0,0), attack_hitbox)



