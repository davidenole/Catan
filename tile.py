from math import sqrt
import pygame

from colours import *
from variables import *

class Tile:
	
	def __init__(self, relPt, pt, N, tipe, font):
		# centre
		self.relX = int(relPt[0])
		self.relY = int(relPt[1])
		self.x = int(pt[0])
		self.y = int(pt[1])
		self.centre = (self.x,self.y)
		# linear dimensions
		self.l = tileRadius
		self.w = self.l*sqrt(3)/2
		# attributes
		self.n = N
		self.type = tipe
		self.col = colType(tipe)
		if self.n in [6,8]:
			self.ncol = DRED
		else:
			self.ncol = BLACK
		self.font = font
		self.txt = self.font.render(str(self.n), False, self.ncol)
		# edges and vertices
		self.tileNum = self.setTileNumber()
		self.vOwner = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0)]
		self.eOwner = [0,0,0,0,0,0]
		self.eNeigh = self.getENeigh()
		self.vNeigh = self.getVNeigh()	
	
	# set the number of the tile (0 tl, 19 br)
	def setTileNumber(self):
		x = self.relX
		y = -self.relY
		r = self.l
		if x == 0:
			if y == 0:
				return 10
			elif y>2.5*r:
				return 2
			else:
				return 18
		elif y == 0:
			if x < -2*r:
				return 8
			elif x < -r:
				return 9
			elif x > 2*r:
				return 12
			else:
				return 11
		else:
			if y > 2*r:
				if x > 0:
					return 3
				else:
					return 1
			elif y > 0:
				if x > 2*r:
					return 7
				elif x > 0:
					return 6
				elif x < -2*r:
					return 4
				else:
					return 5
			elif y < -2*r:
				if x > 0:
					return 19
				else:
					return 17
			else:
				if x > 2*r:
					return 16
				elif x > 0:
					return 15
				elif x < -2*r:
					return 13
				else:
					return 14	
	
	# returns the neighbours at the edges of the current tile
	def getENeigh(self):
		n = [[0,0,2,5,4,0],[0,0,3,6,5,1],[0,0,0,7,6,2],
				 [0,1,5,9,8,0],[1,2,6,10,9,4],[2,3,7,11,10,5],
				 [3,0,0,12,11,6],[0,4,9,13,0,0],[4,5,10,14,13,8],
				 [5,6,11,15,14,9],[6,7,12,16,15,10],[7,0,0,0,16,11],
				 [8,9,14,17,0,0],[9,10,15,18,17,13],[10,11,16,19,18,14],
				 [11,12,0,0,19,15],[13,14,18,0,0,0],[14,15,19,0,0,17],[15,16,0,0,0,18]]
		return n[self.tileNum-1]
	
	# returns the neighbours at the vertices of the current tile
	# in 2-tuples
	def getVNeigh(self):
		a = [0,1,2,3,4,5,0]
		return [(self.eNeigh[a[i]], self.eNeigh[a[i+1]]) for i in range(6)]
	
	# returns true if point xy is inside the tile
	def isIn(self, xy):
		# relative coordinates
		x , y  = xy[0]- self.x , xy[1] - self.y
		# conditions
		if y > self.l or y < -self.l:
			return False
		elif x < -self.w or x > self.w:
			return False
		elif y > self.l/2:
			y = y-self.l/2
			if x > 0:
				if y <= self.l/2 - self.l/2/self.w * x:
					return True
				else:
					return False
			else:
				if y <= self.l/2 + self.l/2/self.w * x:
					return True
				else:
					return False
		elif y < -self.l/2:
			y = y+self.l/2
			if x > 0:
				if y >= -self.l/2 + self.l/2/self.w * x:
					return True
				else:
					return False
			else:
				if y >= -self.l/2 - self.l/2/self.w * x:
					return True		
				else:
					return False
		else:
			if x < self.w and x > -self.w:
				return True
			else:
				return False
		return False

	# returns the clicked edge by point xy
	def getEdge(self, xy):
		# assume point is inside
		# relative coordinates
		x , y  = xy[0] - self.x , xy[1] - self.y	
		# conditions
		# not really clicking an edge
		if x**2 + y**2 < (self.l**2)*0.49:
			return -1
		# clicking an edge
		else:		
			if y < -self.l/2:
				if x > 0:
					return 1
				else:
					return 0
			elif y < self.l/2:
				if x > 0:
					return 2
				else:
					return 5
			else:
				if x > 0:
					return 3
				else:
					return 4
	
	# draws the tile on the board
	def draw(self, screen, players):
		drawNgon(screen, 6, self.l, self.centre, self.col)
		if self.type != 'desert':
			pygame.draw.circle(screen, self.ncol, self.centre, int(self.l/4))
			pygame.draw.circle(screen, WHITE, self.centre, int(self.l/4-2))
			if self.n >= 10:
				x = self.x - 10
				y = self.y - 15			
			else:
				x = self.x - 5
				y = self.y - 15
			screen.blit(self.txt,(x,y))
		# owners
		# roads
		for i in range(len(self.eOwner)):
			if self.eOwner[i] > 0:
				col = players[ self.eOwner[i]-1 ][1]
				r = self.l
				ctr = self.centre
				pt = [ ( ctr[0]-r*cos(pi/2+2*pi/6*(j-1)) , ctr[1]-r*sin(pi/2+2*pi/6*(j-1)) ) for j in range(i,i+2)]
				x = ( int(pt[0][0]),int(pt[0][1]) )
				y = ( int(pt[1][0]),int(pt[1][1]) )
				pygame.draw.line(screen, WHITE, x,y, 10)
				pygame.draw.line(screen, col, x,y, 6)
		# settlements / cities
		for i in range(len(self.vOwner)):
			if self.vOwner[i] != (0,0):
				v = i
				col = players[ self.vOwner[i][0]-1 ][1]
				ctr = self.centre
				r = self.l
				pt =( ctr[0]-r*cos(pi/2+2*pi/6*(v)) , ctr[1]-r*sin(pi/2+2*pi/6*(v)) )
				x = ( int(pt[0]),int(pt[1]) )				
				if self.vOwner[i][1] == 1:
					drawSettlement(screen, x, col)
				elif self.vOwner[i][1] == 2:
					drawCity(screen, x, col)


