 #traffic rush
import pygame
from pygame.locals import *
import math
import random
import datetime

class car:
    #this is the basic initiation fuction for a class
    def __init__(self,x):
        #self.x and self.y are the top left corner of the rectangle/car
        self.v = 1
        self.r=random.randint(150,255)
        self.g=random.randint(150,255)
        self.b=random.randint(150,255)
        #color indications; random to make it more interesting
        
        self.d = random.randint(1,4)
        # 1 is from the left
        # 2 is from the top
        # 3 is from the right, going leftwards
        # 4 is from the bottom, going up
        if x < 5:
            if self.d == 1:
                self.x = -28
                self.y = 165
            if self.d == 2:
                self.x = 175
                self.y = -28
            if self.d == 3:
                self.x = 400
                self.y = 125
            if self.d == 4:
                self.x = 215
                self.y = 300
            if self.d == 1 or self.d == 3:
                self.l= 28
                self.w= 10
            if self.d == 2 or self.d == 4:
                self.l= 10
                self.w= 28
        if x == 5:
            if self.d == 1:
                self.x = -35
                self.y = 163
            if self.d == 2:
                self.x = 173
                self.y = -35
            if self.d == 3:
                self.x = 408
                self.y = 123
            if self.d == 4:
                self.x = 213
                self.y = 308
            if self.d == 1 or self.d == 3:
                self.l= 35
                self.w= 14
            if self.d == 2 or self.d == 4:
                self.l= 14
                self.w= 35
            self.r = 255
            self.g = 255
            self.b = 255
    def draw(self,screen):
        pygame.draw.rect(screen,(self.r,self.g,self.b),(self.x,self.y,self.l,self.w))
    def move(self):
        if self.d == 1:
            self.x = self.x + self.v
        if self.d == 2:
            self.y = self.y + self.v
        if self.d == 3:
            self.x = self.x - self.v
        if self.d == 4:
            self.y = self.y - self.v

#the colission program that i am using
def collide(d, x,y,lisst):
    for c in lisst:
        if d == 1 and c.x != x and c.y != y:
            if abs(x + 28 -(c.x+7)) <3 and abs(y+5 -(c.y+14)) < 32 and c.d !=3:
                return True
        if d == 2 and c.x != x and c.y != y:
            if abs(y + 28 -(c.y+7)) <3 and abs(x+5 -(c.x+14)) < 32 and c.d !=4:
                return True
        if d == 3 and c.x != x and c.y != y:
            if abs(x -(c.x+3)) <3 and abs(y+5 -(c.y+14)) < 32 and c.d != 1:
                return True
        if d == 4 and c.x != x and c.y != y:
            if abs(y -(c.y+3)) <3 and abs(x+5 -(c.x+14)) < 32 and c.d !=2:
                return True
#this i dont use currently
def rect_collide(rect1,rect2):
    r1 = Rect(rect1)
    r2 = Rect(rect2)
    if r1.colliderect(r2): return True
    return False

def write():
    print ''
    print 'Instructions:'
    print 'use the arrow keys to control the cars which are rectangles'
    print 'the goal of the game is to get as many cars to cross the intersection'
    print 'without crashing'
    print 'if you set a new high score, you can enter your name'
    a = 0
    while a < 17:
        print ''
        a = a + 1

