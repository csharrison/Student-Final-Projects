#circle collide w/rect
import pygame
from pygame.locals import *

def collide(x,y, r, rect):
	cdx = abs(x-rect[0] - rect[2]/2.)
	cdy = abs(y-rect[1] - rect[3]/2.)

	if cdx > rect[2]/2. + r: return False
	if cdy > rect[3]/2. + r: return False

	if cdx <=rect[2]/2. + r: return True
	if cdy <= rect[3]/2. + r: return True
	
	corner_d = (cdx - rect[2]/2.)**2 + (cdy - rect[3]/2.)**2
	return corner_d <= r**2


	
if __name__ == '__main__':
	pygame.init()
	screen = pygame.display.set_mode((400,400))
	
	rect = (100,100,100,10)
	going = True
	while going == True:
		for e in pygame.event.get():
			if e.type == QUIT:
				going = False
	
		x,y = pygame.mouse.get_pos()
		r = 20
		color = (200,200,200)
		if collide(x,y,r,rect):
			print 'sdfsdf'
			color = (255,0,0)
			
		screen.fill((0,0,0))
		pygame.draw.rect(screen,(0,255,0),rect)
		pygame.draw.circle(screen,color,(x,y),r)
		pygame.display.update()