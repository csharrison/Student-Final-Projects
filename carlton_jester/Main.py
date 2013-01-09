import pygame
from pygame.locals import*
from math import cos,sin,pi,tan,atan2,hypot
import random
import high
screen = pygame.display.set_mode((1024,768))
pygame.init()
#define variables in class
x=1
y=1
radius=1
## how much to add to angle
da=0
uod=0
Going=True
Clock=pygame.time.Clock()
red=0
blue=0
green=0
bs=0
MGT=0
endgamer=0
endgameg=0
endgameb=0
#space ship
class SS (object):
        def __init__(self,x,y,radius,red,green,blue):
                #x and y are the center point
                self.x=x
                self.y=y
                #radius is radius of triangle
                self.radius=radius
                #angles
                self.vx=0
                self.vy=0
                self.angle=pi
                self.red=red
                self.green=green
                self.blue=blue
                self.invis=False
                #don't mess with math
                self.pointlist=[(-self.radius,0),(self.radius*sin((5./18)*pi)+0,-self.radius*sin((2./9)*pi)),(self.radius*sin((5./18)*pi),self.radius*sin((2./9)*pi))]
        def draw(self,surface):
                new_points = [(point[0]+self.x,point[1]+self.y) for point in self.pointlist]
                pygame.draw.polygon(screen,(self.red,self.green,self.blue),new_points)
        def move(self,uod):
                self.x=self.x+self.vx*uod
                self.y=self.y+self.vy*uod
                #for color
                x=self.x
                y=self.y
                #keeps restrictions
                self.x=self.x%1024
                self.y=self.y%768
                if self.x!=x or self.y!=y:
                        self.blue=random.randint(0,255)
                        self.green=random.randint(0,255)
                        self.red=random.randint(0,255)
                        self.invis=False
        def rotate(self,da):
                #rotates a list of points about an axis
                new_points = []
                for point in self.pointlist:
                        new_points.append([point[0]*cos(da) - point[1]*sin(da),point[0]*sin(da)+point[1]*cos(da)])
                self.pointlist=new_points
                self.vx=cos(self.angle)
                self.vy=sin(self.angle)
#######################
class Bullet(object):
        def __init__(self,red,green,blue,Player,incspd):
                self.red=red
                self.green=green
                self.blue=blue
                self.x=Player.x
                self.vx=Player.vx*incspd
                self.y=Player.y
                self.vy=Player.vy*incspd
        def draw(self):
                pygame.draw.circle(screen, (self.red, self.green, self.blue),(int(self.x),int(self.y)),5)
        def update(self):
                self.x=self.vx+self.x
                self.y=self.vy+self.y
class Badguy(object):
        def __init__(self,speed):
                self.x=random.randint(0,1024)
                self.y=random.randint(0,768)
                self.red=random.randint(0,255)
                self.green=random.randint(0,255)
                self.blue=random.randint(0,255)
                self.angle=0
                self.speed=speed
                self.vx=0
                self.vy=0
                self.numbershoot=0
        def create(self):
                pygame.draw.circle(screen, (self.red,self.green,self.blue),(self.x,self.y),15)
        def shoot(self,SS):
                if self.numbershoot/100.==int(self.numbershoot/100.):
                        if Player.invis== True:
                                #random angle
                                self.angle= random.uniform(0,2*pi)
                                self.vx=cos((self.angle))
                                self.vy=sin((self.angle))
                                return Bullet(0,255,0,self,self.speed)
                        if Player.invis==False:
                                #aimed angle
                                self.angle= atan2((SS.y-self.y),(SS.x-self.x))
                                self.vx=cos((self.angle))
                                self.vy=sin((self.angle))
                                return Bullet(0,255,0,self,self.speed)
