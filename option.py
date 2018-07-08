import pygame

from colours import *
from variables import *

# all sprites count as 60x60
S = 60

class Option:

	def __init__(self, pos, sprite, cost=[]):
		# position
		self.pos = pos
		self.x = pos[0]
		self.y = pos[1]
		self.cost = cost
		self.sprite = pygame.image.load(sprite)

	def isIn(self, xy):
		return isIn(self.x, self.y, self.x+S, self.y+S, xy)
	
	def draw(self, screen):
		screen.blit(self.sprite, (self.x,self.y))
		n = len(self.cost)
		if n>0:
			h = S/(n+1)
			x0 = self.x + h
			for c in self.cost:
				pygame.draw.circle(screen, resCols[c], (x0,self.y+S+10), 5)
				x0 += h
