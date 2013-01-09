import pygame
from pygame.locals import *
from rect import rect_collide
import random

screen = pygame.display.set_mode ((700,700))

class Rectangle (object):
    def __init__(self,y,x,width,height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height

    def draw(self,screen):
        pygame.draw.rect(screen, (0,0,255), (self.x,self.y,self.width,self.height))
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy

class Rectangle1 (object):
    def __init__(self,y,x,width,height):
      self.x = x
      self.y = y
      self.width = width
      self.height = height

    def draw(self,screen):
        pygame.draw.rect(screen, (0,255,0), (self.x,self.y,self.width,self.height))
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy
pygame.init()
g = -10
z = 0
p = 10
m = 0
xpos = 70
ypos = 0
xpos2 = 0
ypos2 = 0
list1 = []
list2 = []
pongfont = pygame.font.Font(None,22)
pongfont2 = pygame.font.Font(None,12)
name = pongfont.render('Made by the awesome Andrew Kafker :)', False, (255,0,255))
text = pongfont.render('PLAYER TWO LOSES', False, (255,0,255))
text1 = pongfont.render('PLAYER ONE LOSES', False, (255,0,255))
clock = pygame.time.Clock()
snake1 = Rectangle(0,700,10,10)
snake2 = Rectangle1(0,0,10,10)
going = True
while going == True:
    for event in pygame.event.get():

        if event.type == QUIT:
            going = False
        if event.type == MOUSEBUTTONDOWN:
            screen.fill(((random.randint(0,255)),(random.randint(0,255)),(random.randint(0,255))))
            snake1.x = 700
            snake1.y = 0
            snake1.width = 10
            snake1.height = 10
            snake2.x = 0
            snake2.y = 0
            snake2.width = 10
            snake2.height = 10
            list1 = []
            list2 = []
            g = -10
            z = 0
            p = 10
            m = 0
            xpos = 70
            ypos = 0
            xpos2 = 0
            ypos2 = 0
            snake1.draw(screen)
            snake2.draw(screen)
            
        if event.type == KEYDOWN:
            if p != 0 or g != 0 or m != 0 or z != 0:
                if event.key == K_RIGHT:
                    if g == -10:
                        g = -10
                        z = 0
                    elif g == 0:
                        g = 10
                        z = 0 

                elif event.key == K_LEFT:
                    if g == 10:
                        g = 10
                        z = 0
                   
                    elif g == 0:
                        g = -10
                        z = 0
                elif event.key == K_DOWN:
                    if z == -10:
                        g = 0
                        z = 0
                
                    elif z == 0:
                        z = 10
                        g = 0
                        
                elif event.key == K_UP:
                    if z == 10:
                        z = 10
                        g = 0
                    
                    elif z == 0:
                        z = -10
                        g = 0
                elif event.key == K_d:
                    if p == -10:
                        p = -10
                        m = 0
                    elif p == 0:
                        p = 10
                        m = 0
            
                elif event.key == K_a:
                    if p == 10:
                        p = 10
                        m = 0
                        xpos = xpos - 1
                    elif p == 0:
                        p = -10
                        m = 0
                elif event.key == K_s:
                    if m == -10:
                        p = 0
                        m = -10
                
                    elif m == 0:
                        m = 10
                        p = 0
                        
                elif event.key == K_w:
                    if m == -10:
                        p = 0
                        m = -10
                
                    elif m == 0:
                        m = -10
                        p = 0
            
                
            

    
    snake1.draw(screen)
    snake2.draw(screen)
    clock.tick(20)
    snake1.move(g,z)
    snake2.move(p,m)
    if z == 10:
        ypos = ypos + 1
    if z == -10:
        ypos = ypos - 1
    if g == 10:
        xpos = xpos + 1
    if g == -10:
        xpos = xpos - 1
    if p == 10:
        xpos2 = xpos2 + 1
    if p == -10:
        xpos2 = xpos2 - 1
    if m == 10:
        ypos2 = ypos2 + 1
    if m == -10:
        ypos2 = ypos2 - 1
    
    for nums in list1:
        if p != 0 or g != 0 or m != 0 or z != 0:
            if (xpos,ypos) == nums:
                screen.blit(text1, (350,350))
                p = 0
                g = 0
                m = 0
                z = 0
                break
            if (xpos2,ypos2) == nums:
                screen.blit(text, (100,350))
                p = 0
                g = 0
                m = 0
                z = 0
                break
    for nums1 in list2:
        if p != 0 or g != 0 or m != 0 or z != 0:
            if (xpos2,ypos2) == nums1:
                screen.blit(text, (100,350))
                p = 0
                g = 0
                m = 0
                z = 0
                break
            if (xpos,ypos) == nums1:
                screen.blit(text1, (350,350))
                p = 0
                g = 0
                m = 0
                z = 0
                break
    if xpos > 69:
        screen.blit(text1, (350,350))
        p = 0
        g = 0
        m = 0
        z = 0

    if xpos2 > 69:
        screen.blit(text, (100,350))
        p = 0
        g = 0
        m = 0
        z = 0
    if ypos > 69:
        screen.blit(text1, (350,350))
        p = 0
        g = 0
        m = 0
        z = 0
    if ypos2 > 69:
        screen.blit(text, (100,350))
        p = 0
        g = 0
        m = 0
        z = 0

    if xpos < 0:
        screen.blit(text1, (350,350))
        p = 0
        g = 0
        m = 0
        z = 0

    if xpos2 < 0:
        screen.blit(text, (100,350))
        p = 0
        g = 0
        m = 0
        z = 0

    if ypos < 0:
        screen.blit(text1, (350,350))
        p = 0
        g = 0
        m = 0
        z = 0
    if ypos2 < 0:
        screen.blit(text, (100,350))
        p = 0
        g = 0
        m = 0
        z = 0
    if (xpos,ypos) == (xpos2,ypos2):
        screen.blit(text1, (350,350))
        screen.blit(text, (100,350))
        p = 0
        g = 0
        m = 0
        z = 0

        
        
    list1.append((xpos,ypos))
    list2.append((xpos2,ypos2))
    screen.blit(name, (200,680))
    pygame.display.update()
    
