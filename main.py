# import modules
import sys
import pygame as py
from pygame.locals import QUIT
from random import choice, random

# screen  variblres
screen_width = 600
screen_height = 400


# color constants
BGCOLOR = (7, 59, 76)
TEXTCOLOR = (255, 209, 107)
PLAYER1COLOR = (239, 71, 111)
PLAYER2COLOR = (6, 214, 160)
BALLCOLOR = (253, 240, 213)

# Player constants
PLAYER_HEIGHT = 50
PLAYER_WIDTH = 10
PLAYER_SPEED = 7

# player scores
player_1_score = 0
player_2_score = 0

#PLayer class
class Player:
	#initilaize Player object
	# x {int} - x coordinate of Player
	# y {int} - y coordinate of Player
	# color {rgb tuple} - color of the Player in rgb
	# return {none}
	def __init__(self, x, y, color) -> None:
		
		self.x = x
		self.y = y
		self.width = PLAYER_WIDTH
		self.height = PLAYER_HEIGHT
		self.color = color
		self.speed = PLAYER_SPEED
		self.is_moving = False
		self.direction = None
	
	#draw the player object
	def draw(self):
		leftx = self.x - self.width /2
		topy = self.y - self.height /2
		coords = py.Rect(leftx, topy, self.width, self.height)
		py.draw.rect(DISPLAYSURF, self.color, coords, 0)

	#move the player object
	def move(self):
		if not self.is_moving:
			return

		if self.direction == "UP" and self.y > 0:
			self.y -= self.speed
		elif self.direction == "DOWN" and self.y < screen_height:
			self.y += self.speed

#ball clas
class Ball:
	#initilaize Player object
	# r {int} - radius of ball object
	# y {int} - y coordinate of Player
	# color {rgb tuple} - color of the Ball in rgb
	# speed {int} - speed of the Ball object
	def __init__(self, r, color, speed):
		self.r = r
		self.color = color
		self.speed = speed
		self.reset()

	# draws the Ball object
	def draw(self):
		py.draw.circle(DISPLAYSURF, self.color, (self.x, self.y), self.r)

	# moves the ball object
	def move(self):
		self.x += self.speedx
		self.y += self.speedy


		#check for collisions with 
		if self.y - self.r < 0 or self.y - self.r >screen_height:
			self.speedy*= -1

		
		if self.x - self.r < 0:
			if collide(player_l, self):
				self.speedx = -self.speedx
			else:
				self.reset()
				global player_2_score
				player_2_score += 1
		elif self.x + self.r > screen_width:
			if collide(player_r, self):
				self.speedx = -self.speedx
			else:
				self.reset()
				global player_1_score
				player_1_score += 1


	def reset(self):
		self.speedx = choice(range(self.speed // 2, self.speed))
		self.speedy = choice(range(self.speed // 2, self.speed))

		if random() > 0.5:
			self.speedx *= -1
		if random()	>	0.5:
			self.speedy *= -1
		self.x = screen_width // 2
		self.y = screen_height // 2


def collide(player, ball):
	if abs(ball.y - player.y) < player.height / 2 + ball.r:
		return True
	else:
		return False

def show_score():
	text = FONT.render(str(player_1_score) + " : " + str(player_2_score), 1, TEXTCOLOR)
	textpos = text.get_rect()
	textpos.centerx = screen_width / 2
	textpos.centery = 15
	return text, textpos

py.init()
DISPLAYSURF = py.display.set_mode((screen_width, screen_height))
py.display.set_caption("Pong")
clock = py.time.Clock()
FPS = 60
FONT = py.font.Font(None, 40)

player_r = Player(screen_width - PLAYER_WIDTH / 2, screen_height - PLAYER_HEIGHT / 2, PLAYER1COLOR)
player_l = Player ( 0 + PLAYER_WIDTH / 2, screen_height - PLAYER_HEIGHT / 2, PLAYER2COLOR)

ball = Ball(7, BALLCOLOR, 4)




while True:
	DISPLAYSURF.fill(BGCOLOR)
	
	player_r.draw()
	player_r.move()

	player_l.draw()
	player_l.move()

	ball.draw()
	ball.move()

	text, position = show_score()
	DISPLAYSURF.blit(text, position)


	# events proccesing
	for event in py.event.get():
		if event.type == QUIT:
			py.quit()
			sys.exit()
		elif event.type == py.KEYDOWN:
			if event.key == py.K_UP:
				player_r.is_moving = True
				player_r.direction = "UP"
			elif event.key == py.K_DOWN:
				player_r.is_moving = True
				player_r.direction = "DOWN"
			elif event.key == py.K_w:
				player_l.is_moving = True
				player_l.direction = "UP"
			elif event.key == py.K_s:
				player_l.is_moving = True
				player_l.direction = "DOWN"
		elif event.type == py.KEYUP:
			if event.key == py.K_UP:
				player_r.is_moving = False
			elif event.key == py.K_DOWN:
				player_r.is_moving = False
			elif event.key == py.K_w:
				player_l.is_moving = False
			elif event.key == py.K_s:
				player_l.is_moving = False
				
	py.display.update()
	clock.tick(FPS)