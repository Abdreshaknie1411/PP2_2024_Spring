import pygame

pygame.init()

w = 800
h = 600

screen = pygame.display.set_mode([w, h])
pygame.display.set_caption("Paint")

def draw_cross(surface, color, position, size):
    pygame.draw.line(surface, color, (position[0] - size, position[1]), (position[0] + size, position[1]), 2)
    pygame.draw.line(surface, color, (position[0], position[1] - size), (position[0], position[1] + size), 2)

run = True
while run:
    screen.fill('white')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

    draw_cross(screen, 'black', (w // 2, h // 2), 50)

    pygame.display.flip()