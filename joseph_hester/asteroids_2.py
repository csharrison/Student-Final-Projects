#Joe Hester
#Asteroids
#final project
import pygame
from pygame.locals import *
from math import cos,sin,pi,hypot
import random


class Ship(object):
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.angle = -pi/2
        self.v = 0
        self.pointlist = [(0,-10),(-5,10),(5,10)]
        
    def draw(self,screen):
        non_local_pl = [(point[0]+self.x,point[1]+self.y) for point in self.pointlist]
        pygame.draw.polygon(screen,(255,0,0),non_local_pl)

    def move(self):
        self.vy = self.v*sin(self.angle)
        self.vx = self.v*cos(self.angle)
        self.x = (self.x+self.vx)%1200
        self.y = (self.y+self.vy)%700

    def rotate(self,dangle):
        self.angle = self.angle + dangle
        #rotates a list of points about an axis
        new_points = []
        for point in self.pointlist:
            new_points.append([point[0]*cos(dangle) - point[1]*sin(dangle),point[0]*sin(dangle)+point[1]*cos(dangle)])
        self.pointlist = new_points

class Faser(object):
    v = 20
    def __init__(self,x,y,r,vx,vy):
        self.x = x
        self.y = y
        self.r = r
        self.vx = vx
        self.vy = vy
        self.angle = -pi/2
        self.red = 255
        self.green = 255
        self.blue = 255

    def draw(self,surface):
        
        pygame.draw.circle(surface,(self.red,self.green,self.blue),(int(self.x),int(self.y),),self.r)
    def move(self):
        self.x = self.x + self.vx
        self.y = self.y + self.vy
    
    def change_color(self):
        self.red = random.randint(0,255)
        self.green = random.randint(0,255)
        self.blue = random.randint(0,255)
class Rock(object):
    def __init__(self,x,y,vx,vy,r):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r

    def draw(self,surface):
        pygame.draw.circle(surface,(255,255,255),(int(self.x),int(self.y)),self.r)
     
    def move(self):
        self.x = (self.x+self.vx)%1200
        self.y = (self.y+self.vy)%700
    
    
    



pygame.init()
screen = pygame.display.set_mode((1200,700))
clock = pygame.time.Clock()
ship = Ship(300,300,0,0)
rightpress = False
leftpress = False
upup = True
updown = False
vmax = 10
bull = []
ast = []
for i in xrange(6):
    ast.append(Rock(random.randint(0,1700), random.randint(0,700), random.uniform(-3,3), random.uniform(-3,3), 30))
playing = True

going = True
dead = False
while going == True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            going = False
        
        

        if event.type == KEYDOWN:
            
            if event.key == K_RIGHT:
                rightpress = True
                
            elif event.key == K_LEFT:
                leftpress = True
                
            elif event.key == K_UP:
                ship.move()
                upup = False
                updown = True
            elif event.key == K_SPACE:
                bull.append(Faser(ship.x,ship.y,7,Faser.v*cos(ship.angle),Faser.v*sin(ship.angle)))
                
                
                

        if event.type == KEYUP:
            if event.key == K_RIGHT:
                rightpress = False
            if event.key == K_LEFT:
                leftpress = False

            if event.key == K_UP:
                upup = True
                updown = False
        elif event.type == MOUSEBUTTONDOWN:
            if dead == True:
                dead = False
                ship.v = 0
                ship.x = 600; ship.y = 350
                ast = []
                for i in xrange(6):
                    ast.append(Rock(random.randint(0,1700), random.randint(0,700), random.uniform(-3,3), random.uniform(-3,3), 30))

        
    if dead == False:        
        for circ in bull:
            circ.draw(screen)
            circ.move()
            circ.change_color()
            if circ.x >= 1207 or circ.x <= -7:
                bull.remove(circ)
            if circ.y >= 707 or circ.y <= -7:
                bull.remove(circ)
            for rock in ast:
                if hypot(rock.x-circ.x,rock.y-circ.y)<rock.r + circ.r:
                    if rock.r > 10:
                        for i in xrange(3):
                            new_rock = Rock(rock.x,rock.y,random.uniform(-3,3),random.uniform(-3,3),rock.r/2)
                            ast.append(new_rock)
                    ast.remove(rock)
                    bull.remove(circ)
                    break


        for rock in ast:
                rock.draw(screen)
                rock.move()
                if hypot(rock.x-ship.x,rock.y-ship.y) < rock.r+9:
                    dead = True


        if rightpress == True:
            ship.rotate(.05)
        if leftpress == True:
            ship.rotate(-.05)
        if upup == True:
            ship.v = ship.v/1.01
        if updown == True:
            ship.v = ship.v + .5
        if ship.v >= vmax:
            ship.v = vmax
        
        if playing == True:    
            clock.tick(50)
            
            ship.draw(screen)
            ship.move()
    else:
        screen.fill((255,0,0))
    

   
    
    
    pygame.display.update()
