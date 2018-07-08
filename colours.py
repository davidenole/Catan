BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
DRED = (193,0,0)
BLUE = (0,0,255)

GRAIN = (255,165,0)
CLAY = (255,99,71)
WOOD = (34,139,34)
ROCK = (107, 107, 81)
SHEEP = (153, 255, 51)
DESERT = (223,193,99)

resCols = {'g':GRAIN, 'c':CLAY, 'w':WOOD, 'r':ROCK, 's':SHEEP}

BG = (0,87,139)
BUILDMENU = (157, 40, 0)
BBUILDMENU = (161, 79, 24)

# given the attribute of a tile, colours it differently
def colType(t):
	tipes = ['desert','clay','rock','wood','grain','sheep']
	cols = [DESERT,CLAY,ROCK,WOOD,GRAIN,SHEEP]
	return cols[ tipes.index(t) ]