def draw_background():
    #imagery
    one = pygame.image.load("1.gif").convert()
    screen.blit(one,(0,0))
    two = pygame.image.load("2.jpg").convert()
    screen.blit(two,(250,0))
    three = pygame.image.load("3.jpg").convert()
    screen.blit(three,(0,200))
    #four = pygame.image.load("4.gif").convert()
    #screen.blit(four,(250,200))
    #four isnot used but it could be if needed
    pygame.draw.rect(screen,(0,255,0),(250,200,150,100))
    
    #traffic lines
    pygame.draw.line(screen, (255,255,255),(0,150), (120,150), 2)
    pygame.draw.line(screen, (255,255,255),(280,150), (400,150), 2)
    pygame.draw.line(screen, (255,255,255),(200,0), (200,70), 2)
    pygame.draw.line(screen, (255,255,255),(200,230), (200,300), 2)
    pygame.draw.line(screen, (255,255,255),(120,150), (120,190), 2)
    pygame.draw.line(screen, (255,255,255),(280,150), (280,110), 2)
    pygame.draw.line(screen, (255,255,255),(200,70), (160,70), 2)
    pygame.draw.line(screen, (255,255,255),(200,230), (240,230), 2)


    #road borders
    pygame.draw.line(screen, (255,255,255),(0,110), (160,110), 2)
    pygame.draw.line(screen, (255,255,255),(0,190), (160,190), 2)
    pygame.draw.line(screen, (255,255,255),(240,110), (400,110), 2)
    pygame.draw.line(screen, (255,255,255),(240,190), (400,190), 2)
    pygame.draw.line(screen, (255,255,255),(160,0), (160,110), 2)
    pygame.draw.line(screen, (255,255,255),(240,0), (240,110), 2)
    pygame.draw.line(screen, (255,255,255),(160,190), (160,300), 2)
    pygame.draw.line(screen, (255,255,255),(240,190), (240,300), 2)

    #intersection crossing left
    pygame.draw.line(screen, (255,255,255),(125,182), (155,182), 2)
    pygame.draw.line(screen, (255,255,255),(125,174), (155,174), 2)
    pygame.draw.line(screen, (255,255,255),(125,166), (155,166), 2)
    pygame.draw.line(screen, (255,255,255),(125,158), (155,158), 2)
    
    pygame.draw.line(screen, (255,255,255),(125,118), (155,118), 2)
    pygame.draw.line(screen, (255,255,255),(125,126), (155,126), 2)
    pygame.draw.line(screen, (255,255,255),(125,134), (155,134), 2)
    pygame.draw.line(screen, (255,255,255),(125,142), (155,142), 2)

    #intersection crossing right
    pygame.draw.line(screen, (255,255,255),(245,182), (275,182), 2)
    pygame.draw.line(screen, (255,255,255),(245,174), (275,174), 2)
    pygame.draw.line(screen, (255,255,255),(245,166), (275,166), 2)
    pygame.draw.line(screen, (255,255,255),(245,158), (275,158), 2)
    
    pygame.draw.line(screen, (255,255,255),(245,118), (275,118), 2)
    pygame.draw.line(screen, (255,255,255),(245,126), (275,126), 2)
    pygame.draw.line(screen, (255,255,255),(245,134), (275,134), 2)
    pygame.draw.line(screen, (255,255,255),(245,142), (275,142), 2)

    #intersection crossing top
    pygame.draw.line(screen, (255,255,255),(168,105), (168,75), 2)
    pygame.draw.line(screen, (255,255,255),(176,105), (176,75), 2)
    pygame.draw.line(screen, (255,255,255),(184,105), (184,75), 2)
    pygame.draw.line(screen, (255,255,255),(192,105), (192,75), 2)
    
    pygame.draw.line(screen, (255,255,255),(232,105), (232,75), 2)
    pygame.draw.line(screen, (255,255,255),(224,105), (224,75), 2)
    pygame.draw.line(screen, (255,255,255),(216,105), (216,75), 2)
    pygame.draw.line(screen, (255,255,255),(208,105), (208,75), 2)

    #intersection crossing bottom
    pygame.draw.line(screen, (255,255,255),(168,195), (168,225), 2)
    pygame.draw.line(screen, (255,255,255),(176,195), (176,225), 2)
    pygame.draw.line(screen, (255,255,255),(184,195), (184,225), 2)
    pygame.draw.line(screen, (255,255,255),(192,195), (192,225), 2)

    pygame.draw.line(screen, (255,255,255),(232,195), (232,225), 2)
    pygame.draw.line(screen, (255,255,255),(224,195), (224,225), 2)
    pygame.draw.line(screen, (255,255,255),(216,195), (216,225), 2)
    pygame.draw.line(screen, (255,255,255),(208,195), (208,225), 2)

