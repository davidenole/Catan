import pygame

from colours import *
from variables import *
from option import *

''' GENERAL MENU '''

class Menu:

	def __init__(self):
		# build menu
		self.build = buildMenu()
		self.isOpen = False
		self.openedMenu = -1

	# check if point is in one of the menus
	def isIn(self, xy):
		if self.build.isIn(xy):
			return True
	
	# opens menus if mouse is in
	def open(self,xy):
		if self.build.isIn(xy) and self.build.isOpen == False:
			self.build.open()
			self.isOpen = True
			self.openedMenu = 0
	
	# closes menus if mouse is out
	def close(self,xy):
		if not self.build.isInOpen(xy) and self.build.isOpen == True:
			self.build.close()		
			self.isOpen = False
			self.openedMenu = -1

	# opens menu
	def justClose(self, n):
		if n == 0:
			self.build.close()
		self.isOpen = False
	
	# shuts menu down
	def justOpen(self, n):
		if n == 0:
			self.build.open()
		self.isOpen = True

	# checks if I want to do something
	def check(self,xy):
		for opt in self.build.opts:
			if opt.isIn(xy):
				self.justClose(0)
				return self.build.build( self.build.opts.index(opt) )
		return ''

	# draw menus on screen
	def draw(self, screen):
		self.build.draw(screen)

''' BUILDING MENU '''

class buildMenu:
	
	def __init__(self):
		# position
		self.ux, self.uy, self.dx, self.dy = 10,10,70,70
		self.isOpen = False
		# menu sprite
		self.mainSprite = pygame.image.load('./build.png')
		# options
		self.opts = []
		px = UINSIDE + DIMX/5
		py = UINSIDE + DIMY/5
		self.opts.append( Option((px,py), './build_road.png', ['c','w']) )
		px = UINSIDE + 2*DIMX/5
		py = UINSIDE + DIMY/5
		self.opts.append( Option((px,py), './build_village.png', ['g','c','w','s']) )
		px = UINSIDE + 3*DIMX/5
		py = UINSIDE + DIMY/5
		self.opts.append( Option((px,py), './build_city.png', ['g']*2+['r']*3) )
	
	# check if point is in the build menu
	def isIn(self, xy):
		return isIn(self.ux, self.uy, self.dx, self.dy, xy)
	
	# return if a click is inside the open menu board
	def isInOpen(self, xy):
		return isIn(UBORDER, UBORDER, UBORDER+DIMX+2*THICKNESS, UBORDER+DIMY+2*THICKNESS, xy)
	
	# opens the build menu
	def open(self):
		self.isOpen = True

	# opens the build menu
	def close(self):
		self.isOpen = False		
	
	# build something
	def build(self, n):
		self.close()
		# n = 0 road
		if n == 0:
			return 'road'
		elif n == 1:
			return 'settlement'
		else:
			return 'city'
	
	# draw print menu on screen
	def draw(self, screen):		
		if self.isOpen == False:
			screen.blit(self.mainSprite, (self.ux,self.uy))
		else:
			pygame.draw.rect(screen, BBUILDMENU, ((UBORDER,UBORDER),(DIMX+2*THICKNESS,DIMY+2*THICKNESS)) )
			pygame.draw.rect(screen, BUILDMENU, ((UINSIDE,UINSIDE),(DIMX,DIMY)) )
			for opt in self.opts:
				opt.draw(screen)
