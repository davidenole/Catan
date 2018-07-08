# maze generator from 
#  https://rosettacode.org/wiki/Maze_generation#Python

import pygame

from random import shuffle, randrange, randint

from colours import * 
from variables import * 
from tile import * 
from board import *
from menu import * 


# game			
class Game_Window():

	def __init__(self):
		pygame.init()
		pygame.font.init()
		self.font = pygame.font.SysFont('Comic Sans MS', 20)
		self.screen = pygame.display.set_mode((L,L),0,0)
		self.screen.fill(BG)
		self.clock = pygame.time.Clock()
		
		self.board = Board(self.font)
		self.menu = Menu()
		self.players = [(1,BLUE),(2,RED)]
		self.building = -1
		
		self.board.tiles[ self.board.getTileIndex(5) ].vOwner[0] = (1,1)
		self.board.tiles[ self.board.getTileIndex(2) ].vOwner[4] = (1,1)
		self.board.tiles[ self.board.getTileIndex(1) ].vOwner[2] = (1,1)
		
		self.board.tiles[ self.board.getTileIndex(10) ].vOwner[0] = (2,1)
		self.board.tiles[ self.board.getTileIndex(6) ].vOwner[4] = (2,1)
		self.board.tiles[ self.board.getTileIndex(5) ].vOwner[2] = (2,1)
	
	def update(self):	
		self.draw()
		pygame.display.update()
	
	def draw(self):
		self.screen.fill(BG)
		self.board.draw(self.screen, self.players)
		self.menu.draw(self.screen)
	
	def run(self):	
		while True :
			for event in pygame.event.get():
				# quit the game
				if event.type == pygame.QUIT:
					exit()
				player = self.players[0]
				# handle mouse clicks
				if event.type == pygame.MOUSEBUTTONUP:
					pos = pygame.mouse.get_pos()
					# building options
					# road
					if self.building == 0:
						if event.button == 1:
							for tile in self.board.tiles:	
								if tile.isIn(pos):
									edge = tile.getEdge(pos)
									if edge >= 0:
										if self.board.checkRoadB(tile.tileNum, edge, player):
											tile.eOwner[edge] = player[0]
											neigh = tile.eNeigh[edge]
											# communicate owner
											if neigh > 0:
												ind = self.board.getTileIndex(neigh)
												self.board.tiles[ind].eOwner[ self.board.convertEdge(edge) ] = player[0]
											self.building = -1
						elif event.button == 3:
							self.building = -1
						else:
							self.menu.justOpen(0)
							self.building = -1
					# open menu options
					elif self.menu.isOpen and event.button == 1:
						s = self.menu.check(pos)
						# build
						if s == 'road':
							self.building = 0
						#close menu
						self.menu.close(pos)
					elif self.menu.isOpen and event.button == 3:
						self.menu.justClose(self.menu.openedMenu)
					# do other operations
					else:
						if self.menu.isIn(pos) and event.button == 1:
							self.menu.open(pos)
						for tile in self.board.tiles:	
							if tile.isIn(pos) and event.button == 1:
								print tile.tileNum , '  -  ', tile.getEdge(pos)

			# general update
			self.update()

if __name__ == '__main__':
	app = Game_Window()
	app.run()

