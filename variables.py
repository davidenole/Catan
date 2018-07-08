from math import sin, cos, pi

import pygame

from colours import *

''' screen variables '''

L = 800

''' variables used in the tiles '''

# converts a three-coordinate point to an xy cartesian point
def convert(p, q, r):
	x = (q+r)*cos(pi/6)
	y = p + (q-r)*sin(pi/6)
	return (x,y)

tileRadius = 80
centres = [ (0,0,0), (3,0,0), (-3,0,0), (1,0,-1), (-1,0,1), 
						(-1,-1,0), (1,1,0), (0,1,1), (0,-1,-1), (0,2,2), (0,-2,-2),
						(2,0,-2), (-2,0,2), (2,2,0), (-2,-2,0), (0,0,3), (0,0,-3), (0,3,0), (0,-3,0) ]
											
ctr = [ (tileRadius*convert(i[0], i[1], i[2])[0], tileRadius*convert(i[0], i[1], i[2])[1]) for i in centres]

''' menu variables '''
UBORDER = 150
DIMX = 450
DIMY = 300
THICKNESS = 20
DBORDER = L-UBORDER
UINSIDE = UBORDER + THICKNESS
DINSIDE = DBORDER - THICKNESS

''' UTILS FUNCTIONS '''

# returns if point is inside a given rectangle
def isIn(ux,uy,dx,dy, xy):
	x = xy[0]
	y = xy[1]
	if ux <= x and dx >= x:
		if uy <= y and dy >= y:
			return True

# draws a polygon with a defined number of points and internal / external colour
def drawNgon(screen, n, r, ctr, icolor=WHITE, lcolor = BLACK):
	points = [ (ctr[0]+r*cos(pi/2+2*pi/n*i) , ctr[1]+r*sin(pi/2+2*pi/n*i)) for i in range(n)]	
	pygame.draw.polygon(screen, icolor, points)
	pygame.draw.lines(screen, lcolor, True, points, 2)

# draw settlement with centre in a point
def drawSettlement(screen, ctr, col):
	r = 20
	pygame.draw.circle(screen, col, ctr, r+5)
	pygame.draw.circle(screen, WHITE, ctr, r)
	x, y = ctr[0]-3*r/8 , ctr[1] - r/4
	pygame.draw.rect(screen, col, ( (x,y), (3*r/4,3*r/4) ))
	points = [(x,y), (x+3*r/4-1,y), (x+3*r/8,y-r/4)]
	pygame.draw.polygon(screen, col, points)
	
# draw city with centre in a point
def drawCity(screen, ctr, col):
	r = 20
	pygame.draw.circle(screen, col, ctr, r+5)
	pygame.draw.circle(screen, WHITE, ctr, r)
	pts =  [(6*r/8,-r/2),(6*r/8,0),(5*r/8,r/8), (r/2,0), (r/2,-r/8)] # first house
	pts += [(3*r/8,-r/8), (5*r/16,0), (r/4,-r/8)] # second house
	pts += [(r/4,3*r/8),(r/8,5*r/8),(0,3*r/8),(0,0),(-r/8,r/8),(-r/4,0),(-r/4,3*r/8),(-3*r/8,5*r/8),
					(-r/2,3*r/8),(-r/2,-r/2)] # cathedral
	points = [(ctr[0]-i[0],ctr[1]-i[1]) for i in pts]
	pygame.draw.polygon(screen, col, points)

def mod6(a):
	if a > 0:
		return a%6
	else:
		return mod6(a+12)
