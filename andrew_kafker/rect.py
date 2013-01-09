from pygame import Rect
def rect_collide(rect1,rect2):
    r1 = Rect(rect1)
    r2 = Rect(rect2)
    if r1.colliderect(r2): return True
    return False

if __name__ == "__main__":
    import pygame
    from pygame.locals import *
    pygame.init()
    screen = pygame.display.set_mode((400,400))
    going = True
    while going == True:
        for e in pygame.event.get():
            if e.type == QUIT: going = False

        screen.fill((0,0,0))
            
        x,y = pygame.mouse.get_pos()

        r1 = (200,200,100,100)
        r2 = (x,y, 100,100)
        pygame.draw.rect(screen,(255,255,255),r1)
        if rect_collide(r1,r2):
            pygame.draw.rect(screen,(255,0,255),r2)
        else:
            pygame.draw.rect(screen,(255,0,0),r2)
        pygame.display.update()
        
