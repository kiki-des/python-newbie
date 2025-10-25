import pygame
import random
import sys

pygame.init()

height = 300
width = 400
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello Shapes!")

black=(0,0,0)
silver=(192,192,192)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)

screen.fill(white)
pygame.draw.polygon(screen,green,((146,0),(291,106),(236,277),(56,277),(0,106)))
pygame.draw.rect(screen, red, (50, 50, 100, 50))
pygame.draw.circle(screen, blue,(200,150),40)
pygame.draw.line(screen,black,(0,0),(400,300),2)

pygame.draw.ellipse(screen, silver,(68,90,40,70))
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
sys.exit()