import pygame
import time
pygame.init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Birthday Greeting Card')

image1 = pygame.image.load("C:/Users/prave/OneDrive - OMO Scholengroep Helmond/Desktop/Jetlearn/Pro_Game_Developer/images/birthday-1.jpg")
image = pygame.transform.scale(image1, (WIDTH, HEIGHT))

while(True):
    font = pygame.font.SysFont("Times New Roman", 72)
    text = font.render("Happy", True, (0, 0, 0))
    text2 = font.render("Birthday", True, (0, 0, 0))
    screen.fill((255,255,255))
    screen.blit(image,(0,0))
    screen.blit(text,(210,180))
    screen.blit(text2,(180,264))
    pygame.display.update()
    time.sleep(2)

    image2=pygame.image.load("C:/Users/prave/OneDrive - OMO Scholengroep Helmond/Desktop/Jetlearn/Pro_Game_Developer/images/birthday-2.jpg")
    font2=pygame.font.SysFont("Arial",36)
    text3=font2.render("Wish you a bright future ahead",True,(0,0,0))
    screen.fill((255,255,255))
    screen.blit(image2,(0,0))
    screen.blit(text3,(30,30))
    pygame.display.update()
    time.sleep(2)

    image3=pygame.image.load("C:/Users/prave/OneDrive - OMO Scholengroep Helmond/Desktop/Jetlearn/Pro_Game_Developer/images/birthday-3.jpg")
    screen.fill((255,255,255))
    screen.blit(image3,(0,0))
    pygame.display.update()
    time.sleep(2)    

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            exit(0)