import pygame
from datetime import datetime

pygame.init()
w=800
h=800
fps=60
screen=pygame.display.set_mode((w,h))
clock=pygame.time.Clock()
pygame.display.set_caption('mickeyclock')
mickey_image = pygame.image.load("mickeyclock.jpeg")
mickey_image.get_rect(center=(w/2,h/2))

running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        screen.blit(mickey_image,(0,0))
        pygame.display.flip()
        pygame.display.update()
