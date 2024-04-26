import pygame 
from random import randrange
res=800
size=40
pygame.init()
img=pygame.image.load('1.jpg')
x,y=randrange(size, res - size, size),randrange(size,res-size,size)
apple=randrange(size,res-size,size),randrange(size,res-size,size)
dirs={'W':True,'S':True,'A':True,'D':True,}
font_score=pygame.font.SysFont("Arial Black", 26)
font_end=pygame.font.SysFont("Arial Black", 66)
font_level=pygame.font.SysFont("Arial Black", 26)
#fender_end=font_end.render('GAME OVER',True,pygame.Color('orange'))
apple_image=pygame.image.load('unnamed.jpg')


pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

#colors=[(randrange(0,255),randrange(0,255),randrange(0,255)) for _ in range(10)]
fps=6
snake=[(x,y)]
dx,dy=0,0
length=1
score=0
level=0
num_lives=2
#speed_count, snake_speed = 0, 10
color_index=0

screnn=pygame.display.set_mode((res,res))
pygame.display.set_caption('Snake')
clock=pygame.time.Clock()



running=True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    
    screnn.blit(apple_image,apple)
    screnn.blit(img, (0,0))
    #drawing snake, apple
    [(pygame.draw.rect(screnn,pygame.Color('blue'),(i,j,size-2,size-2))) for i,j in snake]
    pygame.draw.rect(screnn,pygame.Color('red'),(*apple,size,size))
    #show score
    
    fender_score=font_score.render(f'SCORE: {score}', True, pygame.Color('orange'))
    screnn.blit(fender_score, (5,5))
    fender_level=font_level.render(f'LEVEL: {level}', True,pygame.Color('orange'))
    screnn.blit(fender_level,(5,30))
    #snake movement
    '''speed_count += 2
    if not speed_count % snake_speed:'''
    x+=dx*size
    y+=dy*size
    snake.append((x,y))
    snake=snake[-length:]
    
    #eating apple
    if snake[-1]==apple:

        apple=randrange(0,res,size),randrange(0,res,size)
        length +=1
        fps +=1
        score+=1
       # snake_speed -= 1
        #snake_speed = max(snake_speed, 4)
        #color_index=(color_index+1)%len(colors)
        level+=1
    
    for i,(sx,sy) in enumerate(snake):
        if i == len(snake)-1:
            pygame.draw.rect(screnn,pygame.Color('blue'),(sx,sy, size-2,size-2))
        else:
            pygame.draw.rect(screnn,pygame.Color('yellow'),(sx,sy,size-2,size-2))
    #game over
    if x<0 or x>res-size or y<0 or y>res-size or len(snake) != len(set(snake)):
        num_lives-=1
        if num_lives>0:
            x,y=randrange(size, res - size, size),randrange(size,res-size,size)
            snake=[(x,y)]
            dx,dy=0,0
            length=1
            continue
        else:



            running=False
            fender_end=font_end.render('GAME OVER',True,pygame.Color('orange'))
            screnn.blit(fender_end,(res//2-200,res//3))
            pygame.display.flip()
            break
    
    #control
    key=pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx,dy=0,-1
        dirs={'W':True,'S':False,'A':True,'D':True,}
    if key[pygame.K_s] and dirs['S']:
        dx,dy=0,1
        dirs={'W':False,'S':True,'A':True,'D':True,}
    if key[pygame.K_a] and dirs['A']:
        dx,dy=-1,0
        dirs={'W':True,'S':True,'A':True,'D':False,}
    if key[pygame.K_d] and dirs['D']:
        dx,dy=1,0
        dirs={'W':True,'S':True,'A':False,'D':True,}

    pygame.display.flip()
    clock.tick(fps)
