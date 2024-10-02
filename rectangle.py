import pygame
pygame.init()

WIDTH = 600
HEIGHT = 600
SCREEN=pygame.display.set_mode((WIDTH, HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255) 
RED = (255,0,0)
GREEN = (0,255,0) 
BLUE = (0,0,255) 

SCREEN.fill(WHITE)
pygame.display.update()

class Rectangle():
    def __init__(self, color, dimensions):
        self.rect_surf = SCREEN
        self.rect_color = color
        self.rect_dimensions = dimensions

    def draw(self):

        self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect_dimensions)

greenRect = Rectangle(GREEN,(50,20,100,100))
redRect=Rectangle(RED,(150,200,150,150))
blueRect=Rectangle(BLUE,(300,400,200,200))
#accessing methods 
greenRect.draw()
blueRect.draw()
redRect.draw()
#Display update to reflect the things on screeen
pygame.display.update()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False