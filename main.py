import pygame
import sys
pygame.init()

display = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

class Player:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
	def main(self, display):
		pygame.draw.rect(display, "white", (self.x, self.y, self.width, self.height))


player = Player(400, 300, 32, 32)
vel = 10


while True:
	display.fill("grey")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.QUIT

	player.main(display)
	keys = pygame.key.get_pressed() 
	if keys[pygame.K_a] and player.x>0:
		player.x -= vel
	if keys[pygame.K_d] and player.x<800-player.width:
		player.x += vel
	if keys[pygame.K_w] and player.y>0:
		player.y -= vel
	if keys[pygame.K_s] and player.y<600-player.height:
		player.y += vel


	clock.tick(60)
	pygame.display.update()