pygame.init()
screen = pygame.display.set_mode((400,300))
clock = pygame.time.Clock()
tick = -100
carlist = []
write()
q = 0

#scoring/ text
y = 0
top = 0
our_font = pygame.font.Font(None,22)
text = our_font.render(str(y), False, (255,0,255))
toptext = our_font.render(str(top), False, (0,0,255))
english = our_font.render('High Score', False, (0,0,255))
language = our_font.render('Your Score', False, (255,0,0))
credit = our_font.render('By Andrew Xia', False, (0,0,255))
disp = our_font.render('The car has crashed', False, (0,0,255))
disptwo = our_font.render('Click to Restart', False, (0,0,255))
record = False
end = False

#writing former high scores
f = open('highscores.txt',"r")
lines = []
for line in f:
    lines.append(line)
f.close()
f = open("highscores.txt","w")
for line in lines:
    f.write(line)
f.write('\n')
f.write(str(datetime.date.today().day)+"/"+str(datetime.date.today().month)+'/'+str(datetime.date.today().year)+'\n')


going = True
while going == True:
    #background draw
    screen.fill((50,50,50))
    draw_background()
    #quitting
    for event in pygame.event.get():
    	if event.type == QUIT:
            f.close()
	    going = False
        if event.type == MOUSEBUTTONDOWN and end == True:
            end = False
            y = 0
        #speeding up cars
        if event.type == KEYDOWN:
            if event.key == K_p:
                end = True
            if event.key == K_RIGHT:
                for c in carlist:
                    if c.d == 1 and c.v != 3:
                        c.v = 3
                        break
            if event.key == K_LEFT:
                for c in carlist:
                    if c.d == 3 and c.v != 3:
                        c.v = 3
                        break
            if event.key == K_UP:
                for c in carlist:
                    if c.d == 4 and c.v != 3:
                        c.v = 3
                        break
            if event.key == K_DOWN:
                for c in carlist:
                    if c.d == 2 and c.v != 3:
                        c.v = 3
                        break
    #the actual loop of creating cars
    if tick > 75 and y < 20:
        tick = 0
        carlist.append(car(q))
    if tick > 60 and y < 40 and y >= 20:
        tick = 0
        q = q + 1
        carlist.append(car(q))
    if tick > 50 and y >= 40 and y < 60:
        tick = 0
        q = q + 1
        carlist.append(car(q))
    if tick > 36 and y < 80 and y >= 60:
        tick = 0
        q = q + 1
        carlist.append(car(q))
    if tick > 30 and y >= 80:
        tick = 0
        carlist.append(car(q))

    #for loop for drawing, moving, removing, crashing cars
    for c in carlist:
        if c.x > 401 or c.x < -51 or c.y < -51 or c.y > 301:
            carlist.remove (c)
            y = y + 1
    for c in carlist:
        c.draw(screen)
        c.move()
        for r in carlist:
            if c.l != r.l and rect_collide((c.x,c.y,c.l,c.w),(r.x,r.y,r.l,r.w)):
                pygame.display.update()
                a = 0
                while a < 100:
                    a = a + 1
                    clock.tick(80)
                end = True
    #when the game ends...
    if end == True:
        carlist = []
        if top < y:
            top = y
            toptext = our_font.render(str(top), False, (0,0,255))
            if top > 20:
                record = True
        pygame.draw.rect(screen,(250,250,250), (170,145,170,50))
        screen.blit(disp, (180,150))
        screen.blit(disptwo, (180,175))

    #text functions
    text = our_font.render(str(y), False, (255,0,0))
    screen.blit(text, (260,240))
    screen.blit(toptext, (260,220))
    screen.blit(credit, (260,260))
    screen.blit(language, (285,240))
    #language is your score
    screen.blit(english, (285,220))
    #other functions
    clock.tick(80)
    if end == False:
        tick = tick + 1
    pygame.display.update()
    if record == True:
        f.write(str(top)+'    ')
        f.write(raw_input('new highscore! please enter your name: '))
        f.write('\n')
        write()
        record = False
    if q == 5:
        q = 1
