#Tessa Kadar
#final project: brickbreaker
import pygame
from pygame.locals import *

import Collision

#create a circle class that will make a circle object
#define x and y (center) and r (radius)
class Circle(object):
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r

    #define a draw function that will draw a circle
    def draw(self,screen):
        pygame.draw.circle(screen,(200,0,255),(int(self.x),int(self.y)),int(self.r))

    #define a move function with arguments dx (direction for x) and dy (direction for y)
    #move changes x value by adding dx and y value by adding dy
    def move(self,dx,dy):
        self.x = self.x + dx
        self.y = self.y + dy


#create a paddle class that will make a paddle object
#define x and y (top left corner), w (width) and h (height)
class Paddle(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    #define a draw function that will draw a rectangle
    def draw(self,screen):
        pygame.draw.rect(screen,(0,255,100),(self.x,self.y,self.w,self.h))

    #define a move function that changes the x coordinate to move + pdx units
        
    def move(self,pdx):
        self.x = self.x + pdx


#create a Brick class that will make a brick object
#define x and y (top left corner), w (width) and h (height)
class Brick(object):
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    #define a draw function that will draw a rectangle with a one pixel border
    def draw(self,screen):
        pygame.draw.rect(screen,(255,0,0),(self.x+1,self.y+1,self.w-1,self.h-1))


#initialize the screen at 500 pixels wide and 400pixels high
pygame.init()
screen = pygame.display.set_mode((500,400))

#fill the screen with white
screen.fill((255,255,255))

#paddle is the Paddle object with its top left corner at (0,390) with a width
#of 50 and a height of 10
paddle = Paddle(0,390,50,10)

#ball is the Ball object with its center at (10,300) with a radius of 10
ball = Circle(10,200,10)

#vx, or the horizontal velocity of the ball, starts at 3
vx = 1

#vy, or the vertical velocity of the ball, starts at 3
vy = 3

#px, or the horizontal velocity of the paddle, starts at 0
px = 0

#initialize a list for each of three rows of bricks with nothing in the lists
Bricks1 = []

Bricks2 = []

Bricks3 = []

#initialize the value x, for the x value of the bricks, at zero
x = 0

while x <= 450:
    #as long as x is less than or equal to 450, add a Brick object to the Bricks1
    #list so that its top left corner is at (x,0) and it is 50 pixels wide
    #and 20 pixels high
    #do the same for the other two lists, but move each row of rectangles down
    #30 pixels
    Bricks1.append(Brick(x,0,50,20))
    Bricks2.append(Brick(x,20,50,20))
    Bricks3.append(Brick(x,40,50,20))
    #increase x by 50
    x = x + 50

#start with 5 lives
lives = 5

#clock is the clock function
clock = pygame.time.Clock()

#create a font as the default font at size 100
our_font = pygame.font.Font(None,100)

#create "FAIL" in purple
failtext = our_font.render("FAIL", False, (255,0,255))

#create "Hit space" in purple
start_text = our_font.render('Hit space', False,(255,0,255))

#create "to start" in purple
start_text2 = our_font.render('to start', False, (255,0,255))

#create "YOU WIN!" in purple
wintext = our_font.render('YOU WIN!',False,(255,0,255))

#start space as false and playing as true
space = False
playing = True
#while clicked is false and playing is true, show the start screen
#if the player hits the spacebar, space becomes true
while playing == True and space == False:
    screen.blit(start_text, (25,100))
    screen.blit(start_text2, (25,200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT: playing = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE: space = True
#while playing is true (and space is true) if the player quits, end the game
#while the player hasn't quit, run the game
while playing == True:
    for event in pygame.event.get():
        if event.type == QUIT: playing = False
        if event.type == KEYDOWN:
            
            #if the player hits the right arrow key, change the paddle's velocity
            #so that it will go right
            if event.key == K_RIGHT:
                px = 4
            #if the player hits the left arrow key, change the paddle's velocity
            #so that it will go left
            if event.key == K_LEFT:
                px = -4

        #if the player lifts the arrow key, change the paddle's velocity so that
        #it will stop moving
        if event.type == KEYUP:
            px = 0

    #if the ball hits the right wall, change its velocity so it goes left
    if ball.x >=490:
        vx = -vx
        ball.x = 490

    #if the ball hits the left wall, change its velocity so it goes right
    if ball.x < 10:
        vx = -vx
        ball.x = 10

    #if the ball hits the top, change its velocity so it goes down
    if ball.y < 10:
        vy = 3

    #if the paddle hits the left wall, change its velocity so it stops moving
    if paddle.x < 0:
        paddle.x = 0

    #if the paddle hits the right wall, change its velocity so it stops moving
    if paddle.x > 450:
        paddle.x = 450

    #if the ball hits the paddle, change the ball's velocity so it goes up
    
    if Collision.collide(ball.x,ball.y,ball.r,(paddle.x,paddle.y,paddle.w,paddle.h)):
        vy = -3
        if paddle.x < ball.x:
            vx = -((paddle.x+paddle.w/2.)-ball.x)/15
        elif paddle.x >= ball.x:
            vx = ((paddle.x+paddle.w/2.)-ball.x)/15
        
    #slows down the screen
    clock.tick(60)

    #move the ball vx pixels right and vy pixels down
    ball.move(vx,vy)

    #move the paddle px pixels right
    paddle.move(px)

    #fill the screen with white
    screen.fill((255,255,255))

    #draw the ball on the screen
    ball.draw(screen)

    #draw the paddle on the screen
    paddle.draw(screen)

    #for each row of bricks:
    #if the ball hits one of the bricks, remove that brick from the list of bricks
    #so that it disappears from the screen
    #then draw all the bricks
    for brick in Bricks1:
        if Collision.collide(ball.x,ball.y,ball.r,(brick.x,brick.y,brick.w,brick.h)):
            Bricks1.remove(brick)
            vy = 3
        brick.draw(screen)

    for brick in Bricks2:
        if Collision.collide(ball.x,ball.y,ball.r,(brick.x,brick.y,brick.w,brick.h)):
            Bricks2.remove(brick)
            vy = 3
        brick.draw(screen)

    for brick in Bricks3:
        if Collision.collide(ball.x,ball.y,ball.r,(brick.x,brick.y,brick.w,brick.h)):
            Bricks3.remove(brick)
            vy = 3
        brick.draw(screen)

    #if the ball goes past the paddle and off the bottom of the screen,
    #the variable lives goes down by 1, the ball starts off the screen,
    #and the paddle goes back to the left of the screen
    if ball.y > 400:
        lives = lives - 1
        ball.x = -10
        ball.y = 200
        paddle.x = 0
        vx = 1
        vy = 3

    #if the variable lives gets to zero (if the player is out of lives)
    #show the end screen, slow down the clock so the end screen stays longer,
    #then close the window
    if lives == 0:
        screen.fill((0,0,0))
        screen.blit(failtext, (250,200))
        pygame.display.update()
        clock.tick(5)
        playing = False

    #if all the brick lists are empty (if the player destroys all the bricks)
    #show the win screen, slow down the clock so the end screen stays longer,
    #then close the window
    if Bricks1 == [] and Bricks2 == [] and Bricks3 == []:
        screen.fill((255,255,255))
        screen.blit(wintext,(50,200))
        pygame.display.update()
        clock.tick(5)
        playing = False

    #update the screen
    pygame.display.update()
