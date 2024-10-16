import pygame
pygame.init()

WIDTH = 500
HEIGHT = 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0 ,0)
YELLOW = (255, 255, 0)

SCREEN.fill(WHITE)
class circle():
    def __init__(self, color, pos, rad, wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = SCREEN

    def draw(self):
       pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

    def grow(self,  x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

position = (300, 300)
radius = 50 
wid = 2
pygame.draw.circle(SCREEN, RED, position, radius, wid)
pygame.display.update()

#creating instances blue circle

bluecircle = circle(BLUE, position, radius+60 )
redcircle = circle(RED, position, radius+40)
yellowcircle = circle(YELLOW, position, radius, 5)
greencircle = circle(GREEN, position, 20)

while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            bluecircle.draw()
            redcircle.draw()
            yellowcircle.draw()
            greencircle.draw()
            pygame.display.update()
        elif (event.type == pygame.MOUSEBUTTONUP):
            bluecircle.grow(2)
            redcircle.grow(2)
            yellowcircle.grow(2)
            greencircle.grow(2)
            pygame.display.update()
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = circle(BLACK, pos, 5)
            blackCircle.draw()
            pygame.display.update()