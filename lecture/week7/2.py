import pygame
pygame.init()
wigth=500
heigth=500
screen=pygame.display.set_mode((heigth,wigth))
ball_radius=25
ball_x=wigth//2
ball_y=heigth//2
done=True
white=(255,255,255)
red=(255,0,0)
while  done:
    screen.fill(white)
    pygame.draw.circle(screen,red,(ball_x,ball_y),ball_radius)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                if ball_y -20 >=ball_radius:
                    ball_y-=20
            elif event.key==pygame.K_DOWN:
                if ball_y+20<=heigth-ball_radius:
                    ball_y+=20
            elif event.key==pygame.K_LEFT:
                if ball_x-20>=ball_radius:
                    ball_x-=20
            elif event.key==pygame.K_RIGHT:
                if ball_x+20<=heigth-ball_radius:
                    ball_x+=20
                  
    pygame.display.flip()