#########################
Player=SS(896,384,20,0,0,255)
#velocity
vx=0
vy=0
#keeps track of angle
da=0.
nop=0.
Bullethasshot=False
Bullets=[]
Badguys=[]
BadguyC=False
Shooting=False
sniper=.1
Score=0
Gamegoing=True
badguyhasshot=True
badguybullets=[]
while Going==True:
        Clock.tick(60)
        for event in pygame.event.get():
                if event.type==QUIT:
                        Going=False
                if event.type == KEYDOWN:
                        if event.key == K_RIGHT:
                                da=sniper
                        if event.key == K_LEFT:
                                da=-1*(sniper)
                        if event.key == K_UP:
                                nop=5
                        if event.key == K_DOWN:
                                nop=-5
                        if event.key == K_w:
                                Shooting=True
                                Bullethasshot=True
                        if event.key == K_SPACE:
                                Bullethasshot=True
                                Bullet1=Bullet(255,0,0,Player,10)
                                Bullets.append(Bullet1)
                        if event.key==K_LSHIFT:
                                Player.red=0
                                Player.blue=0
                                Player.green=0
                                Player.invis=True
                        if event.key == K_RSHIFT:
                                Player.red=random.randint(0,255)
                                Player.blue=random.randint(0,255)
                                Player.green=random.randint(0,255)
                                Player.invis=False
                        if event.key==K_s:
                                sniper=.05
                        if event.key==K_r:
                                BadguyC=True
                                Badguy1=Badguy(1)
                                Badguys.append(Badguy1)
                                Gamegoing=True
                                Score=0
                if event.type == KEYUP:
                        if event.key == K_RIGHT:
                                da=0
                        if event.key == K_LEFT:
                                da=0
                        if event.key == K_UP:
                                nop=0
                        if event.key == K_DOWN:
                                nop=0
                        if event.key == K_w:
                                Shooting=False
                        if event.key ==K_s:
                                sniper=.1
        Player.angle=Player.angle+da
        #####################
        #remove badguys and add 2 more after 1 is killed
        for badguy in Badguys:
                for bullet in Bullets:
                        if ((bullet.x-badguy.x)**2+(bullet.y-badguy.y)**2)**(.5)<=20:
                                Score=Score+1
                                Badguys.remove(badguy)
                                Badguy1=Badguy(1)
                                Badguy2=Badguy(1)
                                Badguys.append(Badguy1)
                                Badguys.append(Badguy2)
                                break

        #####################
        screen.fill((endgamer,endgameg,endgameb))
        #machine gun shoot
        if Shooting== True and MGT<1000:
                Bullet1=Bullet(255,0,0,Player,6)
                Bullets.append(Bullet1)
                #charge decrease
                MGT=MGT+25
        #machine gun decrease
        if Shooting==False and MGT>0:
                #charge up
                MGT=MGT-2
        if Bullethasshot==True:
                #starts drawing bullets and checks for removed bullets
                for Bullet2 in Bullets:
                        Bullet2.update()
                        Bullet2.draw()
                        if Bullet2.x>2000 or Bullet2.x<-200 or Bullet2.y>1500 or Bullet2.y<-200:
                                Bullets.remove(Bullet2)
        if BadguyC==True:
                #monitors number of shots and time
                for badguy in Badguys:
                        #adds one every frame
                        badguy.numbershoot=1+badguy.numbershoot
                        badguy.create()
                        if badguy.numbershoot/200.==int(badguy.numbershoot/200.):
                                bbullet=badguy.shoot(Player)
                                badguybullets.append(bbullet)
        for bullet3 in badguybullets:
                #badguy bullets update and remove
                bullet3.update()
                bullet3.draw()
                if bullet3.x>1024 or bullet3.x<0 or bullet3.y>768 or bullet3.y<0:
                        badguybullets.remove(bullet3)
        for bullet4 in badguybullets:
                #collision with player and badguy bullets
                if Player.radius+5>=hypot(Player.x-bullet4.x,Player.y-bullet4.y):
                        txt = high.update_score(Score)
                        Gamegoing=False
                        break
                        
        if Gamegoing == False:
                #reset all variables and score on gameover
                badguybullets=[]
                Badguys=[]
                endgamer=255
                endgameg=0
                endgameb=0
                Bullets=[]
                font=pygame.font.Font(None,22)
                text = font.render(txt,True,(0,0,0))
                textwidth=text.get_width()
                textheight=text.get_height()
                textx=512-(textwidth/2.)
                texty=384-(textheight/2.)
                screen.blit(text,(textx,texty))
        if Gamegoing == True:
                #reset color
                endgamer=0
                endgameg=0
                endgameb=0
                
        Player.move(nop)
        Player.rotate(da)
        Player.draw(screen)
        pygame.display.update()

######
        #Space = shoot
        #W = machine gun
        #S = sniper mode
        #Arrowkeys = move
        #r = start and reset
        #LShift = invisible
        #RShift = exit invisible mode
