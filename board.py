from math import sin, cos, pi, sqrt
from random import randint
import pygame

from variables import *
from colours import *
from tile import *

class Board:

	def __init__(self, font):
	
		# visualisation
		self.font = font
	
		# tiles
		self.tiles = self.createBoard()
		
		
	
	# creates the initial board
	def createBoard(self):
		tiles = []
		terrs = ['desert'] + ['clay']*3 +['rock']*3 + ['wood']*4 + ['grain']*4 + ['sheep']*4
		used = []
		nums = [2,12] + [3,4,5,6,8,9,10,11]*2
		usedn = []
		for i in ctr:
			a = i[0]+L/2
			b = i[1]+L/2-L/25
			t = randint(0,len(terrs)-1)
			while t in used:
				t = randint(0,len(terrs)-1)
			used.append(t)
			if terrs[t]!='desert':
				u = randint(0,len(nums)-1)
				while u in usedn:
					u = randint(0,len(nums)-1)
				usedn.append(u)
			tiles.append( Tile((i[0],i[1]),(a,b),nums[u],terrs[t], self.font) )
		return tiles

	# returns index of the tile addressed with a certain number
	def getTileIndex(self, tileNum):
		c = 0
		for tile in self.tiles:
			if tile.tileNum == tileNum:
				return c
			c += 1
	
	# converts the neighbour number, given a certain edge
	# returns the edge of the neighbour corresponding to 
	#	the given edge
	def convertEdge(self, edge):
		return (edge+3) % 6

	# checks if player "pl" can build a road in tile
	# number "tn" on edge "e"
	def checkRoadB(self, tn, e, pl):
		tile = self.tiles[ self.getTileIndex(tn) ]
		pl = pl[0]
		if tile.eOwner[e] != 0:
			return False
		else:
			if tile.vOwner[e][0] == pl or tile.vOwner[ mod6(e-1) ][0] == pl:
				return True
			# first vertex
			# my edge
			ed = mod6(e-1)
			if tile.eOwner[ed] == pl and tile.vOwner[ed] != (0,0) and tile.vOwner[ed][0] != pl:
				return False
			elif tile.eOwner[ed] == pl and tile.vOwner[ed] == (0,0):
				return True
			# neighbour's edge	
			if tile.vNeigh[mod6(e-1)][0] > 0:
				n = self.getTileIndex( tile.vNeigh[mod6(e-1)][0] ) 
				ntile = self.tiles[n]
				edd = mod6(e+1)
				if ntile.eOwner[edd] == pl and tile.vOwner[ed] != (0,0) and tile.vOwner[ed][0] != pl:
					return False
				elif ntile.eOwner[edd] == pl and tile.vOwner[ed] == (0,0):
					return True			
			# second vertex	
			# my edge
			ed = mod6(e+1)
			if tile.eOwner[ed] == pl and tile.vOwner[e] != (0,0) and tile.vOwner[e][0] != pl:
				return False
			elif tile.eOwner[ed] == pl and tile.vOwner[e] == (0,0):
				return True
			# neighbour's edge	
			if tile.vNeigh[e][1] > 0:
				n = self.getTileIndex( tile.vNeigh[e][1] ) 
				ntile = self.tiles[n]
				ed = mod6(e+1)
				if ntile.eOwner[ed] == pl and tile.vOwner[e] != (0,0) and tile.vOwner[e] != pl:
					return False
				elif ntile.eOwner[ed] == pl and tile.vOwner[e] == (0,0):
					return True
			return False
						
	# draw board on screen
	def draw(self, screen, players):
		for tile in self.tiles:
			tile.draw(screen, players)

